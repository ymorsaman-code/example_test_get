import cv2

haarcascade_frontalface_default = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/haarcascade_frontalface_default.xml"
haarcascade_eye = '/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/haarcascade_eye.xml'
Nariz = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/Nariz.xml"
Mouth = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/mouth.xml"

faceCascade  = cv2.CascadeClassifier(haarcascade_frontalface_default)
eyesCascade  = cv2.CascadeClassifier(haarcascade_eye)
noseCascade  = cv2.CascadeClassifier(Nariz)
mouthCascade = cv2.CascadeClassifier(Mouth)

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize=(55, 55))
        coords=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img,coords 
        
def detect(img,faceCascade,eyesCascade,noseCascade,mouthCascade):
        img,coords=draw_boundary(img,faceCascade,1.1,10,(0,0,255),"Face")
        img,coords=draw_boundary(img,eyesCascade,1.1,12,(0,255,0),"Eye")
        img,coords=draw_boundary(img,noseCascade,1.1,20,(255,0,0),"Nose")
        img,coords=draw_boundary(img,mouthCascade,1.1,20,(255,255,0),"Mouth")
        
        return img

        
cap = cv2.VideoCapture(0)

while (True):
        ret,frame = cap.read()
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)  # ย่อภาพ 50% เพื่อลด lag
        frame=detect(frame,faceCascade,eyesCascade,noseCascade,mouthCascade)
        
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1) & 0xFF== ord('q')):
            break
        
cap.release()
cv2.destroyAllWindows()
