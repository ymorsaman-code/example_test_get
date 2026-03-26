from PIL import Image
import math

path_name = "/Users/mac/Downloads/dog_mushroom.jpeg"
im = Image.open(path_name).convert('RGB')
w, h = im.size

gray = Image.new('L', (w, h))

total = 0


for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i, j))
        c = (r + g + b) // 3
        gray.putpixel((i, j), c)
        total += c


N = w * h
mean = total / N


sum_sq = 0
for i in range(w):
    for j in range(h):
        val = gray.getpixel((i, j))
        sum_sq += (val - mean) ** 2

std = math.sqrt(sum_sq / N)


gray.show()
gray.save('Imageb_gray.jpg')
print("Mean =", mean)
print("Std =", std)
