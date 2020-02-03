# WEB Агрегатор новостей.
from flask import Flask
import ParserNews


app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Агрегатор новостей.</h1>'


@app.route("/news/", methods=['GET'])
def newsby():
    news = '<ul><h1>Последние новости:</h1>'
    for i in range(len(ParserNews.create_class('news'))):
        news += ('<li>' + ParserNews.create_class('news')[i] + '</li>')
    return news + '</ul>'


@app.route("/news/tut.by/", methods=['GET'])
def tutby():
    tut_by = '<ul><h1>Новости tut.by:</h1>'
    for i in range(len(ParserNews.create_class('tut_by'))):
        tut_by += ('<li>' + ParserNews.create_class('tut_by')[i] + '</li>')
    return tut_by + '</ul>'


@app.route("/news/yandex.by/", methods=['GET'])
def yandexby():
    yandex_by = '<ul><h1>Новости yandex.by:</h1>'
    for i in range(len(ParserNews.create_class('yandex_by'))):
        yandex_by += ('<li>' + ParserNews.create_class('yandex_by')[i] + '</li>')
    return yandex_by + '</ul>'


@app.route("/news/belta.by/", methods=['GET'])
def beltaby():
    belta_by = '<ul><h1>Новости belta.by:</h1>'
    for i in range(len(ParserNews.create_class('belta_by'))):
        belta_by += ('<li>' + ParserNews.create_class('belta_by')[i] + '</li>')
    return belta_by + '</ul>'


if __name__ == "__main__":
    app.run(debug=True)
