import cv2

img = cv2.imread('img.jpg',0) #to read  instead as 1 read it as clr 0 for black adn white
cv2.imshow('image',img) #to display
cv2.waitKey(1000)  #it takes in milli sec to close it automatic
cv2.imwrite('ris.jpg',img) # to create new file diff name 
cv2.destroyAllWindows() #to stop background running

