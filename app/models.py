from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id:int):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # идентификатор юзера
    username = db.Column(db.String(64), index=True, unique=True) # никнейм
    first_name = db.Column(db.String(100)) # имя (полностью)
    last_name = db.Column(db.String(100)) # фамилия (полностью)
    age = db.Column(db.Integer) # возраст (целых лет)
    email = db.Column(db.String(120), index=True, unique=True) # адрес электронной почты
    password_hash = db.Column(db.String(128)) # захешированный пароль
    books = db.relationship('Book', backref='book_owner', lazy='dynamic') # поле доступа из модели Book
    journals = db.relationship('Journal', backref='journal_owner', lazy='dynamic') # поле доступа из модели Journal
    image_file = db.Column(db.String(20), nullable=False, default='defaultuser.png')

    def __rep__(self):
        return f'<User [username={self.username}, email={self.email}]>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return  check_password_hash(self.password_hash, password)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True) # идентификатор книги
    created = db.Column(db.DateTime, index=True, default=datetime.now) # дата/время создания книги на сервисе
    title = db.Column(db.String(150)) # название книги
    author = db.Column(db.String(200)) # автор книги (тот, кто ее написал)
    rating = db.Column(db.Integer) # рейтинг книги
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # собственник книги (тот, кто разместил на сервисе)
    image_file = db.Column(db.String(20), nullable=False, default='defaultbook.png')

    def __rep__(self):
        return f'<Book [title={self.title}, author={self.author}]>'


class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True) # идентификатор журнала
    created = db.Column(db.DateTime, index=True, default=datetime.now) # # дата/время создания журнала на сервисе
    title = db.Column(db.String(150)) # название журнала
    editor = db.Column(db.String(200)) # редактор журнала
    page_amount = db.Column(db.Integer) # количество страниц
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # cобственник (тот,кто разместил журнал на сервисе)
    image_file = db.Column(db.String(20), nullable=False, default='defaultjournal.png')

    def __repr__(self):
        return f'<Journal [title={self.title}, editor={self.author}]>'