import urllib.parse
import re
from bs4 import BeautifulSoup as bs
import requests

def Check(q):
    raw_query=q  #Preserving original string to return if error is excepted
    q = str(str.lower(q)).strip()
    url = "http://www.google.com/search?q=" + urllib.parse.quote(q)
    source=requests.get(url).text
    soup=bs(source,'lxml')
    ans = soup.find('a', attrs={'class' : 'spell'})
    try:
        result = repr(ans.contents)
        result = result.replace("u'","")
        result = result.replace("/","")
        result = result.replace("<b>","")
        result = result.replace("<i>","")
        result = re.sub('[^A-Za-z0-9\s]+', '', result)
        result = re.sub(' +',' ',result)
    except AttributeError:
        result = raw_query
    return result
