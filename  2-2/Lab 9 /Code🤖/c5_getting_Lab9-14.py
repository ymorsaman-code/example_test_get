# lab9 - 14
# C5: ทำสเปกโตรแกรม (Spectrogram) แล้วเซฟเป็นรูป

import urllib.request # ใช้สำหรับดาวน์โหลดไฟล์จาก URL

url = "https://github.com/karolpiczak/ESC-50/raw/master/audio/1-30226-A-0.wav"

sound_filename = "dog_barking.wav"

# 2. 
# ตอนการดึงไฟล์แบบอัตโนมัติ (Automated Download)
print(f"กำลังดาวน์โหลดไฟล์จาก: {url}")
urllib.request.urlretrieve(url, sound_filename)
print("ดาวน์โหลดเสร็จสิ้น!")

#------------------
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# สมมติว่าไฟล์ดาวน์โหลดมาแล้วชื่อ "dog_barking.wav" ตามโค้ดของคุณ
sound_filename = "dog_barking.wav"

# 1. โหลดข้อมูลเสียง
y, sr = librosa.load(sound_filename)

# 2. แปลงสัญญาณเสียงเป็น Spectrogram (หน่วยเดซิเบล)
D = librosa.stft(y) 
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# 3. วาดกราฟ
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz')

# ---------------------------------------------------------
# 4. เพิ่มคำอธิบายแกนเวลาและความถี่ให้ชัดเจน (ตามโจทย์สั่ง)
# ---------------------------------------------------------
plt.xlabel("Time (seconds)")               # คำอธิบายแกน X (เวลา)
plt.ylabel("Frequency ( Hz)")              # คำอธิบายแกน Y (ความถี่)

plt.colorbar(format='%+2.0f dB')      # แถบสีแสดงความดัง
plt.title('Spectrogram of Audio File')
plt.tight_layout()

# 5. เซฟเป็นไฟล์รูปภาพ (png)
output_img = "spectrogram_result.png"
plt.savefig(output_img)
plt.close() # ปิดกราฟเพื่อเคลียร์หน่วยความจำ

print(f"บันทึกไฟล์ภาพพร้อมคำอธิบายแกนสำเร็จ: {output_img}")