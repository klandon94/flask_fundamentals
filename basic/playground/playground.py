from flask import Flask, render_template as render 

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<number>')
@app.route('/play/<number>/<newcolor>')
def play(number = 3, color = 'lightblue'):
    return render('playground.html', num=int(number), newcolor=color)


if __name__ == "__main__":
    app.run(debug=True)