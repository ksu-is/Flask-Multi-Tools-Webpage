from flask import Flask, render_template, request, redirect, session, make_response, url_for, flash
from miscellaneous.states import us_states # A dictionary mapping state abbreviations to full state names
import random
import pandas as pd
import math

app = Flask(__name__, static_folder='static', static_url_path= '/', template_folder='templates')
app.secret_key = '1st application development' # In production, use a secure and random secret key, and keep it confidential.

# Not recommended for credential storage in production. 
# In production, use a secure method for storing and verifying user credentials,
# such as hashing passwords and using a database (SQLite, MySQL).
users = {
    "Luno": "1234",
    "chico": "eating"
}   
@app.route('/', methods=['GET','POST'])
def home():
    yourname = ''
    if request.method == 'POST':
        yourname = request.form.get('yourname')
    return render_template('home.html', message= yourname)

@app.route('/state_abbreviation', methods=['GET','POST'])
def state_abbreviation():
    full_state_name = ''
    state_abbreviation = ''
    if request.method == 'POST':
        state_abbreviation = request.form.get('state_abbreviation')
        full_state_name = us_states[state_abbreviation]
    return render_template('state_abbreviation.html', us_states=us_states, full_state_name=full_state_name, state_abbreviation=state_abbreviation)

@app.route('/calculator',methods=['GET','POST'])
def calculator():
    first_number = ''
    second_number = ''  
    operator = ''
    result =''
    if request.method == 'POST':
        first_number = request.form.get("first_number")
        second_number = request.form.get("second_number")
        operator = request.form.get("operator")

        if operator == "+":
            result = float(first_number) + float(second_number)
        elif operator == "-":
            result = float(first_number) - float(second_number)
        elif operator == "X":
            result = float(first_number) * float(second_number)
        elif operator == "÷":
            if float(second_number) == 0:
                result = "Error - Cannot divide by zero"
            else:
                result = float(first_number) / float(second_number)
        elif operator == "^":
            result = math.pow(float(first_number), float(second_number))
        
    return render_template('calculator.html',first_number=first_number,second_number=second_number,operator=operator,result=result)

@app.route('/guess_number', methods=['GET','POST'])
def guess_number():
    level = ''
    attempts = '' 
    target = '' 
    result = '' 
    guess = '' 
    count = ''
    reset = ''
    if request.method == 'POST':
        level = int(request.form.get('level'))
        attempts = int(request.form.get('attempts'))
        guess = int(request.form.get('guess', 0))
        count = int(request.form.get('count', 0))
        target = int(request.form.get('target',0))
        reset = request.form.get('reset')

        if not target or reset:
            if level == 1:
                target = random.randint(1, 9)
            elif level == 2:
                target = random.randint(10, 99)
            elif level == 3:
                target = random.randint(100, 999)
            elif level == 4:
                target = random.randint(1000, 9999)
            count = 0

        if guess:
            count += 1
            if count <= attempts:
                if guess == target:
                    result = f"Congratulations! You guessed the number {target}!"
                else:
                    if count == attempts:
                        result = f"Out of attempts - the number was {target}."
                    else:
                        if guess < target:                
                            result = "Too low. Try again!"
                        else:
                            result = "Too high. Try again!"
            else:
                result = f"Out of attempts - the number was {target}."

    return render_template('guess_number.html', level=level, result=result, attempts=attempts, guess=guess, count=count, target=target)

@app.route('/excel_upload', methods=['GET', 'POST'])
def excel_upload():
    if 'user' not in session:
        flash('Please log in first', 'warning')
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_excel(file)
        return df.to_html()
    return render_template('excel_upload.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/text_transformation', methods=['GET','POST'])
def text_transformation():
    input_text = ''
    transformation_type = ''
    result = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        transformation_type = request.form.get('transformation_type')

        if transformation_type == 'uppercase':
            result = input_text.upper()
        elif transformation_type == 'lowercase':
            result = input_text.lower()
        elif transformation_type == 'capitalize':
            result = input_text.capitalize()
        elif transformation_type == 'title':
            result = input_text.title()
    return render_template('text_transformation.html', input_text=input_text, transformation_type=transformation_type, result=result)

@app.route('/session_cookies', methods=['GET','POST'])
def session_cookies():
    message1 = ''
    message2 = ''
    if request.method == 'POST':
        set_session = request.form.get('set_session')
        get_session = request.form.get('get_session')
        clear_session = request.form.get('clear_session')
        set_cookie = request.form.get('set_cookie')
        get_cookie = request.form.get('get_cookie')
        clear_cookie = request.form.get('clear_cookie')

        # Session management
        if set_session:
            session['name1'] = 'Quang'
            session['pet1'] = 'chico'
            message1 = 'Session data set'
        elif get_session:
            if 'name1' in session.keys() and 'pet1' in session.keys():
                value1 = session['name1']
                value2 = session['pet1']
                message1 = f"[name1 : {value1}] , [pet1 : {value2}]"
            else:
                message1 = 'No session data found'
        elif clear_session:
            session.clear()
            message1 = 'Session cleared'

        # Cookie management
        elif set_cookie:
            response = make_response(render_template('session_cookie.html', message2 = 'Cookie set'))
            response.set_cookie(key='Wuthering Waves', value='2.6')
            return response
        elif get_cookie:
            if 'Wuthering Waves' in request.cookies:
                cookie_value = request.cookies['Wuthering Waves']
                message2 = f"Cookie value: {cookie_value}"
            else:
                message2 = 'No cookie found'
        elif clear_cookie:
            response = make_response(render_template('session_cookie.html', message2 = 'Cookie cleared'))
            response.set_cookie(key='Wuthering Waves', expires=0)
            return response

    return render_template('session_cookie.html', message1=message1, message2=message2)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Not recommended for credential storage in production
        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully', 'info')
    return redirect(url_for('home'))

#run the app and launch the server in debug mode. 
if __name__ == '__main__':
    app.run(debug=True)





