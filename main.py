import time

import cv2
#version 4.5.5.62 being used on this laptop

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
while True:
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grey_frame_gau

    delta_frame = cv2.absdiff(first_frame, grey_frame_gau)
    cv2.imshow("My video", delta_frame)

    key = cv2.waitKey(1)
    #video processing happens here
    if key == ord("q"):
        break

video.release()


#array = cv2.imread("image.png")





#print(array.shape)
#print(array)
