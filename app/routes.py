# from app.forms import LoginForm ...
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
@app.route('/home')
def home():
    return render_template('home.html')