from flask import Flask, render_template,session,request,redirect,flash
import re
from datetime import datetime,date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    return render_template('registration_form.html')

@app.route('/create',methods=['POST'])
def create():
    errors = 0
    data = request.form
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    session['email'] = data['email']
    session['password'] = data['password']
    session['confirm_password'] = data['confirm_password']
    session['birthday'] = data['birthday']

    if not data['first_name']:
        flash(u'Please enter your first name','error')
        errors += 1
    elif not data['first_name'].isalpha():
        flash(u'First name must not contain any numbers', 'invalid')
        errors += 1
    
    if not data['last_name']:
        flash(u'Please enter your last name','error')
        errors += 1
    elif not data['last_name'].isalpha():
        flash(u'Last name must not contain any numbers','invalid')
        errors += 1

    if not data['email']:
        flash(u'Please enter your email address','error')
        errors += 1
    elif not EMAIL_REGEX.match(data['email']):
        flash(u'Invalid email address','invalid')
        errors += 1

    if not data['password']:
        flash(u'Please enter a password','error')
        errors += 1
    elif len(data['password']) <= 8:
        flash(u'Password must be greater than 8 characters', 'invalid')
        errors += 1
    elif not (any(x.isupper() for x in data['password'])) or not (any(x.isdigit() for x in data['password'])):
        flash(u'Password must contain at least 1 number and 1 uppercase letter', 'invalid')
        errors += 1
    elif not data['confirm_password']:
        flash(u'Please confirm your password','error')
        errors += 1
    elif data['confirm_password'] != data['password']:
        flash(u'Passwords do not match', 'invalid')
        errors += 1

    if not data['birthday']:
        flash(u'Please enter your birth date','error')
        errors += 1
    elif datetime.strptime(data['birthday'],'%m/%d/%Y').strftime('%Y/%m/%d') > date.today().strftime('%Y/%m/%d'):
        flash(u'Birth date must be from the past', 'invalid')
        errors += 1

    if errors == 0:
        flash(u'Thanks for submitting your information!','message')
    
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)