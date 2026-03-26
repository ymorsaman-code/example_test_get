# regular expression จัดการข้อความตามรูปแบบ
import re 
from pythainlp.util import normalize

text = "Macbook neo!!!    เครื่อง    รุ่นใหม่    ในปี  2026"

print(f" Before = {text}")

# แปลงเป็น lowercase (ตัวพิมพ์เล็ก) จะมีผลแค่กับภาษาอังกฤษ
text = text.lower()

# ลบอีโมจิ/อักขระพิเศษด้วย regex (ต้องใช้ double backslash \\)
# [^\\w\\s] หมายถึง ทุกอย่างที่ไม่ใช่ตัวอักษร ตัวเลข และช่องว่าง
# ^ = ตัวปฏิเสธ หมายถึง "ไม่เอา" หรือ "ยกเว้น" สิ่งที่ตามหลังมา
# \\w  = แทนตัวอักษร (ก-ฮ, A-Z, a-z), ตัวเลข (0-9) และเครื่องหมายขีดล่าง (underscore _) ใน Python 3 และไลบรารี re
# \\s  = Space Character (ช่องว่าง)

#    = re.sub('สิ่งที่ต้องการค้นหา หรือจะลบ', 'สิ่งที่จะแทนที่', ข้อความต้นฉบับ)
text = re.sub('[^, \\w, \\s]', '', text)

# normalize ลบสระที่พิมพ์ซ้ำซ้อน
text = normalize(text)

print(f" After = {text}")
