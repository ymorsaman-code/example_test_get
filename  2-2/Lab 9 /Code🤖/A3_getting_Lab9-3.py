from pythainlp import word_tokenize, sent_tokenize

# Input (รับข้อความจากผู้ใช้) 
text = input(" Input (คั่นด้วย . ? !) --> ")

# Sentence Splitting (แยกประโยค) 
sentences = sent_tokenize(text.strip(), engine="whitespace+newline")

# Word Tokenization (ตัดคำเป็นภาษาไทย) 
sentences_words = [word_tokenize(s, engine="newmm") for s in sentences]  # จำเป็นต้องเป็น for loop เพราะ sentences เป็นลิสต์

# คำนวณจำนวนประโยค
num_sentences = len(sentences_words)    

# หาประโยคที่ยาวที่สุด
longest_list = max(sentences_words, key = len)

# คำนวณค่าเฉลี่ย (รวมจำนวนคำทุกประโยค / จำนวนประโยค)
avg_words = sum(len(words) for words in sentences_words) / num_sentences 

# คำนวณจำนวนคำในประโยคที่ยาวที่สุด
longest_words = len(longest_list)

# text to test --> MacBook Neo เปิดตัวแล้ว. ราคาประหยัดมาก! ดีไซน์สวยและพกพาสะดวก.


print(f"1. จำนวนประโยคทั้งหมด: {num_sentences}")
print(f"2. ค่าเฉลี่ยจำนวนคำต่อประโยค: {avg_words:.2f}")
print(f"3. ประโยคที่ยาวที่สุด: '{''.join(longest_list)}'") # ''.join เพราะ longest_list เป็นลิสต์ ต้องต้องใช้เพื่อเชื่อคำที่แยกๆกันอยู่
print(f"   (มีความยาว {longest_words} คำ)")
