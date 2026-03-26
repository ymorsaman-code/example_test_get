from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
from networkx import edges

path_name = "/Users/mac/Downloads/dog_mushroom.jpeg"
im = Image.open(path_name).convert('RGB')

gray_color = im.convert('L') # ปรับเป็น ภาพขาวดำ
im_EdgeDetection = gray_color.filter(ImageFilter.FIND_EDGES) # FIND_EDGES หาขอบของภาพ

im_EdgeDetection.save("edges.png") # save ภาพขอบที่ได้เป็นไฟล์ใหม่

#-----------------------------
# plt.subplot( row = 1, column =  2, position = 1) 
plt.subplot(1, 2, 1)        
plt.imshow(im)        # show รูปต้นฉบับ
plt.title("Original") # ตั้งชื่อรูป
plt.axis("off")       # default = "on" แสดงแกน x, y
#------------------------------
plt.subplot(1, 2, 2)
plt.imshow(im_EdgeDetection, cmap = "gray") #  cmap ="gray" แสดงภาพขาวดำ (ไม่ใส่ สีจะม่วงๆ เพี้ยนๆ  ดูยาก)
plt.title("Edge")
plt.axis("off")

plt.savefig("comparison.png")    # บันทึกภาพ Original กับ Edge
plt.show()                       # แสดงรูปทั้ง 2  Original กับ Edge