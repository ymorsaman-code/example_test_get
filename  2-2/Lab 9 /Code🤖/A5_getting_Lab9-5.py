import os 
from collections import defaultdict , Counter 
from pythainlp import word_tokenize

# os --> การขออนุญาตใช้ "เครื่องมือจัดการไฟล์และโฟลเดอร์" ของระบบคอมพิวเตอร์ (Operating System)
# defaultdict --> กำหนดค่าเริ่มต้นให้เองอัตโนมัติ" เมื่อเราพยายามเข้าถึง Key ที่ยังไม่มีอยู่ในระบบ
# Counter --> การนับจำนวนของสิ่งต่างๆ
# word_tokenize --> การตัดคำ

butterbear_folder = "/Users/mac/Downloads/butterbear_story"

# ทำให้คุณสามารถเขียนโค้ดบรรทัดเดียวสั้นๆ เพื่อสั่งนับเลขได้ทันที โดยไม่ต้องเขียน if เพื่อเช็คว่ามีคำนี้หรือมีไฟล์นี้อยู่ในระบบหรือยัง
word_data = defaultdict(lambda: defaultdict(int)) 

# 1. อ่านไฟล์และสร้างดัชนี
for filename in os.listdir(butterbear_folder):      # os.listdir() : การขอรายชื่อไฟล์และโฟลเดอร์
   
   # os.path.join() : การรวม path ของไฟล์และโฟลเดอร์
   # e.g. 
   # Input 1: /Users/mac/Downloads/butterbear_story
   # Input 2: butterbear_1.txt
   # ผลลัพธ์ที่ได้ : /Users/mac/Downloads/butterbear_story/butterbear_1.txt
   # เข้าถึงแต่ละไฟล์ ใน  folder ได้
   file_path = os.path.join(butterbear_folder, filename)

   text = open(file_path, encoding="utf-8").read()  # อ่านไฟล์
   word_split = word_tokenize(text, engine="newmm") # ตัดคำ
    
   # เช็คว่าเป็นไฟล์ 
   # word_cuted เป็นตัวแทน คำที่ตัดแล้ว ใน word_split
   for word_cuted in word_split:
        if word_cuted.strip(): # เช็คว่าไม่ใช่ช่องว่าง เพราะบางทีตัดคำ มีช่องว่าง ทำการตัดช่องว่าง " หมีเนย " --> "หมีเนย" 
            word_data[word_cuted][filename] += 1  
                     #   ["หมี"] ["butterbear_1.txt"] ถ้าเจอคำว่า หมี ในไฟล์ butterbear_1.txt แล้วให้ + 1 ครั้งที่พบ

# 2. ค้นหา
search = input("search word --> ")
if search in word_data:
    
    # Counter(word_data[search]) : การนับจำนวนของคำที่ค้นหา
    # .most_common() : การเรียงลำดับจากมากไปน้อย
    total_count = Counter(word_data[search]).most_common()

    for file, count in total_count:
        print(f"-> {file} เจอ {count} ครั้ง")
else:
    print("ไม่พบคำนี้ เอาแค่คำเดียวนะครับคุณพี่!!!!!")
