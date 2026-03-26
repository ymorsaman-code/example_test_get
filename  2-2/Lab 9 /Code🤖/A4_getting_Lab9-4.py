from pythainlp.tokenize import word_tokenize
from pythainlp.corpus.common import thai_words
from pythainlp.util import dict_trie

wrong_word = {"ฟรี", "ด่วน", "คลิก", "โปรโมชั่น", "เงินคืน", "รับทันที"}
text_input = input(" Input text --> ")

# 1. สร้าง set คำศัพท์ใหม่ขึ้นมา 
custom_dict_spam = set(thai_words())
custom_dict_spam.update(wrong_word)  # เติมคำสแปมลงไปใน set

# 2. ต้องเรียก dict_trie(...) แปลง set เป็น trie ก่อนส่งให้ตัดคำเสมอ เพื่อไมให้คำ เช่น โปรโมชั่น --> โปร โม ชั่น
trie = dict_trie(dict_source = custom_dict_spam)

# 3. ส่ง trie ให้ custom_dict เพื่อให้คำ ที่ต้องการไม่ถูกตัดคำ
words = word_tokenize(text_input, engine="newmm", custom_dict=trie)

# เงินคืน --> ['เงินคืน']
# print(words)
#---------------------------------------------------------------------------------------
# คิดคะแนน
# k --> ตัวแทน นับคำที่มีความน่าสงสัย ที่กำหนดไว้ใน wrong_word ว่ามีกี่คำ 
# words.count(k) นับคำจากจำนวน k ทีี่ได้จากการ  for k in wrong_word loop
# คูณ 2 --> มีคำหน้าสมสัยกี่คำ ก็เพิ่ม + 2 คะแนนในแต่ละคำ    
# sum() --> รวมผลรวมทั้งหมด จากการนับ คะแนน
score = sum(words.count(k) * 2 for k in wrong_word)

# ตรวจว่ามี http หรือ https หรือไม่
# ถ้ามี http:// หรือ https:// ให้เพิ่ม + 3 คะแนน
if "http://" in text_input or "https://" in text_input:
    score += 3

# ตรวจว่ามีตัวอักษรซ้ำ 5 ตัวรึป่าว
# character --> ตัวอักษร
# set() --> จัดการข้อมูล ให้ไม่ซ้ำกัน เป็น built-in function python
# set(text_input) --> ตัวอักษรที่ไม่ซ้ำกัน
for character in set(text_input):
    if character * 5 in text_input:  # แต่ถ้ามีตัวอักษรซ้ำ 5 ตัว ใน text_input 
        score += 2   # เพิ่ม + 2 คะแนนถ้ามีตัวอักษรซ้ำ 5 ตัว
        break        # หยุดการวนลูปทันที ไม่ต้องไปเช็คตัวอื่นต่อ และป้องกันไม่ให้คะแนนบวกเพิ่มซ้ำซ้อน

# กำหนดระดับ
# 

# index --> [0 ปกติ, 1 น่าสงสัย, 2 สแปม]

# e.g. 
# score = 2 
# ถ้า score >= 2 เป็น TRUE = 1
# ถ้า score >= 4 เป็น TRUE = 0
# Total = 1 + 0 = 1 index = 1
# --> index = 1 --> level = "น่าสงสัย"
level = ["ปกติ", "น่าสงสัย", "สแปม"][(score >= 2) + (score >= 4)]
print(f"ผลลัพธ์ : สรุปคะแนน {score} ระดับ ({level})")
