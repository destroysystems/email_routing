from email_routing import process

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def call():
    if request.method == 'GET':
        return 'Hi!'
    elif request.method == 'POST':
        return 'Success!'
