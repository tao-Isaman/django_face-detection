import cv2
import time
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
ds_factor=0.6

class VideoCameraFace(object):
    pTime = 0
    cTime = 0
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        image=cv2.flip(image,1)
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
        	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        	break
        self.cTime = time.time()
        fps = 1/(self.cTime - self.pTime)
        self.pTime = self.cTime

        cv2.putText(image, str(int(fps)), 
                    (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255,0,255), 3
        )
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()