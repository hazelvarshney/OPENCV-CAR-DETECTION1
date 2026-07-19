import cv2 as cv
import numpy as np
import time

vid = cv.VideoCapture("f1.mp4")

fps = vid.get(cv.CAP_PROP_FPS)
frame_time = 1000 / fps
lower_red1 = np.array([0, 150, 40])
upper_red1 = np.array([4, 255, 255])

lower_red2 = np.array([160, 50, 50])
upper_red2 = np.array([180, 255, 255])

lower_mclaren = np.array([5, 65, 40])
upper_mclaren = np.array([22, 255, 255])

kernel = np.ones((5, 5), np.uint8)

hsv_times = []
mask_times = []
contour_times = []
draw_times = []

frame_count = 0

cv.namedWindow("Cars", cv.WINDOW_NORMAL)
cv.resizeWindow("Cars", 960, 540)

def print_hsv(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(hsv[y, x])

cv.setMouseCallback("Cars", print_hsv)

while True:
    start = time.time()

    ret, frame = vid.read()

    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv.bitwise_or(mask1, mask2)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_CLOSE, kernel)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)

    contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        for c in contours:
            area = cv.contourArea(c)
            if area > 500:
                x, y, w, h = cv.boundingRect(c)
                rect_area = w * h
                extent = area / float(rect_area)
                if extent > 0.5:
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv.putText(frame, "Ferrari", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    mclaren_mask = cv.inRange(hsv, lower_mclaren, upper_mclaren)
    mclaren_mask = cv.morphologyEx(mclaren_mask, cv.MORPH_CLOSE, kernel)
    mclaren_mask = cv.morphologyEx(mclaren_mask, cv.MORPH_OPEN, kernel)

    mclaren_contours, _ = cv.findContours(mclaren_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if mclaren_contours:
        for c in mclaren_contours:
            area = cv.contourArea(c)
            if area > 500:
                x, y, w, h = cv.boundingRect(c)
                rect_area = w * h
                extent = area / float(rect_area)
                if extent > 0.5:
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    cv.putText(frame, "McLaren", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv.imshow("Cars", frame)
    cv.imshow("Mask", red_mask)

    elapsed = (time.time() - start) * 1000
    remaining_delay = max(1, int(frame_time - elapsed))

    if cv.waitKey(remaining_delay) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
