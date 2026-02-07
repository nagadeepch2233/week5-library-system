from library_system.book import Book
from library_system.member import Member
from library_system.library import Library

lib = Library()

print("\n=== LIBRARY MANAGEMENT SYSTEM ===")

while True:
    print("\n1.Add Book 2.Add Member 3.Borrow 4.Return 5.Stats 6.Exit")
    c = input("Choice: ")

    if c == "1":
        lib.add_book(Book(input("Title: "), input("Author: "), input("ISBN: ")))
    elif c == "2":
        lib.add_member(Member(input("Name: "), input("ID: ")))
    elif c == "3":
        print("Success" if lib.borrow_book(input("ISBN: "), input("Member ID: ")) else "Failed")
    elif c == "4":
        print("Success" if lib.return_book(input("ISBN: "), input("Member ID: ")) else "Failed")
    elif c == "5":
        t, a, b, m = lib.stats()
        print(f"Total:{t} Available:{a} Borrowed:{b} Members:{m}")
    elif c == "6":
        break
