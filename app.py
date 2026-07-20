from flask import Flask, render_template, request, redirect
from config import Config
from models import db, Todo

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():

    todos = Todo.query.order_by(Todo.created_at.desc()).all()

    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():

    title = request.form.get("title")

    if title:

        todo = Todo(title=title)

        db.session.add(todo)

        db.session.commit()

    return redirect("/")


@app.route("/complete/<int:id>")
def complete(id):

    todo = Todo.query.get_or_404(id)

    todo.completed = not todo.completed

    db.session.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)

    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)