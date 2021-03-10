from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField, FloatField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Length, Email
from .models import User, Journal, Book
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    age = StringField('Your age', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('User with that username already exists.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('User with that email adress already exists.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me?')
    submit = SubmitField('Log in')


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    submit = SubmitField('Create')


class JournalForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    editor = StringField('Editor', validators=[DataRequired()])
    page_amount = StringField('Page amount', validators=[DataRequired()])
    submit = SubmitField('Create')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    picture = FileField(label='Account avatar', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'svg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class UpdateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired()])
    picture = FileField(label='Book cover', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'svg'])])
    submit = SubmitField('Update')


class UpdateJournalForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    editor = StringField('Editor', validators=[DataRequired()])
    page_amount = StringField('Page amount', validators=[DataRequired()])
    picture = FileField(label='Journal cover', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'svg'])])
    submit = SubmitField('Update')