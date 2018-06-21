from flask import Flask, render_template,session,request,redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1 
    print(session)
    return render_template('counter.html')

@app.route('/addonemore')
def addAnother():
    session['counter'] += 1
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.clear()
    session['counter'] = 0 # If this line isn't added, repeatedly doing /destroy_session will go back and forth between 1 and 2
    return redirect('/')

@app.route('/resetvisits')
def reset():
    session['counter'] = 0
    return redirect('/')

if __name__ == "__main__":
    # run our server
    app.run(debug=True)