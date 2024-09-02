from bs4 import BeautifulSoup
import requests
#https://apteka.ru/
# https://apteka.ru/search/?q=пенталгин  запрос поиска
#https://yar.stararbat.ru/
#https://yandex.ru/pogoda/yaroslavl?via=reg&lat=57.541603&lon=39.975708

url_list = ["https://apteka.ru/"," "]
print(url_list)
page = requests.get(url_list[0]+"search/?q=пенталгин")
print(page.status_code)
soup = BeautifulSoup(page.text,"html.parser")

print(soup)
