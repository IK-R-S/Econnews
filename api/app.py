from bs4 import BeautifulSoup
from requests import get

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

class Websites:
    def __init__(self):
        pass


    def uol(self):
        url = 'https://economia.uol.com.br/ultimas/'
        req = get(url, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        elements = html.find_all('div', class_='thumbnails-wrapper')

        titles = []
        links = []
        response = {}

        for element in elements:
            title = element.find('h3').get_text()
            link = element.find('a')['href']

            response.update({title: link})
            titles.append(title)
            links.append(link)
        
        return response


    def g1(self):
        pass


    def infomoney(self):
        pass
