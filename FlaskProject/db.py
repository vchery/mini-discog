import psycopg2
from dotenv import load_dotenv, dotenv_values

load_dotenv('.env')
def start_connect():
    connection = psycopg2.connect(database=dotenv_values(".env")['DB'],
                                  user=dotenv_values(".env")['USER'],
                                  password=dotenv_values(".env")['PASSWORD'],
                                  host=dotenv_values(".env")['HOST'],
                                  port=dotenv_values(".env")['PORT'])
    return connection

def show_details():
    conn = start_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ariana_grande")
    discography = cursor.fetchall()
    return discography

def album_details(album_id):
    conn = start_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ariana_grande WHERE album_id = (%s)", [album_id])
    albums = cursor.fetchall()
    return albums