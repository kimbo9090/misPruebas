import urllib.request
from bs4 import BeautifulSoup
fullVids = []
textToSearch = 'PewDiePie'
query = urllib.parse.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    fullVids.append('https://www.youtube.com' + vid['href'])

for vid in fullVids:
    if 'user' in vid:
        fullVids.remove(vid)

