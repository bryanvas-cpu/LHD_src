import cv2

# Callback function for mouse click
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        print(f"Clicked at: ({x}, {y})")

# Load the image
image_path = "/home/bryan/lhd_ws/src/lhd_mapping/maps/mine/mine_gimp_calibration.png"  # Change this to your image file
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

if image is None:
    print("Error: Could not load image.")
else:
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", get_coordinates)

    while True:
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Press 'Esc' to exit
            break

    cv2.destroyAllWindows()
