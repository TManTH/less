from bs4 import BeautifulSoup
import requests

# commit test
#https://yar.stararbat.ru/
#https://yandex.ru/pogoda/yaroslavl?via=reg&lat=57.541603&lon=39.975708
url = "https://dikidi.net/687868"
page = requests.get(url)

soup = BeautifulSoup(page.text,"html.parser")
print(soup)
print(page.status_code)
