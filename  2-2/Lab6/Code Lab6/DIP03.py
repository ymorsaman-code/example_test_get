from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

lisa_img = Image.open('/Users/mac/Downloads/Lisa_Lab6.jpg')

# ------------------------
# หา (Min, Max, Mean) ของแต่ละสี
'''
ranges = [
    (0, 256, 'Red'),     # สีแดง: index 0 ถึง 255
    (256, 512, 'Green'), # สีเขียว: index 256 ถึง 511
    (512, 768, 'Blue')   # สีน้ำเงิน: index 512 ถึง 767
]
'''
# แบบนี้ง่ายกว่า
img_arr = np.array(lisa_img) 

colors_name = ['Red', 'Green', 'Blue']

print("--- ผลลัพธ์การคำนวณค่าสี ---")
for i in range(3):
    
    # [ความสูง, ความกว้าง, ชั้นสี]
    channel_data = img_arr[:, :, i] # : เอาทั้งหมด , i คือ index ของสี
    mn = channel_data.min()
    mx = channel_data.max()
    avg = channel_data.mean()
    print(f"สี {colors_name[i]}: Min={mn}, Max={mx}, Mean={avg}")

# ------------------------
# การวาดกราฟ Histogram
# ใช้คำสั่ง histogram() จะได้ list ยาวๆ รวมทุกสีมา
c = lisa_img.histogram()

nr = [] # ลิสต์เก็บกราฟสีแดง
ng = [] # ลิสต์เก็บกราฟสีเขียว
nb = [] # ลิสต์เก็บกราฟสีน้ำเงิน

# วนลูปแยกสีตามวิธีของอาจารย์ (Manual Loop)
for i in range(256):
    nr.append(c[i])        # ช่วง 0-255 คือสีแดง
    ng.append(c[i + 256])  # ช่วง 256-511 คือสีเขียว
    nb.append(c[i + 512])  # ช่วง 512-767 คือสีน้ำเงิน

# ตั้งค่ากราฟ
# _mpl-gallery แกน y เป็น 0 หมดเลย
plt.style.use("ggplot")      # style กราฟ ชื่อ ggplot ดีกว่า
plt.xlabel("color value (0-255)")  # ตั้งชื่อแกน x
plt.ylabel("pixel counts")         # ตั้งชื่อแกน y

# พล็อตเส้นกราฟแยกสี
plt.plot(range(256), nr, color='red', label = 'Red')        # label = บอกชื่อเส้นกราฟ
plt.plot(range(256), ng, color='green', label = 'Green')
plt.plot(range(256), nb, color='blue', label = 'Blue')

plt.legend()
plt.show()