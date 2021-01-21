#import cv2
#import numpy as np
#import random
#from skimage import measure

#camera = cv2.VideoCapture(1)

#while(camera.isOpened()):
    #ret, frame = camera.read()
    #HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #HSV = cv2.blur(HSV,(5,5))


    #cv2.imshow('frame', frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
#camera.release()
#cv2.destroyAllWindows()


import cv2
import numpy as np
import random


def findBall(blurred, lower, upper):
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    countours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ballCoords = 0
    if len(countours) > 0:
        c = max(countours, key=cv2.contourArea)
        (X, Y), rad = cv2.minEnclosingCircle(c)
        if rad > 25:
            cv2.circle(frame, (int(X), int(Y)),
                       int(rad), (0, 255, 255), 2)
            ballCoords = int(X)

    return ballCoords


cam = cv2.VideoCapture(2)

masks = {
    "RED": np.array(([176, 0, 0], [180, 255, 255])),
    "GREEN": np.array(([49, 0, 0], [74, 255, 255])),
    "YELLOW": np.array(([21, 0, 0], [28, 255, 255])),
}

colors = ["RED", "YELLOW", "GREEN"]
random.shuffle(colors)
print(colors)
while cam.isOpened():
    ret, frame = cam.read()
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    queue = {}
    for colorname, mask in masks.items():
        ball = findBall(blurred, mask[0], mask[1])
        if ball:
            queue[colorname] = ball
    answers = []
    for key in sorted(queue, key=lambda x: queue[x]):
        answers.append(key)
    if (colors == answers):
        cv2.putText(frame, "Right queue", (200, 50), cv2.QT_FONT_NORMAL, 0.9, (0, 0, 255))
    else:
        cv2.putText(frame, "Not right queue", (200, 50), cv2.QT_FONT_NORMAL, 0.9, (0, 0, 255))
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow("Camera", frame)

cam.release()
cv2.destroyAllWindows()

