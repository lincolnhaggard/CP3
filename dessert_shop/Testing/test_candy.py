from desserts import Candy

def test_calculate_cost():
    test_cookie=Candy("Purple and black gumdrops",12,5)
    assert test_cookie.calculate_cost()==60.0

def test_calculate_tax():
    test_cookie=Candy("Purple and black gumdrops",12,5)
    assert test_cookie.calculate_tax()==4.35