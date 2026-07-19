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
concepts of OpenCV by implementing a simple yet effective colour-based object
tracking system.

# Performance Notes

The benchmarking showed that colour conversion and masking consume most of the
processing time, as both operations examine every pixel in the frame. Contour
detection and drawing operations are comparatively inexpensive since they only
process detected object boundaries.

# Demo
The demo videos are attached alongwith the code.
The demo videos are attached alongwith the code.
