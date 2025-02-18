from PIL import Image

def item_image_parser(x,y,filename,itemname):
    im = Image.open(filename)

    left = x
    top = y
    right = x + 40
    bottom = y + 40

    im1 = im.crop((left, top, right, bottom))
    im1.save(f"./itempics/{itemname}.png")
