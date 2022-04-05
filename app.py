from flask import Flask, redirect, request, url_for, jsonify
import connexion
import requests
import serv


# app = Flask(__name__)

app = connexion.App(__name__, specification_dir="./")

app.app.config['JSON_AS_ASCII'] = False

app.add_api("swagger.yaml")

url = 'https://blsspain-belarus.com/contact.php'


@app.route("/")
def index():
    return (
        "<p>add <b>/to-file</b> to URL to  scrap info about spain visa centers</p>"
        "<p>add <b>/visa-center</b> to URL to get info about visa center</p>"
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


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
