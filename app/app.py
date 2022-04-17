import json
import os
from flask import Flask, redirect, request, url_for, jsonify
import requests
import serv
import connexion

def create_app():
    app = connexion.App(__name__, specification_dir="./")

    app.app.config['JSON_AS_ASCII'] = False
    app.add_api("swagger.yaml")

    url = 'https://blsspain-belarus.com/contact.php'

    return app

app = create_app()

@app.route("/")
def index():
    return (
        "<p>add <b>/api/swagger.yaml</b> to see swagger</p>"
        "<p>add <b>/visa-center</b> to URL to get info about visa center</p>"
        "<p>add <b>/news</b> to URL to get news of visa center</p>"
        "<p>add <b>/news_in_file</b> to URL to save file about new of visa center</p>"
    )


@app.route("/to-file")
def to_file():
    all_centres = serv.create_file()
    return (
        "<p>{}</p>"
        "<p>wrote to file</p>".format(all_centres)
    )

@app.route("/visa-center")
def visa_center():
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
    app.run(host='0.0.0.0', debug=True)