import json
import os
from bs4 import BeautifulSoup
from flask import Flask, redirect, request, url_for, jsonify
import requests
import serv
from swagger_ui import api_doc

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api_doc(app, config_path='.\swagger.yaml', url_prefix='/api/doc', title='API doc')
url = 'https://blsspain-belarus.com/contact.php'


@app.route("/")
def index():
    return (
        "<p>add <b>/api/swagger.yaml</b> to see swagger</p>"
        "<p>add <b>/visa-center</b> to URL to get info about visa center</p>"
        "<p>add <b>/news</b> to URL to get news of visa center</p>"
        "<p>add <b>/news_in_file</b> to URL to save file about new of visa center</p>"
    )


@app.route("/visa-center", methods=['POST', 'GET'])
def visa_center():
    if request.method=='POST':
        serv.create_center()
    center = serv.read_visa_center()
    return jsonify(center)


@app.route("/news", methods=['POST', 'GET'])
def news():
    return jsonify(serv.create_correct_data(
        serv.get_info_site(
            'https://newssearch.yandex.ru/news/search?ajax=0&from_archive=1&neo_parent_id=1647441873582156-81607431716702717200156-production-news-app-host-112-NEWS-NEWS_NEWS_SEARCH&p=2&text=испанский+визовый+центр+в+Беларуси',
            'https://newssearch.yandex.ru/news/search?from_archive=1&p=1&text=испанский+визовый+центр+в+Беларуси&ajax=1&neo_parent_id=1647442457082880-358481777924388487800157-production-news-app-host-130-NEWS-NEWS_NEWS_SEARCH'))
            )


@app.route("/news_in_file", methods=["POST", "GET"])
def news_in_file():
    serv.save_in_file(serv.create_correct_data(
        serv.get_info_site(
            'https://newssearch.yandex.ru/news/search?ajax=0&from_archive=1&neo_parent_id=1647441873582156-81607431716702717200156-production-news-app-host-112-NEWS-NEWS_NEWS_SEARCH&p=2&text=испанский+визовый+центр+в+Беларуси',
            'https://newssearch.yandex.ru/news/search?from_archive=1&p=1&text=испанский+визовый+центр+в+Беларуси&ajax=1&neo_parent_id=1647442457082880-358481777924388487800157-production-news-app-host-130-NEWS-NEWS_NEWS_SEARCH'))
            )
    return "<h3>File save</h3>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)