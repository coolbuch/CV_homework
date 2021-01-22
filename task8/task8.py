import numpy as np
from skimage.measure import label, regionprops
import skimage.morphology as morph
import matplotlib.pyplot as plt
import cv2
import mss
import pyautogui
from time import sleep



with mss.mss() as scr:  # Create a new mss.mss instance
    monitor = scr.monitors[1]  # Identify the display to capture
    monitor = {"top": 600, "left": 100, "width": 800, "height": 200}
      # Take the screenshot

    while(True):
        img = np.array(scr.grab(monitor))
        #cv2.imshow("window", img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        obstacle = img[130:140, 100:200]
        mediumBird = img[110:130, 110:200]
        dinoUp = img[0:40, 50:100]
        dinoBottom = img[60:80, 50:100]
        ret, obstacle = cv2.threshold(obstacle, 40, 255, 0)
        ret, dinoUp = cv2.threshold(dinoUp, 40, 255, 0)
        ret, dinoBottom = cv2.threshold(dinoBottom, 40, 255, 0)
        gray = np.array(dinoUp)
        cv2.imshow("image", mediumBird)
        cv2.imshow("imag2", obstacle)
        #cv2.imshow("image2", dino)
        #print(np.unique(obstacle))
        if (np.unique(obstacle)[0] == 0):
            pyautogui.keyDown("space")
        if (np.unique(dinoUp)[0] == 0 and np.unique(dinoBottom)[0] == 255):
            pyautogui.keyDown("down")
            # sleep(0.02)
            pyautogui.keyUp('down')
        if (np.unique(mediumBird)[0] == 0 and np.unique(obstacle)[0] == 255):
            pyautogui.keyDown("down")
           # pyautogui.keyDown('down')
            #sleep(0.05)
            #pyautogui.keyUp('down ')
         # x 150 - 170
        # y 120 - 140
        #if ()
        #pyauto gui.keyUp("space")
        #print(n p.average(gray[120:140][150:170]))
        #cv2.imshow("OKNO", gray)
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()