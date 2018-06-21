from flask import Flask, render_template as render

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render("index.html")
@app.route('/success')
def success():
    return "<h1>success</h1>\n" * 50
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello "+name
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)