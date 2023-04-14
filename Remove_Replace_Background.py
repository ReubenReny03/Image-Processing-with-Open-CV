import cv2
import numpy as np 
  
video = cv2.VideoCapture(0)
image = cv2.imread("task_5\\boring.jpg")
  
while True:
  
    ret, frame = video.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  
    u_green = np.array([179,116,160])
    l_green = np.array([0,0,0])
  
    mask = cv2.inRange(frameHSV, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)
  
    f = res
    cv2.imshow("two", f)
    f = np.where(f == 0, image, f)
  
    # cv2.imshow("video", frame)
    # cv2.imshow("res", mask)
    cv2.imshow("one", f)

  
    if cv2.waitKey(25) == ord('q'):
        break 
  
video.release()
cv2.destroyAllWindows()
