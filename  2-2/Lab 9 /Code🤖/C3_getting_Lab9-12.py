# lab9 - 12
# C3: ตัดเงียบหัว-ท้าย (Trim Silence)

import urllib.request # ใช้สำหรับดาวน์โหลดไฟล์จาก URL

url = "https://github.com/karolpiczak/ESC-50/raw/master/audio/1-30226-A-0.wav"

sound_filename = "dog_barking.wav"

# 2. ขั้นตอนการดึงไฟล์แบบอัตโนมัติ (Automated Download)
print(f"กำลังดาวน์โหลดไฟล์จาก: {url}")
urllib.request.urlretrieve(url, sound_filename)
print("ดาวน์โหลดเสร็จสิ้น!")

#------------------

import librosa
import soundfile as sf

# โหลดข้อมูลเสียง
# y คือ ข้อมูลคลื่นเสียง (Array)
# sr (Sample Rate) คือ ความละเอียดของเสียง (จำนวนจุดข้อมูลต่อ 1 วินาที)
y, sr = librosa.load(sound_filename, sr=None) 

#  คำนวณความยาวก่อนตัด (วินาที)
duration_before = len(y) / sr 

#  กระบวนการตรวจจับและตัดช่วงเงียบ (Trim)
# db = 20 คือเสียงอยู่ในช่วงเบามาก 
# top_db=20 หมายถึง กำหนด Threshold ว่าเสียงที่เบากว่า "เสียงที่ดังที่สุดในไฟล์" เกิน 20 เดซิเบล (Decibel) ให้ถือเป็นความเงียบและตัดทิ้ง
y_trimmed, index = librosa.effects.trim(y, top_db=20)

#  คำนวณความยาวหลังตัด (วินาที)
duration_after = len(y_trimmed) / sr

# กำหนดชื่อไฟล์ผลลัพธ์หลังจากตัดเสียงแล้ว
output_filename = "dog_barking_silence.wav"

# ตัดออกแล้วเซฟเป็นไฟล์ใหม่
sf.write(output_filename, y_trimmed, sr)

#  ผลลัพธ์: แสดงความยาวก่อน/หลัง
print("-" * 10)
print(f"ตัดเสียงเงียบเรียบร้อยแล้ว")
print(f"ความยาวก่อนตัด: {duration_before:.4f} วินาที")
print(f"ความยาวหลังตัด:  {duration_after:.4f} วินาที")
print(f"พื้นที่เสียงเงียบที่ถูกตัดออก: {duration_before - duration_after:.4f} วินาที")
print(f"ไฟล์ใหม่ถูกบันทึกในชื่อ: {output_filename}")