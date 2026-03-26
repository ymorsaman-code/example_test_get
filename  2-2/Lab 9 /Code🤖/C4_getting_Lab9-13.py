# lab9 - 13
# C4: แยกช่วงเสียงพูด/ไม่พูดแบบง่าย (Voice Activity Detection แบบคร่าว ๆ)



import urllib.request

import librosa # ใช้สำหรับดาวน์โหลดไฟล์จาก URL

url = "https://github.com/karolpiczak/ESC-50/raw/master/audio/1-30226-A-0.wav"

sound_filename = "dog_barking.wav"

#  ขั้นตอนการดึงไฟล์แบบอัตโนมัติ (Automated Download)
print(f"กำลังดาวน์โหลดไฟล์จาก: {url}")
urllib.request.urlretrieve(url, sound_filename)
print("ดาวน์โหลดเสร็จสิ้น!")

#------------------
# librosa.effects.split() สิ่งที่ฟังก์ชันนี้แอบทำอยู่หลังบ้านคือ:
# แบ่งเฟรม (Framing): มันจะทำการหั่นข้อมูลเสียง y ออกเป็นเฟรมย่อยๆ ให้เอง
# คำนวณพลังงาน (Energy Calculation): มันจะคำนวณหาพลังงานของแต่ละเฟรม (มักจะใช้สูตรทางสถิติที่เรียกว่า RMS - Root Mean Square) โดยที่เราไม่ต้องเขียนสูตรบวกเลขยกกำลังสองเอง
# เทียบ Threshold: มันนำพลังงานที่ได้ไปเทียบกับจุดตัดที่ตั้งไว้ (top_db=20)
# คืนค่า (Return): ส่งเฉพาะตำแหน่งเริ่มต้นและสิ้นสุด (intervals) กลับมาให้เรา

import librosa

# โหลดไฟล์เสียง
y, sr = librosa.load(sound_filename, sr=None)

# 3. ใช้ฟังก์ชัน split เพื่อหาช่วงที่มีเสียงโดยอัตโนมัติ
# top_db=20 หมายถึง เสียงที่เบากว่าเสียงที่ดังที่สุดเกิน 20 เดซิเบล (dB) จะถูกมองว่าเป็น "ความเงียบ"
intervals = librosa.effects.split(y, top_db=20)

# 4. แสดงผลลัพธ์ (intervals เก็บค่าเป็นตำแหน่ง index ของข้อมูล ต้องหารด้วย sr เพื่อแปลงเป็นวินาที)
print("เกิน threshold ถือว่า “พูด”")
for start_idx, end_idx in intervals:
    start_time = start_idx / sr
    end_time = end_idx / sr
    print(f"พบเสียงช่วงเวลา: {start_time:.3f} วินาที - {end_time:.3f} วินาที")