from flask import Flask,render_template as render 

app = Flask(__name__)

@app.route('/')
@app.route('/<x>/<y>')
def board(x=8,y=8):
    return render('board.html', num1=int(x), num2=int(y))


if __name__ == "__main__":
    app.run(debug=True)