from flask import Flask, render_template, request, url_for
from .bot import Bot
import configparser
import os

app = Flask(__name__)
app.debug = True

config = configparser.ConfigParser()
config.read('settings.ini')
BOT_TOKEN = config['Bot']['token']

@app.route("/")
def index():
    b = Bot(BOT_TOKEN)
    b.set_webhook('https://caesar-cipher-encrypt-decrypt.herokuapp.com/hook/')
    return ''

@app.route("/hook/", methods=['POST'])
def hook():
    b = Bot(BOT_TOKEN)
    result = b.checkResult(request.json)
    return ''
