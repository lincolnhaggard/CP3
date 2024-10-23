from class_notes import Animal

def test_get_name():
    testanimal = Animal("Bob","bobcat",27, "Male", "Epic")
    name = testanimal.get_name()
    assert name == "Bob"