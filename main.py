from app import app, db
from app.models import User, Book, Journal

@app.shell_context_processor
def make_shell_context():
    return {
        'db' : db, 
        'app' : app,
        'User' : User,
        'Book' : Book,
        'Journal' : Journal,
    }