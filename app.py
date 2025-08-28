from flask import Flask  # correct

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the About page!'
def bad_function ():return 42

