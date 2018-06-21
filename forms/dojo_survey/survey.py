from flask import Flask, render_template,session,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    print('\n\nGOT POST INFO')
    my_data = request.form
    print("Input data in dict form: ", my_data)
    print(my_data['name'])
    return render_template('created.html')

@app.route('/danger')
def danger_zone():
    print ('\n\na user tried to visit /danger. we have redirected the user back to /')
    return redirect('/')

if __name__ == "__main__":
    # run our server
    app.run(debug=True)