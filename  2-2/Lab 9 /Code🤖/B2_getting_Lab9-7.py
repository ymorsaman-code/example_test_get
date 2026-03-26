from PIL import Image


input_path = "input.jpg"        # ชื่อไฟล์รูปต้นฉบับ
output_path = "newSize_512.jpg" # ชื่อไฟล์ที่ต้องการเซฟ
resize = 512                    # ความกว้างที่กำหนด ใหม่

path_name = "/Users/mac/Downloads/dog_mushroom.jpeg"

# 1. รับภาพ
img = Image.open(path_name)
old_width, old_height = img.size

# โชว์รูปต้นฉบับ
print("เปิดรูปต้นฉบับ Old Image")
img.show()

# 2. คำนวณสัดส่วนความสูงใหม่ เพื่อรักษาอัตราส่วนเดิม
ratio = resize / old_width
new_height = int(old_height * ratio)

# 3. ปรับขนาดภาพ
new_img = img.resize((resize, new_height))

# โชว์รูปที่ปรับขนาดแล้ว
print("เปิดรูปที่ปรับขนาดแล้ว New Image")
new_img.show()

# 4. เซฟเป็นไฟล์ใหม่
new_img.save(output_path)

# 5. แสดงผลลัพธ์ขนาดก่อน/หลัง
print(f"ขนาดก่อนทำ : {old_width} x {old_height} px")
print(f"ขนาดหลังทำ : {resize} x {new_height} px")
print("บันทึกไฟล์สำเร็จ!")