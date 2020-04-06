import os
from flask import Flask, render_template, url_for


IMG_DIR = "static/img/"


class Image:
    def __init__(self, index, filename):
        self.index = index
        self.filename = filename


def image_generator(images):
    for index, filename in enumerate(images):
        yield Image(index, filename)


app = Flask(__name__)


@app.route("/carousel")
def carousel():
    params = {
        "title": "Пейзажи Марса",
        "images": list(image_generator(os.listdir(IMG_DIR))),
    }
    return render_template("carousel.html", **params)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
