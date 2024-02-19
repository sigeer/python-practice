import pytesseract
from PIL import Image, ImageEnhance, ImageGrab
import datetime

import re

# https://digi.bib.uni-mannheim.de/tesseract/ 处下载安装
pytesseract.pytesseract.tesseract_cmd = "D:\\Program Files\\Tesseract-OCR\\tesseract.exe"
print(pytesseract.pytesseract.get_languages())
# 打开图片
origin_image = Image.open(r"./zh.png")

if origin_image is None:
    print("图片不存在")
    exit()

# 调整亮度
enhancer = ImageEnhance.Brightness(origin_image)
enhanced_image = enhancer.enhance(1)  # 增加亮度的倍数

# 调整对比度（根据最后的图片调整）
enhancer = ImageEnhance.Contrast(enhanced_image)
enhanced_image = enhancer.enhance(2)  # 增加对比度的倍数

# 放大图片（图片过小识别效果较差）
width, height = enhanced_image.size
scale = 2
new_size = (width * scale, height * scale)
resized_image = enhanced_image.resize(new_size)

# 去除噪点（可选）
# 这里可以根据具体需要选择合适的去噪方法，例如中值滤波、高斯模糊等

# 保存最终调整后的图像参考
resized_image.save(f'./ocr_temp_{int(datetime.datetime.now().timestamp() * 1000)}.png')

# 使用 pytesseract 识别图片中的文字
text = pytesseract.image_to_string(resized_image, lang='chi_sim')

# 输出识别结果
print(text)



