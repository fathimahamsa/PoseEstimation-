import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV range for BLUE color
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply mask to get blue regions
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show windows
    cv2.imshow("Original", frame)
    cv2.imshow("Blue Detection", result)

    # Close on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Close when any window is closed
    if cv2.getWindowProperty("Original", cv2.WND_PROP_VISIBLE) < 1 or \
       cv2.getWindowProperty("Blue Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()




