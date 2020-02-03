# Парсер новостей по RSS
import requests as req
from bs4 import BeautifulSoup
import config


class SiteScraper():

    def __init__(self, url):
        self.url = url

    def parser_news(self):
        # Собираем последние новости
        news = []
        resp = req.get(self.url)
        soup = BeautifulSoup(resp.text, 'lxml')
        tag = soup.findAll('item')
        for i in range(len(tag)):
            title = tag[i].title.string
            link = tag[i].guid.string
            description = tag[i].description.string
            news.append(title + '\n <a href="' + link+'"> подробнее.</a>')
        return news


def create_class(class_name):
    #    генерируем переменные класса для парсера.
    object_class = []
    data = config.sourse_url
    if class_name in data:
        for key in data:
            globals()[key] = SiteScraper(data[key])
            if class_name == str(key):
                object_class = (globals()[key].parser_news())
            else:
                pass
    elif class_name == "news":
        for key in data:
            class_name = str(key)
            globals()[key] = SiteScraper(data[key])
            if class_name == str(key):
                object_class += (globals()[key].parser_news())
    else:
        pass
    return object_class
