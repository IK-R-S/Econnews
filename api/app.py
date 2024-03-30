from bs4 import BeautifulSoup
from requests import get

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

class Websites:
    def __init__(self):
        pass


    def uol(self):
        url = 'https://economia.uol.com.br/noticias/'
        req = get(url, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        elements = html.find_all('div', class_='thumbnails-wrapper')

        response = []

        for element in elements:
            title = element.find('h3').get_text()
            link = element.find('a')['href']
            div_img = element.find_all('div', class_='thumb-layer')
            for i in div_img:
                image = i.find('img')['data-src']
            news = {"title": title, "link": link, "image": image}
            print(image)
            response.append(news)
        
        return response



    def cnn(self):
        url = 'https://www.cnnbrasil.com.br/economia/'
        req = get(url, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        elements = html.find_all('a', class_='home__list__tag')

        response = []

        for element in elements:
            title = element.find('h3', class_="news-item-header__title market__new__title").get_text()
            link = element['href']
            image = element.find('img')['src']
            news = {"title": title, "link": link, "image": image}
            response.append(news)
        
        return response


    def antagonista(self):
        pass


    def g1(self):
        pass


    def infomoney(self):
        pass
