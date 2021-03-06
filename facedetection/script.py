import cv2 #importing open cv library.     

def generate_dataset(img, id, img_id):
    cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg", img)

def draw_boundary(img, classifier, scalefactor, minNeighbours, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features =  classifier.detectMultiScale(gray_img, scalefactor, minNeighbours)
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y),(x+w, y+h), color,2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords= [x, y, w, h]

    return coords, img

def detect(img, faceCascade, img_id):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0, 255,0)}
    coords, img = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")
    if len(coords)==4:
        roi_img= img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]

        user_id= 1
        generate_dataset(roi_img, user_id, img_id)
    return img

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
video_capture = cv2.VideoCapture(0)

img_id= 0
while True:
    _, img = video_capture.read()
    img = detect(img, faceCascade, img_id)
    cv2.imshow("face detection", img)
    img_id +=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()