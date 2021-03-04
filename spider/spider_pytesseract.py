# author:ToddCombs

import requests

# 导入图像识别模块tesseract-ocr
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

captcha = Image.open(r'1.webp')
result = pytesseract.image_to_string(captcha)
print(result)