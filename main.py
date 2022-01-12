from bs4 import BeautifulSoup
import requests

url = 'https://id.carousell.com/u/carousell_id/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
contents = requests.get(url, headers=headers)

soup = BeautifulSoup(contents.text, 'html.parser')
# print(soup.prettify())
data = soup.find_all('div', 'D_asM D_rT M_p_ D_rV M_pB')
print(data[0].text)

