import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask, request, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)
load_dotenv()
def db_connect():
    conn = psycopg2.connect(dbname=os.getenv('DB'),
                            user=os.getenv('USER'),
                            password=os.getenv('PW'),
                            host=os.getenv('HOST'),
                            port=os.getenv('PORT'))
    return conn

@app.route('/')
def index():  # put application's code here
    return 'Index Page'

@app.route('/sql')
def show_details():
    conn = db_connect()
    print('Connected to database')
    cursor = conn.cursor()
    cursor.execute('select * from ariana_grande')
    discography = cursor.fetchall()
    #cursor.close()
    #conn.close()
    #print('Closing database connection')
    return render_template('index.html', discography=discography)

if __name__ == '__main__':
    app.run()
