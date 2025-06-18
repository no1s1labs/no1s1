import time
import cv2
from time import sleep

t_cam_end = time.time() +30*3 # 3 minute loop


def camcheck():

 while time.time()<t_cam_end:
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    #print(data)
    if (bbox is not None):
     if data:
       print(data)
       return data
       break
    # display the image preview
    #cv2.imshow("code detector", img)
# free camera object and exit
    cap.release()
    cv2.destroyAllWindows()



data=camcheck()
print(data)


