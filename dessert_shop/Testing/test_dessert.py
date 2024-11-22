from desserts import (
    Candy,
    Cookie,
    IceCream,
    Sundae,
    Order
)

def test_candy():
    test_candy=Candy("Pepermint Candy",10.0,6.25)
    assert test_candy.name=="Pepermint Candy"
    assert test_candy.candy_weight==10.0
    assert test_candy.price_per_pound==6.25

def test_cookie():
    test_Cookie=Cookie("Vannila Swirl Chocolate Chip Cookie",23,6.10)
    assert test_Cookie.name=="Vannila Swirl Chocolate Chip Cookie"
    assert test_Cookie.cookie_quantity==23
    assert test_Cookie.price_per_dozen==6.1

def test_icecream():
    test_IceCream=IceCream("Double Mint IceCream",2,10.99)
    assert test_IceCream.name=="Double Mint IceCream"
    assert test_IceCream.scoop_count==2
    assert test_IceCream.price_per_scoop==10.99

def test_sundae():
    test_Sundae=Sundae("Strawberry Explosion Sundae",1,11.99,"Orange Flavoured Chocolate",2.99)
    assert test_Sundae.name=="Strawberry Explosion Sundae"
    assert test_Sundae.scoop_count==1
    assert test_Sundae.price_per_scoop==11.99
    assert test_Sundae.topping_name=="Orange Flavoured Chocolate"
    assert test_Sundae.topping_price==2.99

def test_ordor():
    test_Ordor=Order()
    test_Ordor.add(Candy("Pepermint Candy",10.0,6.25))
    assert test_Ordor.ordor[0].name=="Pepermint Candy"
    test_Ordor.add("Squigles")
    assert len(test_Ordor)==1

def test_tax_percent():
    test_candy=Candy("Purple and black gumdrops",100.5,0.25)
    assert test_candy.tax_percent==7.25

