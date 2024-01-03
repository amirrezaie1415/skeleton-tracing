import trace_skeleton
import cv2
import random

# Load the image
im = cv2.imread("../test_images/SVS_2_LS43_to_LS44_RS6_0000_0_mask.png", 0)

# Apply threshold
_, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

# Resize the image for display if it's too large
max_display_size = 800  # Maximum display size
h, w = im.shape[:2]
if h > max_display_size or w > max_display_size:
    scaling_factor = max_display_size / float(h) if h > w else max_display_size / float(w)
    im = cv2.resize(im, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

# Trace skeleton
polys = trace_skeleton.from_numpy(im)

# Draw lines
for l in polys:
    c = (200 * random.random(), 200 * random.random(), 200 * random.random())
    for i in range(0, len(l) - 1):
        cv2.line(im, (l[i][0], l[i][1]), (l[i + 1][0], l[i + 1][1]), c)

# Display the image
cv2.imshow('', im)
while True:
    # Break the loop when 'q' is pressed or the window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

