import requests
from bs4 import BeautifulSoup

wn = [("005935","삼성전자 우"), ("000270","기아차"), ("005380","현대차")]
for i in wn:
    url = f"https://finance.naver.com/item/sise.naver?code={i[0]}"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("strong#_nowVal.tah.p11")
    print(i[1] + "의 가격은 : ", end="")
    print(price.text)