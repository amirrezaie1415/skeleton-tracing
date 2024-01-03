import trace_skeleton
import cv2
import random

# Load the image
im = cv2.imread("../test_images/SVS_2_LS43_to_LS44_RS6_0000_0_mask.png", 0)

# Apply threshold
_, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

# Trace skeleton
polys = trace_skeleton.from_numpy(im)

# Draw lines
for l in polys:
    c = (200 * random.random(), 200 * random.random(), 200 * random.random())
    for i in range(0, len(l) - 1):
        cv2.line(im, (l[i][0], l[i][1]), (l[i + 1][0], l[i + 1][1]), c)

# Create a resizable window with a valid name
window_name = 'Display Window'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Set the window size (change the width and height as needed)
window_width, window_height = 800, 600
cv2.resizeWindow(window_name, window_width, window_height)

# Display the image
cv2.imshow(window_name, im)
while True:
    # Break the loop when 'q' is pressed or the window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

