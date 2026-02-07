import os
import json
import pytest
from library_system.book import Book
from library_system.member import Member
from library_system.library import Library

TEST_DATA_FILE = "test_library.json"

@pytest.fixture
def clean_library(tmp_path, monkeypatch):
    lib = Library()
    
    monkeypatch.setattr(lib, "DATA_FILE", tmp_path / TEST_DATA_FILE)
    
    return lib

def test_add_book_and_member(clean_library):
    lib = clean_library
    b = Book("Python 101", "Guido", "B1")
    m = Member("Suresh", "M1")
    
    lib.add_book(b)
    lib.add_member(m)
    
    assert "B1" in lib.books
    assert "M1" in lib.members

def test_borrow_and_return(clean_library):
    lib = clean_library
    b = Book("OOP", "Author", "B2")
    m = Member("Bob", "M2")
    
    lib.add_book(b)
    lib.add_member(m)
    
    res_borrow = lib.borrow_book("B2", "M2")
    assert "borrowed" in res_borrow.lower()
    assert lib.books["B2"].available == False
    
    res_return = lib.return_book("B2", "M2")
    assert "returned" in res_return.lower()
    assert lib.books["B2"].available == True

def test_search(clean_library):
    lib = clean_library
    b1 = Book("Learn Python", "Author", "B3")
    b2 = Book("Advanced Python", "Author", "B4")
    
    lib.add_book(b1)
    lib.add_book(b2)
    
    result = lib.search("Python")
    assert len(result) == 2
    assert any(book.isbn == "B3" for book in result)

def test_stats_empty(clean_library):
    lib = clean_library
    assert lib.stats() == (0, 0, 0, 0)
