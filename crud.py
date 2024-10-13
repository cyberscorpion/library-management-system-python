from models import Book, Member, Transaction
from database import session

def add_book(title, author, isbn, count):
    book = Book(title=title, author=author, isbn=isbn, count=count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()

def add_member(name, email):
    member = Member(name = name, email = email)
    session.add(member)
    session.commit()