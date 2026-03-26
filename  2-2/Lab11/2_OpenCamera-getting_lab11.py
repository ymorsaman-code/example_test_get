import cv2

# เปิดกล้อง (0 คือ webcam ตัวแรก)
cap = cv2.VideoCapture(0)

# กำหนด codec และไฟล์ output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # แสดงภาพ
    cv2.imshow('Recording', frame)

    # บันทึก frame ลงไฟล์
    out.write(frame)

    # กด q เพื่อหยุด
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดทุกอย่าง
cap.release()
out.release()
cv2.destroyAllWindows()