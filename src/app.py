from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'TransmiDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route("/")
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute("select * from Cliente")
    bdResponse = cur.fetchall()
    
    print(bdResponse)

    return json.dumps(bdResponse)

if __name__ == '__main__':
    app.run(debug=True, port=5050)