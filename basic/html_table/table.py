from flask import Flask,render_template as render 

app = Flask(__name__)

@app.route('/')
def table():
    users = (
        {'first_name': 'LeBron','last_name':'James'},
        {'first_name': 'Kobe','last_name':'Bryant'},
        {'first_name': 'Michael','last_name':'Jordan'},
        {'first_name': 'Tim','last_name':'Duncan'}
    )
    return render('table.html', data=users)

if __name__ == "__main__":
    app.run(debug=True)