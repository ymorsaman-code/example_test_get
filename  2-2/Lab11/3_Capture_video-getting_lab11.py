import cv2
import os

video_file = "output.avi"
output_folder = "images"

# สร้างโฟลเดอร์เก็บภาพ
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_file)

fps = cap.get(cv2.CAP_PROP_FPS)   # จำนวนเฟรมต่อวินาที
frame_interval = int(fps)
print(frame_interval)

frame_count = 0
image_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # บันทึกภาพทุก 1 วินาที
    if frame_count % frame_interval == 0:
        filename = f"{output_folder}/output{image_count}.jpg"
        cv2.imwrite(filename, frame)
        print("Saved:", filename)
        image_count += 1

    frame_count += 1

cap.release()

print("เสร็จแล้ว ได้ภาพทั้งหมด", image_count, "ภาพ")