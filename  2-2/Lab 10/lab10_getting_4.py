import pytesseract
from PIL import Image

# version ที่เร็วกว่า
# https://github.com/UB-Mannheim/tesseract/wiki 

# pytesseract.pytesseract.tesseract_cmd = "/Users/mac/Downloads/tesseract-ocr-w64-setup-5.5.0.20241111.exe"
# pytesseract.pytesseract.tesseract_cmd = "/Users/mac/Downloads/tesseract-ocr-w64-setup-5.5.0.20241111.exe"

# สำหรับ macOS ให้ใช้ path นี้แทน (หลังจากสั่ง brew install tesseract แล้ว)
# หมายเหตุ: ถ้าใช้ Mac รุ่นเก่า (Intel) อาจต้องเปลี่ยนเป็น /usr/local/bin/tesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

img = Image.open("/Users/mac/Desktop/image_ocr.jpg")
text = pytesseract.image_to_string(img)
print(text)