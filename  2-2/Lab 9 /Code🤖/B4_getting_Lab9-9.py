from PIL import Image, ImageFilter

# โหลดภาพ (จากโค้ดของคุณ)
path_name = "/Users/mac/Downloads/dog_mushroom.jpeg"
im = Image.open(path_name).convert('RGB')

# กำหนดพิกัด Bounding Box (x1, y1, x2, y2) หรือ (ซ้าย, บน, ขวา, ล่าง)
box_coords = (250, 350, 450, 540) 

# ระบุและตัดพื้นที่เป้าหมาย 
roi_img = im.crop(box_coords)

# ประมวลผลทำภาพเบลอ 
# รัศมี (radius=15) ควบคุมความเบลอ ยิ่งตัวเลขสูง ภาพในกรอบก็จะยิ่งเบลอมาก
blurred_roi = roi_img.filter(ImageFilter.GaussianBlur(radius=15))

# รวมผลลัพธ์
im.paste(blurred_roi, box_coords)

# เปิดดูภาพ
output_path = "dog_mushroom_blurred.jpeg"
im.save(output_path)
im.show() 