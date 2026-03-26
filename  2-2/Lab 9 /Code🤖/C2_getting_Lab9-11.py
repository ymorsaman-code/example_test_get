# lab9 - 10
# c2  ปรับความดัง + normalize
# โจทย์: รับไฟล์เสียง (.wav หรือ .mp3)

import urllib.request # ใช้สำหรับดาวน์โหลดไฟล์จาก URL

url = "https://github.com/karolpiczak/ESC-50/raw/master/audio/1-30226-A-0.wav"

sound_filename = "dog_barking.wav"

# 2. ขั้นตอนการดึงไฟล์แบบอัตโนมัติ (Automated Download)
print(f"กำลังดาวน์โหลดไฟล์จาก: {url}")
urllib.request.urlretrieve(url, sound_filename)
print("ดาวน์โหลดเสร็จสิ้น!")

#------------------
# Normalize (การทำให้เป็นมาตรฐาน): คือการปรับระดับความดังของเสียงทั้งหมดในไฟล์ให้เพิ่มขึ้นหรือลดลงในสัดส่วนที่เท่ากัน เพื่อให้จุดที่ดังที่สุดของไฟล์ (Peak) ไปแตะที่ระดับเป้าหมายที่เราตั้งไว้ (ในโจทย์นี้คือ -1 dBFS)
import urllib.request
from pydub import AudioSegment

# ----------------------------------
# 2. ขั้นตอนการประมวลผลเสียง (Audio Processing

# โหลดไฟล์เสียงที่ดาวน์โหลดมา
audio = AudioSegment.from_file(sound_filename)

# วัดระดับความดังก่อนปรับ เสียง
current_peak = audio.max_dBFS # ค่าความดังสูงสุดในไฟล์ (Peak Level)
current_rms = audio.dBFS      # ค่าความดังเฉลี่ย (RMS Level)
print(">> ก่อนปรับความดัง:")
print(f"   Peak Level: {current_peak:.2f} dBFS")
print(f"   RMS Level:  {current_rms:.2f} dBFS")

#--------------------------------
# โจทย์กำหนดเป้าหมายเป็น -1 dBFS ต้องการให้จุดที่ดังที่สุดของไฟล์เสียงไปแตะที่ระดับ -1 dBFS
# กำหนดเป้าหมายเป็น -1 dBFS และคำนวณส่วนต่าง
target_peak = -1.0
change_in_dB = target_peak - current_peak   # ยกตัวอย่าง ถ้า current_peak = -5 dBFS -->  change_in_dB = (-1) - (-5) = +4 dB (ต้องปรับเพิ่มความดังอีก 4 dB)
                                            # ถ้า current_peak = -0.5 dBFS --> change_in_dB = (-1) - (5) =  -6 dB (ต้องปรับลดความดังลง 0.5 dB)
print(f"\n คำนวณส่วนต่าง: ต้องปรับความดังเพิ่ม {change_in_dB:+.2f} dB")

#--------------------------------
# ปรับความดัง (บวกค่า dB ที่ขาดไป)
normalized_audio = audio + change_in_dB

# วัดระดับความดังหลังปรับ (After)
new_peak = normalized_audio.max_dBFS
new_rms = normalized_audio.dBFS
print("\n หลังปรับความดัง:")
print(f"   Peak Level: {new_peak:.2f} dBFS")
print(f"   RMS Level:  {new_rms:.2f} dBFS")

#----------------------------------
# เตรียมไฟล์ทีีเราทำการ normalize เสร็จแล้วจะบันทึกเป็นชื่อใหม่เพื่อไม่ให้ทับไฟล์ต้นฉบับ
output_filename = "dog_barking_normalized.wav"

# บันทึกไฟล์ใหม่ (Save)
normalized_audio.export(output_filename, format="wav")
print(f"\nบันทึกไฟล์ผลลัพธ์เรียบร้อยแล้วที่: {output_filename}")