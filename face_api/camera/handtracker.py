import cv2
import mediapipe as mp
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
ds_factor=0.6

# camera = cv2.VideoCapture(0)

pTime = 0
cTime = 0

# while True:
#     success, img = camera.read()
#     imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     result = hands.process(imageRGB)

#     if result.multi_hand_landmarks:
#         for handLms in result.multi_hand_landmarks:
#             for i, lm in enumerate(handLms.landmark):
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 print(cx, cy)
#                 # if i == 0 : 
#                 cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)


#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

#     cTime = time.time()
#     fps = 1/(cTime - pTime)
#     pTime = cTime

#     cv2.putText(img, str(int(fps)), 
#                 (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#                 (255,0,255), 3
#     )


#     cv2.imshow("Image", img)
#     cv2.waitKey(1) 

class VideoCameraHand(object):
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
        # gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        result = hands.process(image)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                for i, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

        self.cTime = time.time()
        fps = 1/(self.cTime - self.pTime)
        self.pTime = self.cTime

        cv2.putText(image, str(int(fps)), 
                    (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255,0,255), 3
        )

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()