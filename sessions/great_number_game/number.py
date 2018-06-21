from flask import Flask, render_template,session,request,redirect,flash
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'holy' not in session and 'result' not in session:
        rando = random.randrange(0,100)
        session['holy'] = rando
        session['result'] = ''
        print(session['holy'])
    return render_template('number.html')

@app.route('/numbers',methods=['POST'])
def get_number():
    if not request.form['num']:
        flash('Must enter a number!')
        return redirect('/')
    session['num'] = int(request.form['num'])
    if session['num'] < session['holy']:
        session['result'] = 'less'
    elif session['num'] > session['holy']:
        session['result'] = 'greater'
    elif session['num'] == session['holy']:
        session['result'] = 'equal'
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    # run our server
    app.run(debug=True)