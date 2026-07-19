# OPENCV-CAR-DETECTION1

# Overview

This is a simple real-time colour based object tracker built using OpenCV.

# Features

Real-time colour-based object detection
HSV colour space segmentation
Contour detection and filtering
Bounding box tracking

# How It Works

It basically captures video frames, converts them from BGR to HSV, and then
applies colour masks to isolate the target object.
It then draws a bounding box around the detected car and then displays the
processed video in real time.

# Objective

The objective of this project was to gain hands on experience with the core
concepts of OpenCV by implementing a simple colour based object tracking
system.

# Benchmarks

The benchmarking showed that colour conversion and masking consume most of the
processing time, as both operations examine every pixel in the frame. Contour
detection and drawing operations are comparatively less consuming since they only
process detected object boundaries.

The demo videos are attached alongwith the code.

## OpenCV Functions Learned

| Function | Purpose |
|---|---|
| `cv.imread()` | Loading an image |
| `cv.VideoCapture()` | Opening and reading a video file |
| `cv.cvtColor()` | Converting BGR to HSV frame by frame |
| `cv.inRange()` | Checks if pixels are in the HSV range for masking |
| `cv.bitwise_or()` | Combines the two red range masks into one |
| `cv.findContours()` | Detect the shape of the object region |
| `cv.contourArea()` | Calculates the enclosed area of a contour and selects the largest contour while filtering out noise |
| `cv.boundingRect()` | Generates the coordinates for the tracking box |
| `cv.rectangle()` | Draws a rectangle on the image, visualizing the car's boundary on each frame |
| `cv.circle()` | Marks a reference pixel on the image |
| `cv.imshow()` | Displaying an image or frame |
| `cv.waitKey()` | Controlling how long we want the image to show |
| `cv.destroyAllWindows()` | Close all OpenCV windows |
