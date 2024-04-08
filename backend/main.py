import random

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/random")
def random_number():
    number = random.randint(0, 100)
    print("Random number generated: ", number)
    return f"{number}"
