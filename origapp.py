from flask import Flask, render_template, g, request
from datetime import datetime
import sqlite3

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect('c:/git_repos/ufcFoodTracker/food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3_db'):
        g.sqlite_db.close






@app.route('/', methods=['GET','POST'])
def index():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        dt = datetime.strptime(date,'%Y-%m-%d')
        database_date=datetime.strftime(dt, '%Y%m%d')
        db.execute('insert into log_date (entry_date) values (?)', [database_date])
        db.commit()

    cur = db.execute('select entry_date from log_date order by entry_date desc')
    results = cur.fetchall()
    print(type(results))
    pretty_results = []
    for i in results:
        #print(i)
        single_date = {}
        d = datetime.strptime(str(i['entry_date']),'%Y%m%d')
        single_date['entry_date'] = datetime.strftime(d, '%B %d, %Y')
        pretty_results.append(single_date)
        #print(pretty_results)
<<<<<<< HEAD
=======


    return render_template('home.html', results = pretty_results)
>>>>>>> f294fa6b0a9122409fd0aec6c79ddbdf1f372abc


    return render_template('home.html', results = pretty_results)


@app.route('/view/<date>') #date soemthing like 20170520
def view(date):
    db =  get_db()
    cur = db.execute('select entry_date from log_date where entry_date = ?', [date])
    result = cur.fetchone()
    print(result)
    return '<h1>The date is {}</h1>'.format(result['entrydate'])
    return render_template('day.html')





@app.route('/food',methods=['GET','POST'])
def food():
    db = get_db()
    if request.method == 'POST':
        name=request.form['food-name']
        protein=int(request.form['protein'])
        carbohydrates=int(request.form['carbohydrates'])
        fat=int(request.form['fat'])
        calories = protein*8 + carbohydrates*4 + fat*9
        #return request.form
        #return '<h1>Name:{} Protein:{} Fat:{} Carbs:{}</h1>'.format(request.form['food-name'], \
        #request.form['protein'], request.form['carbohydrates'], request.form['fat'])                                                           
        db.execute('insert into food (name, protein, carbohydrates, fat, calories) values (?,?,?,?,?)', \
                [name, protein, carbohydrates, fat, calories ])
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fat, calories from food')
    results = cur.fetchall()
 
 
    return render_template('add_food.html', results = results)







#my own stuff here.
@app.route('/recipients')
def recipients():
    return None






if __name__ == '__main__':
    app.run(debug=True)