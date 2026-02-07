from library_system.member import Member

def test_member_creation():
    m = Member("Suresh", "M1")
    assert m.name == "Suresh"
    assert m.id == "M1"
    assert m.borrowed == []

def test_borrow_and_return_logic():
    m = Member("Bob", "M2")
    
    m.borrowed.append("ISBN1")
    assert "ISBN1" in m.borrowed
    
    m.borrowed.remove("ISBN1")
    assert "ISBN1" not in m.borrowed
