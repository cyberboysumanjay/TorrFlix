import json
from bs4 import BeautifulSoup as bs
import requests
import urllib.parse
import pyperclip
import colored
from colored import stylize
import open_magnet
import peerflix_play

print(stylize("Welcome to YTS Movie Downloader.\n", colored.fg("red")))
query=input("Enter the movie name:\n")
url='https://yts.am/api/v2/list_movies.json?query_term='+query
print()
print(stylize("Searching......\n",colored.fg("green")))
source=requests.get(url).text
loaded_json= (json.loads(source))

print(stylize(loaded_json['status_message'],colored.fg('red')))
movie_data=(loaded_json['data'])
movies=movie_data['movies']
result=movies[0]
print(stylize("Here is your search result",colored.fg('green')))
print(stylize('Title: ',colored.fg("red")))
print(result['title_long'])
print(stylize('Rating: ',colored.fg("red")))
print(result['rating'])
print(stylize('Summary: ',colored.fg("red")))
print(result['summary'])
print(stylize('Language: ',colored.fg("red")))
print(result['language'])
available_torrents=result['torrents']
print(stylize("Here is a list of available quality: ",colored.fg("red")))
j=1
for i in available_torrents:
    print (j,stylize("Quality:",colored.fg("yellow")),i['quality'],stylize("Size:",colored.fg("yellow")),i['size'])
    j=j+1
choice=int(input("Enter your choice: "))
choice=choice-1
hash_code=available_torrents[choice]['hash']
print(stylize("Building Magnet Link...",colored.fg("yellow")))
m2=hash_code
#print(m2)
m1='magnet:?xt=urn:btih:'

m4='&tr='
m5=['udp://open.demonii.com:1337/announce','udp://tracker.openbittorrent.com:80','udp://tracker.coppersurfer.tk:6969','udp://glotorrents.pw:6969/announce','udp://tracker.opentrackr.org:1337/announce','udp://torrent.gresille.org:80/announce','udp://p4p.arenabg.com:1337','udp://tracker.leechers-paradise.org:6969']
#magnet:?xt=urn:btih:EE07FC0BC38040AC3E7440C4DE02C02A4A8E0154&dn=Ant-Man+%282015%29+%5B1080p%5D+%5BYTS.AG%5D&    tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337

URL_Movie_Name=result['title_long']+" ["+available_torrents[choice]['quality']+"] [YTS.AG]"
#print(URL_Movie_Name)
URL_Encoded_Movie_Name=urllib.parse.quote_plus(URL_Movie_Name)
m3='&dn='+URL_Encoded_Movie_Name
#print(URL_Encoded_Movie_Name)
trackers=""
for i in range(len(m5)):
    trackers=trackers+m4+m5[i]

magnet_link=m1+m2+m3+trackers
print(stylize("Your magnet link is copied to your clipboard",colored.fg("yellow")))
print(magnet_link)
pyperclip.copy(magnet_link)

print(stylize("Press 1 for Yes or Press 2 for No",colored.fg("red")))
selection=int(input("Do you want to stream the movie?\n"))
if selection==1:
#    open_magnet.open_magnet(magnet_link)
    peerflix_play.peerflix_stream(magnet_link)
elif selection==2:
    print("Ok! Paste the magnet link in your default Torrent Client\n")
else:
    print("Wrong choice! Please Try Again\n")
