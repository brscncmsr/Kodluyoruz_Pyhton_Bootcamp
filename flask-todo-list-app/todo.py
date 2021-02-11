from flask import Flask,render_template,request,session,redirect,url_for,logging
from flask_sqlalchemy import SQLAlchemy
import time
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Baris/Desktop/to_do/todo.db'
db = SQLAlchemy(app)
app.secret_key = '\x87\xe2\xaa\x88\xb8\xa6\x0f\xe7\xa8\x97'


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


@app.route("/",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        session["username"] = request.form["uname"]


        
        singup = user.query.filter_by(username=uname, password=passw).first()
        if singup is not None:
            return redirect(url_for("index"))
        else:
            return render_template("login_failed.html")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    global uname
    if request.method == "POST":
        uname = request.form['uname']
        passw = request.form['passw']

        register = user(username = uname, password = passw)

        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

class Todo(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)
    username = db.Column(db.String(80))
    
#--------------------------------------------

@app.route("/index")
def index():
    todolist=Todo.query.filter_by(username=session["username"]).all()
    todolist1 = Todo.query.filter_by(username=session["username"]).first()
    
    
    
    return render_template("index.html",todolist1=todolist1,todolist=todolist)
@app.route("/add",methods=["POST"])
def addTodo():
    title =request.form.get("title")
    content=request.form.get("content")
    newTodo =Todo(title=title,content=content,complete=False,username=session["username"])
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/complete/<string:id>")
def completeTodo(id):
    value = request.form.getlist('check') 
    todo=Todo.query.filter_by(id=id).first()
    if (todo.complete==False):
        todo.complete = True
    else:
        todo.complete = False
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/detail/<string:id>")
def detailTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template("detail.html",todo = todo)

#--------------------------------------------

if __name__ == "__main__":
    app.run(debug=True,port=2727)

