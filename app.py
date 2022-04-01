import json
import os
from bs4 import BeautifulSoup

from flask import Flask, redirect, request, url_for, jsonify
import connexion
import requests
import serv


#app = Flask(__name__)
app = connexion.App(__name__, specification_dir="./")

app.app.config['JSON_AS_ASCII'] = False

app.add_api("swagger.yaml")



url = 'https://blsspain-belarus.com/contact.php'


@app.route("/")
def index():
    return (
        "<p>add <b>/api/swagger.yaml</b> to see swagger</p>"
        "<p>add <b>/visa-center</b> to URL to get info about visa center</p>"
    )

@app.route("/visa-center", methods=['POST', 'GET'])
def visa_center():
    if request.method=='POST':
        serv.create_center()
    center = serv.read_visa_center()
    return jsonify(center)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)