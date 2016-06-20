from flask import Flask, render_template, request
from cipher import Caesar
import os

host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    c = Caesar(request.json['key'])
    encrypted_sentence = c.encrypt_sentence(request.json['sentence'])
    return str(encrypted_sentence)

@app.route("/decrypt", methods=['POST'])
def decrypt():
    c = Caesar(request.json['key'])
    decrypted_sentence = c.decrypt_sentence(request.json['sentence'])
    return str(decrypted_sentence)


app.run(host=host, port=port, debug=True)
