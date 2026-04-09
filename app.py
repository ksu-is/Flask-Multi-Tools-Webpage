from flask import Flask, render_template, redirect, url_for, request, Response, send_from_directory
import pandas as pd
import os
import uuid
from flask import session, make_response, flash

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = "luno"

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        names = ["Chico",'Luno','Augusta','Charlotte Hazelrink']
        return render_template('home.html', list = names, message = 'Index')
    elif request.method == 'POST':
        id = request.form.get('username')
        pas = request.form.get('password')

        if id == 'luno' and pas == '1234':
            return 'correct'
        else:
            return 'incorrect'
        
@app.route('/image')
def image():
    return render_template('image.html')



@app.route('/loli')
def LOLI():
    return render_template('charlotte.html')

@app.route('/redirect')
def redirect1():
    return redirect(url_for('LOLI'))

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
    df = pd.read_excel(file)
    return df.to_html()

@app.route('/csv_converter', methods = ['POST'])
def csv_converter():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    filename = f"{uuid.uuid4()}.csv"
    filepath = os.path.join('downloads', filename)
    df.to_csv(filepath)
    return render_template('download.html', filename=filename)

@app.route('/set_data')
def set_data():
    session['name'] = 'augusta'
    session['hair'] = 'red'
    return render_template('home.html', message = 'Session data set')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'hair' in session.keys():
        name = session['name']
        hair = session['hair']
        return render_template('home.html', message = f"Name: {name}, Hair: {hair}")
    else:
        return render_template('home.html', message = 'No session data found')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('home.html', message = 'Session cleared')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('home.html', message = 'Cookie set'))
    response.set_cookie(key='cookie key', value='cookie value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie key']
    return render_template('home.html', message = f"Cookie value: {cookie_value}")

@app.route('/clear_cookie')
def clear_cookie():
    response = make_response(render_template('home.html', message = 'Cookie cleared'))
    response.set_cookie(key='cookie key', expires=0)
    return response

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'luno' and password == '1234':
            flash('Logged in successfully')
            return render_template('image.html')
        else:
            flash('Log in failed')
            return render_template('image.html')





    
    



if __name__ == '__main__':
    app.run(debug=True) 