import os
from flask import Flask, request, render_template
import db
app = Flask(__name__)

@app.route('/')
def index():
    # display artist names
    return render_template('index.html')

@app.route('/artist')
def artist():
    # display artist's albums
    return render_template('artist.html')

@app.route('/albums')
def albums():
    return render_template('albums.html', albums = db.show_details())

@app.route('/albums/<album_id>')
def album(album_id):
    return db.album_details(album_id)

if __name__ == '__main__':
    app.run()