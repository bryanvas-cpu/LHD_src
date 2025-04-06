import cv2
import numpy as np
import heapq


def load_and_threshold(image_path):

    image = cv2.imread(image_path)
    cv2.imshow("image", image)
    if image is None:
        raise FileNotFoundError("Error: Could not load image.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    
    _, thresh = cv2.threshold(gray, 206,255,cv2.THRESH_BINARY)
    cv2.imshow("thresh",thresh)

    blurred_image = cv2.GaussianBlur(thresh, (25, 25), 0)
    cv2.imshow("blurred_image",blurred_image)
    
    cost_map = np.where(thresh == 0, 0, blurred_image)
    cv2.imshow("cost_map",cost_map)

    # bitmap = (thresh == 255).astype(np.uint8)
    # cv2.imshow("bitmap",bitmap)
    
    return cost_map

def heuristic(a, b):
    """Heuristic function (Manhattan distance)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(pix_map, start, goal):
    """
    A* algorithm using a pix-map where pixel values represent movement cost.
    Lower pixel values (darker) mean higher movement costs.
    """
    rows, cols = pix_map.shape
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
                pixel_cost = 255 - pix_map[neighbor]
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
def visualize_path(image_path, path):
    """Visualizes the path on the original image."""
    image = cv2.imread(image_path)
    for (x, y) in path:
        image[x, y] = (0, 0, 255)  # Red color for path
    cv2.imshow("Path", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # EDIT THESE VALUES AS NEEDED
    image_path = "/home/bryan/lhd_ws/src/lhd_mapping/maps/mine/mine_gimp.png"  # Provide your image path
    start_x = 119
    start_y = 111
    
    end_x = 119
    end_y = 350
    
    start = (start_y, start_x)  # (y, x) start position in pixels
    goal = (end_y, end_x)  # (y, x) goal position in pixels
    buffer_size = 5  # Buffer around obstacles

    cost_map = load_and_threshold(image_path)

    path = a_star(cost_map, start, goal)

    if path:
        print("Path found!")
        visualize_path(image_path, path)
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
