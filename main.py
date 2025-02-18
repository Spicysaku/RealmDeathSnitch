import urllib.request
from bs4 import BeautifulSoup

# Realmeye graveyard url
url = "https://www.realmeye.com/graveyard-of-player/Spncerfrez"

# Open the url
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
page = urllib.request.urlopen(req)

# Read the html
html_bytes = page.read()
html = html_bytes.decode("utf-8")

with open("page.html", "w", encoding="utf-8") as file:
    soup = BeautifulSoup(html, "html.parser")
    file.write(str(soup.prettify()))

# Get dead character sprites
# SEEMS IMPOSSIBLE PLS HELP

# Find the table
table = html.split('<div class="table-responsive">')[1].split('</div>')[0]
tablebody = table.split('<tbody>')[1].split('</tbody>')[0]
deathlist = tablebody.split('<tr>')[1:]

#soup = BeautifulSoup(table, "html.parser")
# with open("table.html", "w") as file:
#     file.write(str(soup.prettify()))
# file.close()

death_list_dict = []
for death in deathlist:
    death_soup = BeautifulSoup(death, "html.parser")
    td_list = death_soup.find_all('td')
    death_dict = {
        "time": td_list[0].text,
        #"skindata": td_list[1].text,
        "classname": td_list[2].text,
        "level": td_list[3].text,
        "base_fame": td_list[4].text,
        "total_fame": td_list[5].text,
        "exp": td_list[6].text,
        #"equipment": td_list[7].text,
        "stats": td_list[8].text,
        "killed_by": td_list[9].text
    }
    death_list_dict.append(death_dict)

print(str(death_list_dict[0]))