from flask import Flask, render_template, redirect, url_for, request, Response, send_from_directory
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        name = ["Chico",'Luno','Augusta','Charlotte Hazelrink']
        return render_template('home.html', list = name)
    elif request.method == 'POST':
        a = request.form.get('username')
        b = request.form.get('password')

        if a == 'luno' and b == '2.6':
            return 'correct'
        else:
            return 'incorrect'




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

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(director= 'downloads', filename = filename, downlload_name ="result.cvs")
    
    



if __name__ == '__main__':
    app.run(debug=True) 