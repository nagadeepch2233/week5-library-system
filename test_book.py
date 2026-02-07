import pytest
from library_system.book import Book
from datetime import datetime, timedelta

def test_borrow_sets_availability_and_due():
    b = Book("Test Book", "Author", "ISBN1")
    
    assert b.available == True
    assert b.due is None
    
    b.borrow()
    
    assert b.available == False
    assert isinstance(b.due, str)
    due_date = datetime.strptime(b.due, "%Y-%m-%d")
    assert due_date.date() == (datetime.now().date() + timedelta(days=14))

def test_return_book_resets_status():
    b = Book("Test Book", "Author", "ISBN1")
    b.borrow()
    b.return_book()
    assert b.available == True
    assert b.due is None
