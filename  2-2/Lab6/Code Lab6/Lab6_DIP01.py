from PIL import Image
lisa_img = Image.open('/Users/mac/Downloads/Lisa_Lab6.jpg')

# version หลายๆ รูป
#--------------
w, h = lisa_img.size
filename = 'Image1 - '

for i in range(10, 76) :
    per = i
    dec = 100 - per
    new_W = int(w * dec / 100)
    
    new_H = int(h * dec / 100)
    
    print( per, w , h, new_W, new_H)
    print(f"percent = {per}%, ขนาดเดิม = {w} x {h}, ขนาดใหม่ = {new_W} x {new_H}")
    
    lisa_resize = lisa_img.resize((new_W, new_H))
    lisa_resize.save(filename + str(i) + '.jpg')
    
    print("สร้างครบ 10 -> 75 % เรียบร้อยแล้ว")