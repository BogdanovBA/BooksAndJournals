from app.forms import RegistrationForm, LoginForm
from flask import redirect, url_for, request, render_template, flash
from app import app, db
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, Book, Journal
from werkzeug.urls import url_parse
import secrets
import os


def save_picture(form_picture):
    random_hex = secrets.token_hex(8) 
    file_ext = form_picture.filename.split('.')[-1]
    picture_filename = random_hex + "." +  file_ext
    picture_path = os.path.join(app.root_path, 'static/media/' , picture_filename)
    form_picture.save(picture_path)

    return picture_filename


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if request.method == 'POST' and not form.validate():
        flash('Invalid credentials. Try again.')
        return redirect(url_for('register'))
    if request.method == 'POST' and form.validate():
        user = User(
            username = form.username.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            age = form.age.data,
            email = form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid credentials. Try again.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        flash(f'Successfully logged in as { user.username }', 'success')

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('home')
        return redirect(next_page)
    
    return render_template('login.html', form=form)