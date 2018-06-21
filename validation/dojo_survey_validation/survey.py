from flask import Flask, render_template,session,request,redirect,flash

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'location' not in session:
        session['location'] = 'Select location'
    if 'language' not in session:
        session['language'] = 'Select language'
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_user():
    my_data = request.form
    session['name'] = my_data['name']
    session['location'] = my_data['location']
    session['language'] = my_data['language']
    session['comments'] = my_data['comments']
    if my_data['name'] and my_data['comments'] and len(my_data['comments']) < 120:
        return redirect('/results')
    if not my_data['name']:
        flash('A name must be provided')
    if not my_data['comments']:
        flash('A comment must be provided')
    if len(my_data['comments']) > 120:
        flash(f"Comments must not exceed 120 characters. Current num of chars: {len(my_data['comments'])}")
    return redirect('/')

@app.route('/results')
def results():
    return render_template('created.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    # run our server
    app.run(debug=True)