from bs4 import BeautifulSoup
from requests import get

# TODO: Create headers list for requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

# Classe de notícias mais recentes:
class Latest:
    def __init__(self):
        pass
    
    # UOL DESATIVADO
    '''   
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
    ''' 


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

    def oantagonista(self):
        url = 'https://oantagonista.com.br/economia/'
        req = get(url, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        

        response = []

        titles_array = []
        titles = html.find_all('h3', class_='ultimas-noticias-area__title-h3')
        for element in titles:
            if element.get_text() != 'Mais lidas':
                title = element.get_text()
                titles_array.append(title)
            else:
                pass

        links_array = []
        links = html.find_all('a', class_='ultimas-noticias-area__link')
        for element in links:
            link = element['href']
            links_array.append(link)

        # ISSUE: ADD IMAGE SCRAPPER
        '''
        images_div = html.find_all('div', class_='row')
        image_set = set()
        for element in images_div:
            figure = element.find('figure')
            if figure:
                image_tag = figure.find('img')
                if image_tag:
                    image_url = image_tag['src']
                    if image_url not in image_set:
                        image_set.add(image_url)
                        print(image_url)
        '''                               

        if len(titles_array) == len(links_array):
            for i in range(0, len(titles_array)):
                news = {"title": titles_array[i], "link": links_array[i]}
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
            
            news = {"title": title, "link": link, "image": image}
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
            news = {"title": title, "link": link, "image": image}
            response.append(news)
        
        return response    


    # TODO: Add news source
    def g1(self):
        pass
    def investing(self):
        pass
    def cartacapital(self):
        pass