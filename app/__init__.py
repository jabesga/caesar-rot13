from flask import Flask, render_template, request
from .cipher import Caesar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/encrypt/", methods=['POST'])
def encrypt():
    return 'test'
    c = Caesar(request.json['key'])
    encrypted_sentence = c.encrypt_sentence(request.json['sentence'])
    return str(encrypted_sentence)

@app.route("/decrypt/", methods=['POST'])
def decrypt():
    c = Caesar(request.json['key'])
    decrypted_sentence = c.decrypt_sentence(request.json['sentence'])
    return str(decrypted_sentence)
