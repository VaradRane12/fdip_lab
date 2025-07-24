import cv2
import os
import time
import numpy as np

folder_path = "images"
display_time = 2 
transition_frames = 30  

image_files = sorted([f for f in os.listdir(folder_path)])

images = []
for file in image_files:
    img = cv2.imread(os.path.join(folder_path, file))
    images.append(img)

w, h = 1280, 720
resized_images = []

for img in images:
    resized = cv2.resize(img, (w, h))
    resized_images.append(resized)

images = resized_images


cv2.namedWindow("Slideshow", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Slideshow", w, h)

for i in range(len(images)):
    current = images[i]
    next_img = images[(i + 1) % len(images)]

    cv2.imshow("Slideshow", current)
    if cv2.waitKey(display_time * 1000) == 27:
        break 
    for t in range(transition_frames):
        alpha = t / transition_frames
        frame = cv2.addWeighted(current, 1 - alpha, next_img, alpha, 0)
        cv2.imshow("Slideshow", frame)
        if cv2.waitKey(30) == 27:
            break

cv2.destroyAllWindows()
