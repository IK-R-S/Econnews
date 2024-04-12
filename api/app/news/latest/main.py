from random import shuffle
from bs4 import BeautifulSoup
from requests import get


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Crie uma classe para gerenciar as diferentes fontes de notícias
class NewsManager:
    def __init__(self):
        self.latest = Latest()

    def get_all_news(self):
        all_news = []
        all_news.extend(self.latest.cnn())
        all_news.extend(self.latest.oglobo())
        all_news.extend(self.latest.infomoney())
        
        # Embaralhe a ordem das notícias
        shuffle(all_news)
        
        return all_news

# Crie uma classe para buscar as notícias mais recentes de cada fonte
class Latest:
    def __init__(self):
        pass

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
            news = {"title": title, "link": link, "image": image, "source": "cnnbrasil.com.br", "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/CNN_International_logo.svg/600px-CNN_International_logo.svg.png"}
            response.append(news)
        
        return response

    def oglobo(self):    
        url = 'https://oglobo.globo.com/economia/'
        req = get(url, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        elements = html.find_all('div', class_='feed-post-body')

        response = []

        for element in elements:
            title = element.find('a', class_='feed-post-link').get_text()
            link = element.find('a', class_='feed-post-link')['href']
            img_element = element.find('img', class_='bstn-fd-picture-image')
            if img_element != None:
                image = img_element['src']
            
            news = {"title": title, "link": link, "image": image, "source": "oglobo.globo.com", "icon": "https://d37iydjzbdkvr9.cloudfront.net/google-assistant/o-globo/logo-globo-1000x1000.jpg"}
            response.append(news)
        
        return response

    def infomoney(self):
        url = 'https://www.infomoney.com.br/ultimas-noticias/'
        req = get(url, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        elements = html.find_all('div', class_='row py-3 item')

        response = []

        for element in elements:
            title = element.find('a')['title']
            link = element.find('a')['href']
            image = element.find('img')['src']
            news = {"title": title, "link": link, "image": image, "source": "infomoney.com.br", "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWglNgnzVLJJz0VkBWP8aRsWlxfvq5KM_WbQc0-SJbkg&s"}
            response.append(news)
        
        return response    


