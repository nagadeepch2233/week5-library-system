
from datetime import datetime, timedelta

LOAN_DAYS = 14

class Book:
    def __init__(self, title, author, isbn, available=True, due=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.due = due

    def borrow(self):
        self.available = False
        self.due = (datetime.now() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")

    def return_book(self):
        self.available = True
        self.due = None
