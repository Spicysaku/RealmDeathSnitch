import urllib.request
from bs4 import BeautifulSoup
import Realm_image_parser as RIP

def guild_graveyard(guild_name:str, death_index:int) -> dict:
    guild_name = guild_name.replace(" ", "%20")

    # Realmeye graveyard url
    url = f"https://www.realmeye.com/recent-deaths-in-guild/{guild_name}"

    # Open the url
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urllib.request.urlopen(req)

    # Read the html
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    # Debugging
    # with open("page.html", "w", encoding="utf-8") as file:
    #     soup = BeautifulSoup(html, "html.parser")
    #     file.write(str(soup.prettify()))

    # Find the table
    table = html.split('<div class="table-responsive">')[1].split('</div>')[0]
    tablebody = table.split('<tbody>')[1].split('</tbody>')[0]
    deathlist = tablebody.split('<tr>')[1:]

    # Parse the table
    death = deathlist[death_index]
    # Parse the death data
    death_soup = BeautifulSoup(death, "html.parser")
    td_list = death_soup.find_all('td')

    # Parse the equipment on dead character
    equipment_soup = BeautifulSoup(str(td_list[5]), "html.parser")

    # Debugging Part 3
    with open("death.html", "w") as file:
        file.write(str(death_soup.prettify()))
    file.close()

    # Unparsed list of equipment on dead character
    equipment_soup_list = equipment_soup.find_all('a')

    # Initialize a list for the parsed equipment
    equipment_array = []
    # Loop through the equipment and parse it
    for equipment in equipment_soup_list:
        name = str(equipment).split('title="')[1].split('">')[0]
        if '\n' in name:
            name = name.split('\n')[0]
        x_y_coords = str(equipment).split('background-position:')[1].split('" title')[0]
        x = abs(int(x_y_coords.split('px ')[0]))
        y = abs(int(x_y_coords.split('px ')[1].split('px')[0]))

        # An equipment has a name, x and y coordinates
        equipment_dict = {
            'name': name,
            'x': x,
            'y': y
        }

        # Append the equipment to the equipment array
        equipment_array.append(equipment_dict)

    #Parse skin data
    skin_x_y = str(td_list[0]).split('background-position:')[1].split('">')[0]
    x = abs(int(skin_x_y.split('px ')[0]))
    y = abs(int(skin_x_y.split('px ')[1].split('px')[0]))
    skin_loc = {'x': x, 'y': y}

    # Combine all the data into a dictionary
    death_dict = {
        "skindata": skin_loc,
        "player-name": td_list[1].text,
        "time": td_list[2].text,
        "base_fame": td_list[3].text,
        "total_fame": td_list[4].text,
        "equipment": equipment_array,
        "stats": td_list[6].text,
        "killed_by": td_list[7].text
    }

    x = death_dict["skindata"]['x']
    y = death_dict["skindata"]['y']
    RIP.skin_image_parser(x, y, death_dict["player-name"])
    for item in death_dict["equipment"]:
        RIP.item_image_parser(item["x"],item["y"],item["name"])

    return death_dict
