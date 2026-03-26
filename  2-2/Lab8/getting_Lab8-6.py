import librosa
import librosa.display
import matplotlib.pyplot as plt
import urllib.request # ใช้สำหรับดาวน์โหลดไฟล์จาก URL

# 1. ระบุ URL ของไฟล์เสียง (ต้องเป็น Direct Link ที่ลงท้ายด้วย .wav หรือ .mp3)
# สมมติ URL นี้เป็นไฟล์เสียงสุนัขที่เรา copy มาจาก Freesound หรือเว็บอื่นๆ

# ใช้ของ github แทน freesound ที่ต้อง login
url = "https://github.com/karolpiczak/ESC-50/raw/master/audio/1-30226-A-0.wav"
# (หมายเหตุ: ลิงก์ด้านบนเป็นตัวอย่างไฟล์ทดสอบ หากมีลิงก์จริงให้แทนที่ตรงนี้ได้เลยค่ะ)

save_filename = "dog_barking.wav"

# 2. ขั้นตอนการดึงไฟล์แบบอัตโนมัติ (Automated Download)
print(f"กำลังดาวน์โหลดไฟล์จาก: {url}")
urllib.request.urlretrieve(url, save_filename)
print("ดาวน์โหลดเสร็จสิ้น!")

# 3. ขั้นตอนการประมวลผล (Load Data)
# y = ข้อมูลความดังของเสียง (Amplitude) ในรูปแบบอาเรย์ตัวเลข
# sr = Sampling Rate (อัตราการสุ่มตัวอย่าง เช่น 22050 Hz)
y, sr = librosa.load(save_filename) 

# 4. ขั้นตอนการแสดงผลกราฟ (Visualization)
plt.figure(figsize=(10, 4)) # กำหนดขนาดกราฟ
librosa.display.waveshow(y, sr=sr) # สร้างกราฟ Waveform

# ตกแต่งกราฟตามโจทย์
plt.title('Dog Barking Sound Waveform')
plt.xlabel('Time (seconds)') # แกน X คือ เวลา
plt.ylabel('Amplitude')      # แกน Y คือ ความดัง
plt.show()