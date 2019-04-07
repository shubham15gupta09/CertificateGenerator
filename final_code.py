from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate(name):
    img = Image.open("final ashwini.png")
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("comics.ttf", size=25)
    draw.text((430,360), name , font=selectFont, fill=(105, 105, 105))
    img.save(name + ".png")
fin = open("new.txt.txt",'r')
for i in fin:
    i=i.replace("\n","")
    generate(i)
fin.close()
