from flask import Flask
import mysql.connector
import os


app = Flask(__name__)
app.secret_key = 'upsites'
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    password="casa45220913",
    database="jogoteca",
    auth_plugin='mysql_native_password'
)
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

from views import *

if __name__ == '__main__':
    app.run(debug=True)
