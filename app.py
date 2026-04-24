from flask import Flask, render_template, request, redirect, session, make_response
from miscellaneous.states import us_states
import random
import pandas as pd

app = Flask(__name__, static_folder='static', static_url_path= '/', template_folder='templates')
app.secret_key = '1st application development'

@app.route('/', methods=['GET','POST'])
def home():
    yourname = ''
    if request.method == 'POST':
        yourname = request.form.get('yourname')
    return render_template('home.html', message= yourname)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/state_abbreviation', methods=['GET','POST'])
def state_abbreviation():
    full_state_name = ''
    abbreviation = ''
    if request.method == 'POST':
        abbreviation = request.form.get('state_abbreviation')
        full_state_name = us_states[abbreviation]
    return render_template('state_abbreviation.html', us_states=us_states, full_state_name=full_state_name, abbreviation=abbreviation)

@app.route('/calculator',methods=['GET','POST'])
def calculator():
    result =''
    first_number = ''
    second_number = ''  
    operator = ''
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
        else:
            if float(second_number) == 0:
                result = "Error - Cannot divide by zero"
            else:
                result = float(first_number) / float(second_number)
       
    return render_template('calculator.html',result=result,first_number=first_number,second_number=second_number,operator=operator)

@app.route('/guess_number', methods=['GET','POST'])
def guess_number():
    level = ''
    attempts = '' 
    target = '' 
    result = '' 
    guess = '' 
    count = ''
    if request.method == 'POST':
        level = int(request.form.get('level'))
        attempts = int(request.form.get('attempts'))
        guess = int(request.form.get('guess', 0))
        count = int(request.form.get('count', 0))
        target = int(request.form.get('target',0))

        if not target:
            if level == 1:
                target = random.randint(1, 9)
            elif level == 2:
                target = random.randint(10, 99)
            else:
                target = random.randint(100, 999)

        if guess:
            if count < attempts:
                if guess == target:
                    result = "Congratulations! You guessed the number."
                else:                  
                    result = "Sorry, that's not the correct number. Try again."
                    count += 1
            if count >= attempts:
                result = f"Out of attempts - the number was {target}."

    return render_template('guess_number.html', level=level, result=result, attempts=attempts, guess=guess, count=count, target=target)

@app.route('/excel_upload', methods=['GET', 'POST'])
def excel_upload():
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
    return render_template('text_transformation.html', input_text=input_text, result=result)

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

if __name__ == '__main__':
    app.run(debug=True)





