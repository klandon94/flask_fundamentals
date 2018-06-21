from flask import Flask, render_template,session,request,redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template('index.html')

# the server is listening for a POST request to:
# localhost:5000/users
# we define the route below such that the route matches the action of our form - '/users'
# similarly we need to allow specific methods - 'POST' in this case
@app.route('/users',methods=['POST'])
def create_user():
    print("\nGot Post Info")
    my_data = request.form
    print("Input data in dict form: ", my_data)
    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']

    # Here we add two properties to session to store the name and the email
    session['name'] = my_data['name']
    session['email'] = my_data['email']
    session['action'] = my_data['action']
    print('Name:', my_data['name'])
    print('Email:', my_data['email'])

    return redirect('/show') #Notice that we changed where we redirect to
    # Now we go to the page that displays the name and email

    #return redirect('created.html' name=name, email = email)

@app.route('/show')
def show_user():
    if session['action'] == 'register':
        print('ahhaah')
    return render_template('user.html')

if __name__ == "__main__":
    # run our server
    app.run(debug=True)

