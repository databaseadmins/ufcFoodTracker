from flask import Flask, render_template, g, request
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






@app.route('/')
def index():
    return render_template('home.html')


@app.route('/view')
def view():
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