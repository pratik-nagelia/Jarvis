from flask import Flask
from controller import *

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome to Patrick's Den !!"


@app.route("/<gpio>/<state>")
def switch_state(gpio, state):
    switch(gpio, state)
    return gpio + ":" + state


if __name__ == "__main__":
    init()
    app.run()
