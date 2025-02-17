import urllib.request
from bs4 import BeautifulSoup

url = "https://www.realmeye.com/graveyard-of-player/Cupdog"

req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
page = urllib.request.urlopen( req )

html_bytes = page.read()
html = html_bytes.decode("utf-8")

table = html.split('<div class="table-responsive">')[1].split('</div>')[0]
tablebody = table.split('<tbody>')[1].split('</tbody>')[0]
deathlist = tablebody.split('<tr>')
soup = BeautifulSoup(table, "html.parser")
with open("table.html", "w") as file:
    file.write(str(soup.prettify()))
file.close()

death_list_dict = []
with open("deathlist.html", "w") as file:
    for death in deathlist:
        death_soup = BeautifulSoup(death, "html.parser")
        file.write(str(death_soup.prettify()))
        deathdate = death_soup.td
        print(deathdate)
file.close()
