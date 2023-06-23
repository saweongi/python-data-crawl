import requests
from bs4 import BeautifulSoup

movieUrl = "https://entertain.naver.com/movie"

response = requests.get(movieUrl)
html = response.text

soup = BeautifulSoup(html, "html.parser")

articleTitles = soup.select("a.tit")

inputs = input("필터링 하고픈 키워드는?")

for at in articleTitles:
    saveTitle = at.text
    if 0 < saveTitle.count(inputs):
        print(saveTitle)