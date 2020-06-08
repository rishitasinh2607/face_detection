import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Best-Loan-for-Students.jpg', 1)
faces = face_cascade.detectMultiScale(img, 1.1,1) #img 1.1,1 is used to detect the rectangle on face

for(x,y,w,h) in faces:
    print(x,y,w,h)
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 5)

resized = cv2.resize(img, (500,500))

cv2.imshow('img', img)
cv2.imshow('img', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
