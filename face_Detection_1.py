
import cv2
from mtcnn.mtcnn import MTCNN
#from ExcelFile import attendance
from ExcelFile import attendance
from predict import predict
detector = MTCNN()

video = cv2.VideoCapture(0)

if (video.isOpened() == False):
    print("Web Camera not detected")
while (True):
    ret, frame = video.read()
    cv2.imwrite("AdityaJaishi.jpg",frame)
    
    frame = cv2.flip(frame, 1)
    # x = 1
    # print(type(frame))
    if ret == True:
        location = detector.detect_faces(frame)
        if len(location) > 0:
            for face in location:
                font = cv2.FONT_HERSHEY_SIMPLEX
                x, y, width, height = face['box']
                x2, y2 = x + width, y + height
                cv2.rectangle(frame, (x, y), (x2, y2), (0, 0, 255), 2)
                # t1 = time.time()
                # cv2.imwrite(str(x) + '.jpg', frame[x:x2, y:y2])
                # x += 1
                try:
                    predicted_name =  predict('AdityaJaishi.jpg')
                    cv2.putText(frame, 
                        predicted_name, 
                        (x, y), 
                        font, 0.5, 
                        (0, 128, 0), 
                        2, 
                        cv2.LINE_4
                    )
                    print("predicted name:",predicted_name)
                    attendance(predicted_name)
                except:
                    pass
                #text_to_speech(predicted_name)
                # t2 = time.time()
                # print(t2 - t1)
        cv2.imshow("Output",frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
#print(predicted_name (score))
video.release()
cv2.destroyAllWindows()