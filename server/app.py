from flask import Flask
from flask_cors import CORS
from controller import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return "Welcome to Patrick's Den !!"


@app.route("/<gpio>/<state>")
def switch_state(gpio, state):
    switch(int(gpio), state)
    return gpio + ":" + state


if __name__ == "__main__":
    init()
    app.run(host="0.0.0.0")
