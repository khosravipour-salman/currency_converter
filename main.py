import requests
from bs4 import BeautifulSoup


toman = input('Chand toomand dari? : ')

url = 'https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1'
req = requests.get(url)

soup = BeautifulSoup(req.content, features="html.parser")

table_element = soup.find('table', attrs={'class': 'data-table'})
td_content = table_element.find('td', attrs={'class': 'nf'}).contents[0]

dollar = int(td_content.split(',').pop(0)) * 100
print(dollar * int(toman))
