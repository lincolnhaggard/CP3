from desserts import Cookie

def test_calculate_cost():
    test_cookie=Cookie("Purple and black mix",12,5)
    assert test_cookie.calculate_cost()==60.0

def test_calculate_tax():
    test_cookie=Cookie("Purple and black mix",12,5)
    assert test_cookie.calculate_tax()==4.35