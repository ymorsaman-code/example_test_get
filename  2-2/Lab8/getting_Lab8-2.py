from datetime import datetime as dt
from gtts import gTTS
import os

# 1. รับชื่อและดึงเวลา
name = input("ป้อนชื่อ: ")
n = dt.now()

# 2. เตรียมข้อมูลวันเดือน (เขียนแบบย่อบรรทัดเดียว)
mons = "มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม".split()
days = "จันทร์ อังคาร พุธ พฤหัสบดี ศุกร์ เสาร์ อาทิตย์".split()

# 3. สร้างข้อความ (f-string)
text = f"สวัสดีคุณ{name} วันนี้วัน{days[n.weekday()]}ที่ {n.day} {mons[n.month-1]} ปีพุทธศักราช {n.year+543} ขณะนี้เวลา {n.hour} นาฬิกา {n.minute} นาที วันนี้เป็นวันครบรอบวันเกิดของคุณ ขอให้คุณมีความสุขมากๆนะครับ"

# 4. สร้างเสียง, บันทึก และเล่นไฟล์
print(text)
gTTS(text, lang='th').save("hbd.mp3")
os.system("start hbd.mp3" if os.name == "nt" else "open hbd.mp3")