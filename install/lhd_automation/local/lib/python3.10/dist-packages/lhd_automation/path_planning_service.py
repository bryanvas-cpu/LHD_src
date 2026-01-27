#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from std_msgs.msg import Int32MultiArray
from lhd_msgs.srv import GetWaypoints
from tf_transformations import quaternion_from_euler
from geometry_msgs.msg import Quaternion
import cv2
import numpy as np
from PIL import Image, ImageDraw
import random
import heapq
import math
from scipy.interpolate import splprep, splev

def smooth_path(path, num_points=100):
    path = np.array(path)
    y, x = path[:, 0], path[:, 1]  # remember: (y, x)

    # Fit spline
    tck, _ = splprep([x, y], s=2.0)
    u_fine = np.linspace(0, 1, num_points)
    x_fine, y_fine = splev(u_fine, tck)

    return list(zip(y_fine, x_fine))  # back to (y, x)

def visualize_path(image_path, path):
    """Visualizes the path on the original image."""
    image = cv2.imread(image_path)
    for (x, y) in path:
        ix, iy = int(x), int(y) 
        image[ix, iy] = (0, 0, 255)  # Red color for path
    cv2.imshow("Path", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def a_star(cost_map, start, goal):
    """
    A* algorithm using a pix-map where pixel values represent movement cost.
    Lower pixel values (darker) mean higher movement costs.
    """
    
    rows, cols = cost_map.shape
    open_set = []
    heapq.heappush(open_set, (0, start))  # Priority queue

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    # 8-directional movement (including diagonals)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal moves
    ]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                # Invert pixel intensity: Darker = Higher Cost
                pixel_cost = 255 - cost_map[neighbor]
                if pixel_cost == 255:  # Treat 255 (white) as impassable
                    continue

                # Apply √2 cost for diagonal movement
                move_cost = pixel_cost * (1.414 if dx != 0 and dy != 0 else 1)

                tentative_g_score = g_score[current] + move_cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def heuristic(a, b):
    """Heuristic function (Manhattan distance)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def yaw_to_quaternion(yaw):
    q = quaternion_from_euler(0, 0, yaw)
    return Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])

class WayPoints(Node):

    def __init__(self):
        super().__init__('path_planning_service')
        self.paths = []
        self.image_path = "/home/bryan/lhd_ws/src/lhd_mapping/maps/mine/cost_map_kernel_31.png"
        self.original_image_path = "/home/bryan/lhd_ws/src/lhd_mapping/maps/mine/mine_gimp.png"
        self.cost_map = cv2.imread(self.image_path)
        self.cost_map = cv2.cvtColor(self.cost_map, cv2.COLOR_BGR2GRAY)
        self.srv = self.create_service(GetWaypoints, 'waypoints', self.waypoint_callback)
    
    def waypoint_callback(self, request, response):
        if request.start and request.end:
            
            start_x = int(request.start.position.x)
            start_y = int(request.start.position.y)
            
            end_x = int(request.end.position.x)
            end_y = int(request.end.position.y)
            
            start = (start_y, start_x)  # (y, x) start position in pixels
            goal = (end_y, end_x)  # (y, x) goal position in pixels

            path = a_star(self.cost_map, start, goal)
            if len(path) <= 25:
                self.get_logger().warn("Path has 20 or fewer waypoints. Rejecting request.")
                response.success = False  # Assuming you have a `success` field in the response
                # response.message = "Path too short. Must have more than 20 waypoints."
                return response
            
            # Skip the first 20 waypoints
            # path = path[10:]
            
            if path:
                print("Path found!")
                smoothed_path = smooth_path(path, num_points=100)
                response.waypoints.poses = [Pose() for _ in path]
                for i in range(len(path)):
                    x, y = float(path[i][1]), float(path[i][0])
                    response.waypoints.poses[i].position.x = x
                    response.waypoints.poses[i].position.y = y

                    if i < len(path) - 1:
                        dy = path[i + 1][0] - path[i][0]
                        dx = path[i + 1][1] - path[i][1]
                        # minus, cuz y axiz is inverted in image, compared to robot frame in sim
                        yaw = math.atan2(-dy, dx)
                        self.get_logger().info(f"dx,dy,yaw: {dx:.2f}, {dy:.2f}, {yaw:.2f}")
                    else:
                        # Last pose: use the yaw of the previous segment
                        dx = path[i][0] - path[i - 1][0]
                        dy = path[i][1] - path[i - 1][1]
                        # minus, cuz y axiz is inverted in image, compared to robot frame in sim
                        yaw = math.atan2(-dy, dx)
                        self.get_logger().info(f"dx,dy,yaw: {dx:.2f}, {dy:.2f}, {yaw:.2f}")

                    quat = yaw_to_quaternion(yaw)
                    response.waypoints.poses[i].orientation = quat
                visualize_path(self.original_image_path, path)
                response.success = True
                return response
            else:
                print("No path found.")
                response.success = False
                return response
        else:
            self.get_logger().info("Request rejected")
            response.success = False
            return response

def main():
    rclpy.init()
    waypoints = WayPoints()

    try:
        rclpy.spin(waypoints)
    except KeyboardInterrupt:
        waypoints.get_logger().info('KeyboardInterrupt, shutting down.\n')
    finally:
        waypoints.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
