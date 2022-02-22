import cv2
recog=cv2.VideoCapture(0)
while(True):
    ret,frame = recog.read()
    cv2.imshow('aditya', frame) 
    cv2.imwrite('test_photo/aditya.jpg',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
#release()
recog.release()
cv2.destroyAllWindows()