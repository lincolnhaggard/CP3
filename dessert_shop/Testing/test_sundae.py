from dessert_shop.desserts import Cookie

def test_calculate_cost():
    test_cookie=Cookie("Purple and black mix",12,5,"Black and purple sprinkles",0.25)
    assert test_cookie.calculate_cost()==60.25

def test_calculate_tax():
    test_cookie=Cookie("Purple and black mix",12,5,"Black and purple sprinkles",0.25)
    assert test_cookie.calculate_tax()==4.368125