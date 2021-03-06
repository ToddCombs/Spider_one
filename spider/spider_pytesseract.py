# author:ToddCombs
# 导入图像识别模块tesseract-ocr
from pygments.formatters import img
import PIL
from PIL import Image
# try:
#     from PIL import Image
# except ImportError:
#     import Image
import pytesseract

# captcha = Image.open('static/1.png')  # 第一张验证码不用处理，很容易就识别出来了
captcha = Image.open('static/2.png')  # 第二张图片需要处理下灰度和二值化
result = pytesseract.image_to_string(captcha)
print(result)  # 不做处理的图片识别为19024
# 所以对原图片灰度处理一下，否则数据识别不准
result = captcha.convert('L')
result.show()
# 对图片继续进行二值化

def convert_img(img, threshold):
    """对图片继续进行二值化"""
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img
# 输出结果看下，发现图片已经变白底黑字了。
captcha = convert_img(captcha, 150)
captcha.show()
print(captcha)
result = pytesseract.image_to_string(captcha)
print(result)
#
# data = img.getdata()
#
#     w, h = img.size
#     count = 0
#     for x in range(1, h-1):
#         for y in range(1, h-1):
#             # 找出各个像素方向
#             mid_pixel = data[x * y + x]
#             if mid_pixel == 0:
#                 top_pixel = data[w * (y - 1) + x]
#                 left_pixel = data[w * y + (x - 1)]
#                 down_pixel = data[w * (y + 1) + x]
#                 right_pixel = data[w * y + (x + 1)]
#
#                 if top_pixel == 0:
#                     count += 1
#                 if left_pixel == 0:
#                     count += 1
#                 if down_pixel == 0:
#                     count += 1
#                 if right_pixel == 0:
#                     count += 1
#                 if count > 4:
#                     img.putpixel((x, y), 0)