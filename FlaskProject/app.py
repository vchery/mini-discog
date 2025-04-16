import os
from flask import Flask, request, render_template
import db
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    # display artist names
    return render_template('home.html')

@app.route('/albums')
def albums():
    return render_template('albums.html', albums = db.show_details())

if __name__ == '__main__':
    app.run()