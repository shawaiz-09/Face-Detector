import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
vid_cap=cv2.VideoCapture(0)
while True:
    ret,vid_data=vid_cap.read()
    col=cv2.cvtColor(vid_data,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(
        col,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30,30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(vid_data,(x,y),(x+w,y+h),(0,0,200),5)
        cv2.imshow("shawaiz Camera", vid_data)
    if cv2.waitKey(1)== ord("a"):
            break
vid_cap.release()