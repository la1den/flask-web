from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

class User:
    def __init__(self,username,email) -> None:
        self.username = username
        self.email = email

@app.route("/variable")
def variable():
    hobby = "Game"
    user = User("Tom", "XX@qq.com")
    return render_template("variable.html", hobby=hobby, user=user)

@app.template_filter("dformat")
def datetime_format(value, format="%Y-%d-%m %H:%M"):
    return value.strftime(format)

@app.route("/if")
def if_statement():
    age = 19
    return render_template("if.html", age=age)

@app.route("/for")
def for_statement():
    books = [{
        "name": "Sanguo",
        "author": "Luo Guanzhong",
        "price": 100 },
        {
            "name": "ShuiHuZhuan",
            "author": "ShiNaian",
            "price": 99 }, ]
    return render_template("for.html",books=books)

