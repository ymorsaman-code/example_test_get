from PIL import Image, ImageOps, ImageChops

# เรียกภาพมาใช้
path = "/Users/mac/Downloads/WatWaAram.jpg" 
wat_img = Image.open(path).convert("RGB") #เผื่อรูปอื่นไม่ใช่ RGB mode
width, height = wat_img.size

#------------------------------
# แยก ช่องสี ออกมาเตรียมใช้
r, g, b = wat_img.split() # ครั้งต่อไป ต้องใส่ .convert("RGB") จะได้รวมทั้ง 3 ช่องสี กลับมาเป็นภาพสีปกติ


#------------------------------
# สร้างภาพทั้ง 9 แบบ

# 1. Gray Scale with Red , ใช้ ช่องสี Red อย่างเดียว
img_1 = r.convert("RGB")

# 2. Gray Scale with Green , ใช้ ช่องสี Green อย่างเดียว
img_2 = g.convert("RGB")

# 3. Gray Scale with Blue , ใช้ ช่องสี Blue อย่างเดียว
img_3 = b.convert("RGB")

# 4. Gray Scale with Max (ค่ามากสุดระหว่าง R, G, B)
# ImageChops = คำนวณค่าสีภาพ
#  .lighter  = เปรียบเทียบหาค่าที่สว่างกว่า (Max)
max_rg = ImageChops.lighter(r, g)    # ที่ใส่่ 2 ช่องสี เพราะ ลองใส่ 3 ช่อง มัน error น่าจะเป็นเพราะฟังก์ชันรับแค่ 2 ช่องสี --> เลือก r, g ก่อน เพราะเรียงจำง่ายดี
img_4 = ImageChops.lighter(max_rg, b).convert("RGB") #เอาสองสีที่สู้กันแล้วว่าใครสว่างกว่ามาสู้กับอีกสี  blue อีกที --> ได้ค่าสีที่สว่างที่สุด = img_4

# 5. Gray Scale with Min (ค่าน้อยสุดระหว่าง R, G, B)
# ImageChops = คำนวณค่าสีภาพ
#  .darker  = เปรียบเทียบหาค่าที่มืดกว่า หรือ สว่างน้อยสุด (Min)
min_rg = ImageChops.darker(r, g)    # ที่ใส่่ 2 ช่องสี เพราะ ลองใส่ 3 ช่อง มัน error น่าจะเป็นเพราะฟังก์ชันรับแค่ 2 ช่องสี --> เลือก r, g ก่อน เพราะเรียงจำง่ายดี
img_5 = ImageChops.darker(min_rg, b).convert("RGB") #เอาสองสีที่สู้กันแล้วว่าใครมืดกว่ามาสู้กับอีกสี  blue อีกที --> ได้ค่าสีที่มืดที่สุด = img_5

# 6. Gray Scale with Mean (ค่าเฉลี่ย)
# ใช้ .convert("L") คือสูตรมาตรฐานที่โปรแกรมทั่วโลกใช้ทำภาพขาวดำ , มีใน slide อาจารย์
img_6 = wat_img.convert("L").convert("RGB")

# 7. Black/White 
# dither = Image.NONE คือ สั่งห้ามกระจายเม็ดสี ให้ตัดฉับเลย , ก่อนไม่ใส่ เป็นเม็ดๆ 
img_7 = wat_img.convert("1", dither = Image.NONE).convert("RGB")

# 8. Sepia Color
# ใช้ colorize ย้อมแสงเงา (ดำ -> น้ำตาลเข้ม, ขาว -> ครีมเหลือง)
img_8 = ImageOps.colorize(wat_img.convert("L"), black="#704214", white="#C0C090").convert("RGB")

# 9. Cyanotype Color (โทนพิมพ์เขียว)
# ย้อมแสงเงา (ดำ->น้ำเงินเข้ม, ขาว->ขาว)
img_9 = ImageOps.colorize(wat_img.convert("L"), black="#00008B", white="#FFFFFF").convert("RGB")


#------------------------------
# รวมภาพทั้ง 9 ใส่ List
all_images = [img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8, img_9]

#------------------------------
'''
# แบบใช้ count 
count = 0  # ต้องสร้างตัวแปรเพิ่ม
for img in all_images:
    strip_img.paste(img, (count * width, 0))
    count = count + 1  # ต้องจำไว้ว่าต้องบวกเองนะ ห้ามลืม!
'''
# แบบใหม่ ใช้ enumerate() สร้างตัวนับให้อัตโนมัติ ง่ายดี
# ข้อ 2.1 ต่อกันเป็นแถวยาวเพียงแถวเดียว (Strip)
# Image.new = สร้างภาพเปล่าใหม่
strip_img = Image.new('RGB', (width * 9, height)) # สร้างพื้นหลังสำหรับใส่รูป กว้าง = 9 เท่าของภาพเดิม , สูง = เท่าภาพเดิม เพราะ ต่อเป็นแถวเดียว
for i, img in enumerate(all_images):              # สร้างตัวนับ i ให้อัตโนมัติ
    strip_img.paste(img, (i * width, 0))          # วางภาพที่ตำแหน่ง (i * width, 0) --> แกน x = i*width , แกน y = 0 เพราะจะเอาแค่แนวนอน
            # PIL (image, ( position เท่านั้น ))
    
strip_img.save("WatWaAram21.jpg")
print(" WatWaAram21 บันทึกภาพ 2.1 (แถวยาว) เรียบร้อยแล้ว")

#------------------------------
# ข้อ 2.2 เรียงเป็น ตาราง 3x3 
# column = 3 , row = 3
# สร้างพื้นหลังสำหรับใส่รูป กว้าง = 3 เท่าของภาพเดิม , สูง = 3 เท่าของภาพเดิม เพราะ ต่อเป็นตาราง 3x3
grid_img = Image.new('RGB', (width * 3, height * 3)) 

for i, img in enumerate(all_images):
    # คำนวณ column, row 
    # i เริ่มจาก 0 ถึง 8
    # // หารไม่เอาเศษ เอาแค่จำนวนเต็ม
    # % หารเอาเศษ
    
    col = i % 3             # i = 3 (3 % 3 = 0) --> คอลัมน์ที่ 0
    row = i // 3            # i = 3 (3 // 3 = 1) --> จะตั้ง แถวใหม่
    grid_img.paste(img, (col * width, row * height))
          # PIL (image,  ( position เท่านั้น ))
          # col * width = แกน x
          # row * height = แกน y

grid_img.save("WatWaAram22.jpg")
print(" WatWaAram22 บันทึกภาพ 2.2 (ตาราง 3x3) เรียบร้อยแล้ว")

print("พร้อมส่งจาร โอ้ตแล้ว")

