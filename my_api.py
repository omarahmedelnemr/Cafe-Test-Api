from random import randint
from flask import Flask,request
import sqlite3
import json
app = Flask(__name__)

def convert_list(list):
    new_dict = []
    data = {}
    for item in list:
        data = {
            'name': item[1],
            'map_url': item[2],
            'img': item[3],
            'location': item[4],
            'hase_sokects': item[5],
            'has_toilet': item[6],
            'has_wifi': item[7],
            'can_take_calls': item[8],
            'seats': item[9],
            'coffie_price': item[10]
        }
        new_dict.append(data)
    return new_dict
@app.route("/random")
def random():
    db = sqlite3.connect('cafes.db')
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM cafe WHERE id={randint(1, 21)}')
    row = cursor.fetchall()
    data = convert_list(row)

    return data[0]



@app.route('/all')
def all():
    db = sqlite3.connect('cafes.db')
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM cafe')
    row = cursor.fetchall()
    data = convert_list(row)
    return {'data':data}




@app.route('/search')
def search():
    loc = request.args
    db = sqlite3.connect('cafes.db')
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM cafe WHERE location="{loc["loc"]}"')
    row = cursor.fetchall()
    data = convert_list(row)

    return {'data':data}


@app.route('/add' , methods =['POST','GET'])
def add():
    if request.method =='POST':
        data = tuple(request.form.values())
        db = sqlite3.connect('cafes.db')
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO cafe VALUES{data}")
        db.commit()
        return {'Data':'Added'}

@app.route('/update/<id>' , methods =['POST','GET','PATCH'])
def remove(id):
    if request.method =='PATCH':
        attr =list(request.form.keys())[0]

        db = sqlite3.connect('cafes.db')
        cursor = db.cursor()
        cursor.execute(f"UPDATE cafe SET {attr}=' {request.form[attr]}' WHERE id = {id}")
        db.commit()

        return {'data':attr}

if __name__ == '__main__':
    app.run(debug=True)
