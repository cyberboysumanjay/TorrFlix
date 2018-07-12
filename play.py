import json
from bs4 import BeautifulSoup as bs
import requests
import urllib.parse
import pyperclip
import colored
from colored import stylize
import open_magnet
import peerflix_play
query=input("Enter the movie name:\n")

# Handle Streaming
def handle_stream(magnet_link):
    print("Do you want to stream the movie?\n")
    print(stylize("Press 1 for Yes or Press 2 for No",colored.fg("red")))
    selection=int(input())
    if selection==1:
        peerflix_play.peerflix_stream(magnet_link)
    elif selection==2:
        print("Ok! Paste the magnet link in your default Torrent Client\n")
    else:
        print("Wrong choice! Please Try Again\n")
        
def yts_search(query):
    print(stylize("Welcome to YTS Movie Downloader.\n", colored.fg("red")))
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
    m1='magnet:?xt=urn:btih:'
    m4='&tr='
    m5=['udp://open.demonii.com:1337/announce','udp://tracker.openbittorrent.com:80','udp://tracker.coppersurfer.tk:6969','udp://glotorrents.pw:6969/announce','udp://tracker.opentrackr.org:1337/announce','udp://torrent.gresille.org:80/announce','udp://p4p.arenabg.com:1337','udp://tracker.leechers-paradise.org:6969']
    URL_Movie_Name=result['title_long']+" ["+available_torrents[choice]['quality']+"] [YTS.AG]"
    URL_Encoded_Movie_Name=urllib.parse.quote_plus(URL_Movie_Name)
    m3='&dn='+URL_Encoded_Movie_Name
    trackers=""
    for i in range(len(m5)):
        trackers=trackers+m4+m5[i]
    magnet_link=m1+m2+m3+trackers
    print(stylize("Your magnet link is copied to your clipboard",colored.fg("yellow")))
    print(magnet_link)
    pyperclip.copy(magnet_link)
    handle_stream(magnet_link)

def piratebay_search(query):
    scrapper_api='https://api.scraperapi.com/?key=2500866341976677504461594942127656&url='
    url=scrapper_api+'https://pirateproxy.mx/search/'+query+'/0/99/0'
    print("Searching......")
    source=requests.get(url).text
    soup=bs(source,'lxml')
    results=soup.find_all('div',class_='detName')
    i=1
    for r in results:
        print(i,r.text)
        i=i+1
    print("Enter the Serial Number of the search item you like to download: ")
    choice=int(input())
    print ("Fetching data.....")
    magnet_results=soup.find_all('a',title='Download this torrent using magnet')
    a=[]
    for m in magnet_results:
        a.append(m['href'])
    magnet_link=(a[choice-1])
    print("Magnet Link of your selected choice has been fetched.")
    pyperclip.copy(magnet_link)
    print ("Your magnet link is now in your clipboard.")
    handle_stream(magnet_link)

def kickass_search(query):
    scrapper_api='https://api.scraperapi.com/?key=2500866341976677504461594942127656&url='
    base_url="https://kickass.unblocked.vet/usearch/"
    url=scrapper_api+base_url+query+'/'
    print("Searching......")
    source=requests.get(url).text
    soup=bs(source,'lxml')
    name=soup.find_all('a', class_="cellMainLink")
    results=[]
    i=1
    for r in name:
        print(i,r.text)
        i=i+1
    print("Enter the Serial Number of the search item you like to download: ")
    choice=int(input())
    print ("Fetching data.....")
    magnet=soup.find_all('a', title="Torrent magnet link")
    a=[]
    for m in magnet:
        a.append(m['href'])
    magnet_link=(a[choice-1])
    print("Magnet Link of your selected choice has been fetched.")
    pyperclip.copy(magnet_link)
    print ("Your magnet link is now in your clipboard.")
    handle_stream(magnet_link)

engine=int(input("Select your preferred search engine: \n1: PirateBay\n2: Kickass\n3: YTS\n"))
if engine==1:
    piratebay_search(query)
elif engine==2:
    kickass_search(query)
elif engine==3:
    yts_search(query)
else:
    print("Wrong Choice! Try again")
    quit()
