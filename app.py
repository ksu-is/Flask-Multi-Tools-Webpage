from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    name = ["Chico",'Luno','Augusta','Charlotte Hazelrink']
    return render_template('home.html', list = name)

@app.route('/loli')
def loli():
    return render_template('charlotte.html')



if __name__ == '__main__':
    app.run(debug=True) 