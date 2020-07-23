from PIL import Image, ImageDraw, ImageFont
     
img = Image.new('RGB', (1280, 720), color = ("#008099"))
fnt = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 72)
with open('../title.txt','r') as f:
    text = f.read()

d = ImageDraw.Draw(img)
d.text((50,200), text=text, font=fnt, fill=(255, 255, 255))
     
img.save('thumbnail.png')
