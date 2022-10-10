import requests
from bs4 import BeautifulSoup


headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

r = requests.get('https://www.metacritic.com/browse/games/release-date/new-releases/pc/date', headers=headers)

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

soup.prettify()

games = soup.find_all('a', class_="title")

releases = []

for i in games:
    releases.append(i.text)


f = open("new_games.txt", "w", encoding='utf-8')

f.write('\n'.join(releases))
f.close()
