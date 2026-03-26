# Lab 9-10
# โจทย์: รับไฟล์เสียง (.wav หรือ .mp3)

import urllib.request # ใช้สำหรับดาวน์โหลดไฟล์จาก URL

url = "https://github.com/karolpiczak/ESC-50/raw/master/audio/1-30226-A-0.wav"

sound_filename = "dog_barking.wav"

# 2. ขั้นตอนการดึงไฟล์แบบอัตโนมัติ (Automated Download)
print(f"กำลังดาวน์โหลดไฟล์จาก: {url}")
urllib.request.urlretrieve(url, sound_filename)
print("ดาวน์โหลดเสร็จสิ้น!")

#----------------------------------
# กำหนดชื่อไฟล์ที่เราดาวน์โหลดมาแล้ว
save_filename = "dog_barking.wav"

#-----------------------------------
import soundfile as sf
# ใช้ soundfile เพื่อดึงข้อมูลพื้นฐาน (Metadata)
audio_info = sf.info(save_filename)

#----------------------------------
# ดึงค่าต่างๆ ออกมาเก็บในตัวแปร
# ความยาวไฟล์ (วินาที)
duration = audio_info.duration    
     
#----------------------------------
# อัตราการสุ่มสัญญาณ (Hz)
sample_rate = audio_info.samplerate     

#----------------------------------
# จำนวนช่องสัญญาณ# จำนวนช่องสัญญาณ
channels = audio_info.channels         

#----------------------------------
# สร้างเงื่อนไขตรวจสอบว่าเป็น Mono หรือ Stereo เพื่อให้ผลลัพธ์อ่านง่ายขึ้น
if channels == 1:                       # ถ้าเป็น Mono จะมีช่องสัญญาณ = เดียว
    channel_type = "Mono"
elif channels == 2:
    channel_type = "Stereo"             # ถ้าเป็น Stereo จะมีช่องสัญญาณ = สองช่อง
else:
    channel_type = "Multi-channel"      # กรณีที่มีมากกว่า 2 ช่อง (เช่น 5.1 Surround Sound) จะถือเป็น Multi-channel

#----------------------------------
# 5. พิมพ์สรุป
print(f"ความยาว: {duration:.2f} วินาที")
print(f"Sample rate: {sample_rate} Hz")
print(f"จำนวนช่องสัญญาณ: {channels} ({channel_type})")