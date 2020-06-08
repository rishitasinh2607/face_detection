import numpy as np
import cv2


img = np.zeros((512, 512, 3), np.uint8)

cv2.circle(img,(120,210), 63, (0,0,255), 2) #last 2 gives u full clr or no clr or thickness of line 
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (200,100), (300,0), (255, 0, 255), -1) #(blankscreen ,height,width,rbg clrs,thickness of line)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
