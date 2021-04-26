from bs4 import BeautifulSoup
import webbrowser
import requests



site = requests.get('http://3615.world')
page = site.content
soup = BeautifulSoup(page, "html.parser")
music = soup.find('title_song')

print(music)