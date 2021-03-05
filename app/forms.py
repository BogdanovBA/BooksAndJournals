from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length
from .models import User, Journal, Book
from flask_login import current_user

