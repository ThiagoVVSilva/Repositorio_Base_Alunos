from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.globo.com/")
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.title)
print(soup.title.sting)
link = soup.select("a")# seleciona todas as tags a
for link in link[:5]:
    print(link.get("href"))