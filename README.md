# OPENCV-CAR-DETECTION1

This is a simple real-time colour based object tracker built using OpenCV.

Features:
1. Real-time colour-based object detection
2. HSV colour space segmentation
3. Contour detection and filtering
4. Bounding box tracking

It basically captures video frames, converts them from BGR to HSV, and then
applies colour masks to isolate the target object.
It then draws a bounding box around the detected car and then displays the
processed video in real time.

The objective of this project was to gain hands on experience with the core 
concepts of OpenCV by implementing a simple yet effective colour-based object 
tracking system

The benchmarking showed that colour conversion and masking consume most of the 
processing time, as both operations examine every pixel in the frame. Contour 
detection and drawing operations are comparatively inexpensive since they only
process detected object boundaries.

The demo videos are uploaded alongwith the project.
