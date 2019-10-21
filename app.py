from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def process():
    if request.method == 'GET':
        return 'Hi!'
    elif request.method == 'POST':
        return 'Correct!'
