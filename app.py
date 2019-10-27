from process import process

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def call():
    return process(request)
