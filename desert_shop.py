
class DessertItem:
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return self.name

class Candy(DessertItem):
    def __init__(self,name,candy_weight,price_per_pound):
        super().__init__(name)#Pass up to DessertItem
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound

class Cookie(DessertItem):
    def __init__(self,name,cookie_quantity,price_per_dozen):
        super().__init__(name)#Pass up to DessertItem
        self.cookie_quantity=cookie_quantity
        self.price_per_dozen=price_per_dozen

class IceCream(DessertItem):
    def __init__(self,name,scoop_count,price_per_scoop):
        super().__init__(name)#Pass up to DessertItem
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop

class Sundae(IceCream):
    def __init__(self,name,scoop_count,price_per_scoop,topping_name,topping_price):
        super().__init__(name,scoop_count,price_per_scoop)#Pass up to IceCream class
        self.topping_name=topping_name
        self.topping_price=topping_price


