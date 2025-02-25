from PIL import Image
import os
import shutil

def item_image_parser(x,y,itemname):
    im = Image.open("./images/renders.png")

    left = x
    top = y
    right = x + 40
    bottom = y + 40

    im1 = im.crop((left, top, right, bottom))
    os.makedirs("./itempics", exist_ok=True)
    im1.save(f"./itempics/{itemname}.png")

def skin_image_parser(x,y,playername):
    im = Image.open("./images/sheets.png")

    left = x
    top = y - 250
    right = x + 50
    bottom = y - 200

    im1 = im.crop((left, top, right, bottom))
    os.makedirs("./skinpics", exist_ok=True)
    im1.save(f"./skinpics/{playername}.png")

def image_combiner(death_dict:dict) -> str:
    template = Image.open("./images/image-template.png")
    skin = Image.open(f"./skinpics/{death_dict['player-name']}.png")
    item_1 = Image.open(f"./itempics/{death_dict['equipment'][0]['name']}.png")
    item_2 = Image.open(f"./itempics/{death_dict['equipment'][1]['name']}.png")
    item_3 = Image.open(f"./itempics/{death_dict['equipment'][2]['name']}.png")
    item_4 = Image.open(f"./itempics/{death_dict['equipment'][3]['name']}.png")
    combined = Image.new('RGBA', (template.width, template.height), (0, 0, 0, 0))
    combined.paste(template, (0, 0), template)
    combined.paste(skin, (6, 7), skin)
    combined.paste(item_1, (60, 12), item_1)
    combined.paste(item_2, (105, 12), item_2)
    combined.paste(item_3, (149, 12), item_3)
    combined.paste(item_4, (193, 12), item_4)
    combined.resize((combined.width * 2, combined.height * 2))
    combined.save("./images/output.png")



def delete_all_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
