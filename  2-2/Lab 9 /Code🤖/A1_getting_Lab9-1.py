from collections import Counter
from pythainlp import word_tokenize

# 1. Input: รับข้อความ 1 ย่อหน้า (ตัวอย่างภาษาไทย ผสมอังกฤษ)
text = """
MacBook Neo เป็น Mac ที่ถูกสุดของ Apple โดยแลกกับการตัดสเปกและฟีเจอร์หลายอย่างจาก MacBook Air เพื่อให้ได้ราคาเริ่มต้น 19,900 บาท (นักศึกษา 16,900 บาท) โดยรวมยังเพียงพอสำหรับงานทั่วไปและการเรียน แต่ไม่เหมาะกับงานหนักด้านกราฟิก วดโอ หรือรันโมเดล AI แบบจริงจัง
สรุปแล้ว MacBook Neo ถูกวางให้เป็นเครื่องราคายอมเยา เหมาะสำหรับงานเอกสาร เรียนออนไลน์ ใช้แอปทั่วไปใน ecosystem ของ Apple หรือทำงานที่ iPhone/iPad ทำได้ แต่ไม่ใช่ตัวเลือกหลักสำหรับงาน 3D, กราฟิกระดับกลาง‑สูง, ตัดต่อวดีโอจริงจัง หรือรันโมเดล AI หนก ๆ
"""

# 2. Process: แยกคำและนับจำนวน
# ใช้ word_tokenize ตัดคำภาษาไทย (engine='newmm') และลบช่องว่าง
words = word_tokenize(text, engine = 'newmm', keep_whitespace = False)

# สร้าง List ว่างรอรับคำที่กรองแล้ว
cleaned_words = []            

# กำหนดสัญลักษณ์ที่ต้องการตัดทิ้งด้วยตัวเอง (Custom Punctuation)
not_words = ".,()/-"

for w in words:               
    
    # เช็คเงื่อนไข: (ตัดช่องว่างแล้วต้องมีตัวอักษร) และ (ต้องไม่ใช่เครื่องหมายวรรคตอน)
    if w.strip() and (w not in not_words):
        
        # ถ้าผ่านเงื่อนไข ให้แปลงเป็นตัวเล็ก แล้วเพิ่มลงใน List
        cleaned_words.append(w.lower())

word_counts = Counter(cleaned_words)

# 4. Output: แสดงผลลัพธ์
print(f"จำนวนคำทั้งหมด: {len(cleaned_words)} คำ")
print("\n 10 อันดับคำที่พบบ่อยที่สุด:")
print(f"{'คำศัพท์ (Word)'} {'จำนวน (Count)'}")
print("-" * 25)

# most_common(10) จะดึงข้อมูล 10 อันดับแรกที่พบบ่อยที่สุดมาแสดง
for word, count in word_counts.most_common(10):
    print(f"{word} = {count}")
