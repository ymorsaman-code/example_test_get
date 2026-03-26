from rembg import remove
from PIL import Image
input_path = "/Users/mac/Downloads/dog_mushroom_blurred.jpeg"
output_path = "/Users/mac/Downloads/dog_mushroom_no_bg.png"
input_img = Image.open(input_path)
output = remove(input_img)
output.save(output_path)