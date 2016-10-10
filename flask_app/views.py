import datetime
from flask import render_template, flash, redirect, url_for, request

from flask_app import app, db
from .forms import TodoForm
from .models import Todo

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = TodoForm()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        detail = form.detail.data
        timestamp = datetime.datetime.utcnow()
        todo = Todo(title=title, detail=detail, timestamp=timestamp)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('register'))

    todo_list = Todo.query.order_by(Todo.timestamp.desc())
    return render_template('register.html',
                           form=form,
                           todo_list=todo_list)