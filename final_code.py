from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate(name):
    img = Image.open("CertificateTemplate.png")     #template
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("comics.ttf", size=25)   #font selection
    draw.text((430,360), name , font=selectFont, fill=(105, 105, 105))
    img.save(name + ".png")        #certificate will be saved with the name of attendee
fin = open("new.txt",'r')   #txt file containing the names of the attendee
for i in fin:
    i=i.replace("\n","")
    generate(i)
fin.close()
