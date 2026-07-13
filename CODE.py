import cv2 as cv
import numpy as np
import time

vid = cv.VideoCapture("cars.mp4")

fps = vid.get(cv.CAP_PROP_FPS)
frame_time = 1000 / fps
lower_red1 = np.array([0, 80, 40])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 80, 40])
upper_red2 = np.array([180, 255, 255])

hsv_times = []
mask_times = []
contour_times = []
draw_times = []

frame_count = 0

trail_points = []


while True:
    start = time.time()

    ret, frame = vid.read()

    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv.bitwise_or(mask1,mask2)

    contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    if contours:
        largest = max(contours, key=cv.contourArea)
        area = cv.contourArea(largest)
        if area > 500:
            x, y, w, h = cv.boundingRect(largest)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame, "McQueen", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


    if area>500:
        x,y,w,h = cv.boundingRect(largest)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = (x+w//2, y+h//2)

    cv.imshow("Cars", frame)
    cv.imshow("Mask", red_mask)

    elapsed = (time.time() - start) * 1000
    remaining_delay = max(1, int(frame_time - elapsed))

    if cv.waitKey(remaining_delay) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
