from PIL import Image
import os

def item_image_parser(x,y,itemname):
    im = Image.open("renders.png")

    left = x
    top = y
    right = x + 40
    bottom = y + 40

    im1 = im.crop((left, top, right, bottom))
    os.makedirs("./itempics", exist_ok=True)
    im1.save(f"./itempics/{itemname}.png")

def skin_image_parser(x,y,itemname):
    im = Image.open("./images/sheets.png")

    left = x
    top = y - 250
    right = x + 50
    bottom = y - 200

    im1 = im.crop((left, top, right, bottom))
    os.makedirs("./skinpics", exist_ok=True)
    im1.save(f"./skinpics/{itemname}.png")

skin_image_parser(2850, 550,"Test")
