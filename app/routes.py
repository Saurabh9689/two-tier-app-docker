from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    
    users = User.query.all()
    return render_template('index.html', users=users)

