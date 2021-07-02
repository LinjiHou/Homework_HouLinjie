"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""
from PIL import Image, ImageDraw, ImageFont


font_path=r"C:\Windows\Fonts\Agency FB\AGENCYR.TTF"
image_path=r"F:\file_py\Homework_HouLinjie\picture\\"
image_without_number="P1_original.jpg"
image_with_number="P1_finished.jpg"

image=Image.open(image_path+image_without_number,'r')

w,h=image.size

font = ImageFont.truetype(font_path, int(h/4))

ImageDraw.Draw(image).pieslice([((w/3)*2,0),(w,h/3)], 0,360, fill = 'white')
ImageDraw.Draw(image).text((w*0.73,h*0.02), '03', font = font, fill = 'red')

# image.show()
image.save(image_path + image_with_number)

