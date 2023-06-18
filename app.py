from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/eatup/<region>')
def eatup(region):
    regions = read_eatup_by_region(region)
    return render_template("eatup.html", region=region, eatup=regions)

@app.route('/region/<int:establishment_id>')
def establishment(establishment_id):
    establishment = read_eatup_by_id(establishment_id)
    return render_template("establishment.html",establishment=establishment)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['post'])
def processing():
    establishment_data = {
        "region": request.form['establishment_region'],
        "name": request.form['establishment_name'],
        "image": request.form['establishment_image'],
        "color": request.form['establishment_color'],
        "description": request.form['establishment_description'],
        "address": request.form['establishment_address'],
        "contact": request.form['establishment_contact']
    }
    insert_establishment(establishment_data)
    return redirect(url_for('eatup', region=request.form['establishment_region']))

@app.route('/modify', methods=['post'])
def modify():
    if request.form["modify"] == "Edit Entry":
        id = request.form["establishment_id"] 
        establishment = read_eatup_by_id(id)
        return render_template('update.html', establishment=establishment)
    elif request.form["modify"] == "Delete Entry":
        establishment_data = {
            "establishment_id" : request.form['establishment_id'],
        }
        delete_establishment(establishment_data)
        return render_template('index.html')
        

@app.route('/update', methods=['post'])
def update():
    establishment_data = {
        "establishment_id" : request.form['establishment_id'],
        "region": request.form['establishment_region'],
        "name": request.form['establishment_name'],
        "image": request.form['establishment_image'],
        "color": request.form['establishment_color'],
        "description": request.form['establishment_description'],
        "address": request.form['establishment_address'],
        "contact": request.form['establishment_contact']
    }
    update_establishment(establishment_data)
    return redirect(url_for('establishment', establishment_id=request.form['establishment_id']))

if __name__ == "__main__":
    app.run(debug=True)