import json
from .book import Book
from .member import Member

BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load()

    def add_book(self, book):
        self.books[book.isbn] = book
        self.save()

    def add_member(self, member):
        self.members[member.id] = member
        self.save()

    def borrow_book(self, isbn, member_id):
        b = self.books.get(isbn)
        m = self.members.get(member_id)
        if b and m and b.available:
            b.borrow()
            m.borrowed.append(isbn)
            self.save()
            return True
        return False

    def return_book(self, isbn, member_id):
        b = self.books.get(isbn)
        m = self.members.get(member_id)
        if b and m and isbn in m.borrowed:
            b.return_book()
            m.borrowed.remove(isbn)
            self.save()
            return True
        return False

    def stats(self):
        total = len(self.books)
        available = sum(b.available for b in self.books.values())
        return total, available, total - available, len(self.members)

    def save(self):
        with open(BOOKS_FILE, "w") as f:
            json.dump({k: b.__dict__ for k, b in self.books.items()}, f, indent=4)
        with open(MEMBERS_FILE, "w") as f:
            json.dump({k: m.__dict__ for k, m in self.members.items()}, f, indent=4)

    def load(self):
        try:
            with open(BOOKS_FILE) as f:
                self.books = {k: Book(**v) for k, v in json.load(f).items()}
            with open(MEMBERS_FILE) as f:
                self.members = {k: Member(v["name"], v["id"]) for k, v in json.load(f).items()}
        except:
            pass
