from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

HOSTNAME = "localhost"
PORT = 3306
USERNAME = "lfh"
PASSWORD = "123456"
DATABASE = "database_learn"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)


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



@app.route("/mysql")
def mysql_connect_test():

    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())

    return "Mysql Connect testing..." 
