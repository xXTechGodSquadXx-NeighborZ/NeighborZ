
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact-us/', methods=['GET'])
def contact_page():
    return render_template('contact-us.html')

@app.route('/forum/', methods=['GET'])
def forum():
    return '<meta http-equiv="Refresh" content="0; url=https://neighborz.freeforums.net/" />'