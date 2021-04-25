import string
from PIL import Image, ImageFont, ImageDraw

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase

img_path_A = 'gen.A.png'
text_A_color = (0, 0, 0)
img_path_a = 'gen._a.png'
text_a_color = (254, 254, 254)
text_font = 'Robika.otf'
text_A_size = 30
text_a_size = 20

def addTextCenter(img_path, img_text, img_text_size, img_font, img_text_color, img_save):
    font = ImageFont.truetype(img_font, img_text_size)
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(img_text, font)
    draw.text(((img.width - w) / 2 + 2, (img.height - h) / 2), img_text, img_text_color,font=font)
    img.save(img_save)

for i in lowerCase:
    addTextCenter(img_path_a, i, text_a_size, text_font, text_a_color, '_' + i + '.png')

for i in upperCase:
    addTextCenter(img_path_A, i, text_A_size, text_font, text_A_color, i + '.png')
