#   Console Агрегатор новостей.
from flask import Flask
import ParserNews


app = Flask(__name__)


@app.route("/")
def index():
    return 'Агрегатор новостей.'


@app.route("/news", methods=['GET'])
def newsby():
    news = 'Последние новости:\n'
    for i in range(len(ParserNews.create_class('news'))):
        news += (ParserNews.create_class('news')[i] + '\n')
    return news


@app.route("/news/tut.by", methods=['GET'])
def tutby():
    tut_by = 'Новости tut.by:\n'
    for i in range(len(ParserNews.create_class('tut_by'))):
        tut_by += (ParserNews.create_class('tut_by')[i] + '\n')
    return tut_by


@app.route("/news/yandex.by/", methods=['GET'])
def yandexby():
    yandex_by = 'Новости yandex.by:'
    for i in range(len(ParserNews.create_class('yandex_by'))):
        yandex_by += (ParserNews.create_class('yandex_by')[i] + '\n')
    return yandex_by


@app.route("/news/belta.by/", methods=['GET'])
def beltaby():
    belta_by = 'Новости belta.by:\n'
    for i in range(len(ParserNews.create_class('belta_by'))):
        belta_by += (ParserNews.create_class('belta_by')[i] + '\n')
    return belta_by


if __name__ == "__main__":
    app.run(debug=True)
