import sqlite3
from flask import Flask, g, request, render_template

app = Flask(__name__)
DATABASE = './sqlite.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/process_url/ikea/<path:url>')
def process_url(url):
    # Do something with the URL
    return f"Processed URL: {url}"

@app.route('/')
def form():
    return render_template('product_form.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    text = request.form['text']
    # Process the URL and text
    return render_template("product_submitted.html")