from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

HOSTNAME = "localhost"
PORT = 3306
USERNAME = "lfh"
PASSWORD = "123456"
DATABASE = "database_learn"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)
migrate = Migrate(app,db)
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone())

@app.route('/')
def index():
    return render_template("index.html")

# class User:
#     def __init__(self,username,email) -> None:
#         self.username = username
#         self.email = email

# @app.route("/variable")
# def variable():
#     hobby = "Game"
#     user = User("Tom", "XX@qq.com")
#     return render_template("variable.html", hobby=hobby, user=user)

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

class Userx(db.Model):
    __tablename__ = "user_x"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# user = Userx(username="Zhang San", password="123123")

# with app.app_context():
#     db.create_all()


@app.route("/user/add")
def add_user():
    user = Userx(username="Zhang San", password="123123")
    db.session.add(user)
    db.session.commit()
    return "Created successfully"

@app.route("/user/query")
def query_user():
    user = Userx.query.get(1)
    print(f"{user.id}: {user.username} - {user.password}")
    users = Userx.query.filter_by(username="Zhang San")
    print(type(users))
    return "Data successfully searched"


@app.route("/user/update")
def update_user():
    user = Userx.query.filter_by(username="Zhang San").first()
    user.password = "123abc"
    db.session.commit()
    return "Successfully updated"


@app.route("/user/delete")
def delete_user():
    user = Userx.query.filter_by(username="Zhang San").first()
    db.session.delete(user)
    db.session.commit()
    return "Successfully deleted"

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


