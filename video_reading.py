import cv2

cap = cv2.VideoCapture('video.mp4') #videos are read by frames we can give 0,1 to on front cam

while(True):
    #capture frame by frame
    ret, frame = cap.read() 

    #Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):  #25 normal speed, extra code to get video close atomatically when i press 'q'
        break

cap.release()

cv2.destroyAllWindows() #to destroy all background data
    
