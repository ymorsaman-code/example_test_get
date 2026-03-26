import cv2

haarcascade_frontalface_default = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/haarcascade_frontalface_default.xml"
haarcascade_eye = '/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/haarcascade_eye.xml'
Nariz = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/Nariz.xml"
Mouth = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/mouth.xml"
eyeglass = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/haarcascade_eye_tree_eyeglasses.xml"
smile = "/Users/mac/Downloads/drive-download-20260316T072203Z-1-001/haarcascade_smile.xml"

faceCascade  = cv2.CascadeClassifier(haarcascade_frontalface_default)
eyesCascade  = cv2.CascadeClassifier(haarcascade_eye)
noseCascade  = cv2.CascadeClassifier(Nariz)
mouthCascade = cv2.CascadeClassifier(Mouth)
eyeglassCascade = cv2.CascadeClassifier(eyeglass)
smileCascade = cv2.CascadeClassifier(smile)


def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize=(55, 55))
        coords=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img,coords 
        
def detect(img,faceCascade,eyesCascade,noseCascade,mouthCascade,eyeglassCascade,smileCascade):
        # สั่งตรวจจับแต่ละส่วน: (ภาพ, ตัวตรวจจับ, ScaleFactor, MinNeighbors, สี BGR, ข้อความ)
        # ScaleFactor (1.1): ย่อภาพทีละ 10% เพื่อหาขนาดที่ต่างกัน
        # MinNeighbors (img,faceCascade,1.1,     20): ความเข้มงวดในการยืนยันวัตถุ (ยิ่งมากยิ่งแม่นแต่หายาก)
        
        img,coords=draw_boundary(img,faceCascade,1.1,20,(0,0,255),"Face")           # สีแดง
        img,coords=draw_boundary(img,eyesCascade,1.1,20,(0,255,0),"Eye")           # สีเขียว
        img,coords=draw_boundary(img,noseCascade,1.1,20,(255,0,0),"Nose")          # สีน้ำเงิน
        img,coords=draw_boundary(img,mouthCascade,1.1,20,(0,165,255),"Mouth")     # สีส้ม
        img,coords=draw_boundary(img,eyeglassCascade,1.1,20,(255,255,0),"Eyeglass") # สีฟ้า (Cyan)
        img,coords=draw_boundary(img,smileCascade,1.1,100,(255,0,255),"Smile")     # สีชมพู (Magenta)
        
        return img

        
cap = cv2.VideoCapture(0)

while (True):
        ret,frame = cap.read()
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)  # ย่อภาพ 50% เพื่อลด lag
        frame=detect(frame,faceCascade,eyesCascade,noseCascade,mouthCascade,eyeglassCascade,smileCascade)
        
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1) & 0xFF== ord('q')):
            break
        
cap.release()
cv2.destroyAllWindows()