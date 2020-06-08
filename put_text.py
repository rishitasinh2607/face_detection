import numpy as np
import cv2


img = np.zeros((512, 512, 3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(img,(100,100),(420,410),(0,0,255),1)
cv2.putText(img,'rish', (184,500), font, 2, (255,255,255), 4)
cv2.imshow('name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
