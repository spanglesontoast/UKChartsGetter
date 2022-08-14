import requests
from bs4 import BeautifulSoup
import urllib.request
from youtubesearchpython import VideosSearch
f = open('currentcharts', 'w', encoding="utf-8")
URL = "https://www.officialcharts.com/charts/singles-chart/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

ctitle = ""
tables = soup.find_all('div', class_="track")

for song in tables:
    titles =  song.find_all("div", {"class": "title"})
    artists =  song.find_all("div", {"class": "artist"})
    
    for title in titles:
        #print(title.text.strip())
        ctitle = title.text.strip()
    for artist in artists:
        ctitle += " - " + artist.text.strip()
        f.write(ctitle + "\n")
        print(ctitle)

#positions = soup.find_all('span', class_="position")
#for position in positions:
#        print(position.text)
f.close()
