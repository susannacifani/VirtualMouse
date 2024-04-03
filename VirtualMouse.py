import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7
#########################

pTime = 0
#use these values to smoothen the movement of the mouse
plocX, plocY = 0, 0 #previous locations of the mouse
clocX, clocY = 0, 0 #current locations of the mouse

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()


while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    #print(lmList) #è tutto []

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print(x1, y1, x2, y2)

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        

        # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0: #index up, middle down
            # 5. Convert Coordinates
            #x3 = np.interp(x1, (0, wCam), (0, wScr))
            #y3 = np.interp(y1, (0, hCam), (0, hScr))
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr)) #TODO out of bound
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move Mouse
            #autopy.mouse.move(x3, y3)
            autopy.mouse.move(wScr -clocX, clocY) #flip dx and sx
            #autopy.mouse.move(wScr - clocX, clocY) #
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 8. Both Index and middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1: #index up, middle up
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            #print(length)
            # 10. Click mouse if distance between index and middle is shorter than 40 (threshold)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()


    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)