from flask import Flask, render_template, request, url_for
from .bot import Bot

app = Flask(__name__)

@app.route("/")
def index():
    return ''

@app.route("/hook/", methods=['POST'])
def hook():
    b = Bot()
    result = b.checkResult(request.data)
    return str(result)
