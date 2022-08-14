import requests
from bs4 import BeautifulSoup
import urllib.request
from youtubesearchpython import VideosSearch
f = open('currentcharts', 'w', encoding="utf-8")
URL = "https://www.officialcharts.com/charts/singles-chart/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

sausage = ""
tables = soup.find_all('div', class_="track")

for song in tables:
    titles =  song.find_all("div", {"class": "title"})
    artists =  song.find_all("div", {"class": "artist"})
    
    for title in titles:
        #print(title.text.strip())
        sausage = title.text.strip()
    for artist in artists:
        #print(artist.text.strip())
        sausage += " - " + artist.text.strip()
        #videosSearch = VideosSearch(sausage, limit = 1)
        #for video in videosSearch.result()['result']:
        #    print(video['id'])
        f.write(sausage + "\n")
        print(sausage)

#positions = soup.find_all('span', class_="position")
#for position in positions:
#        print(position.text)
f.close()
