
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

class Order:
    def __init__(self):
        self.ordor=[]

    def add(self,item):
        if isinstance(item,DessertItem):
            self.ordor.append(item)
    
    def __len__(self):
        return len(self.ordor)

def main():
    ordor=Order()
    ordor.add(Candy("Candy Corn", 1.5, .25))
    ordor.add(Candy("Gummy Bears", .25, .35))
    ordor.add(Cookie("Chocolate Chip", 6, 3.99))
    ordor.add(IceCream("Pistachio", 2, .79))
    ordor.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    ordor.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in ordor.ordor:
        print(item)
    print("Total number of items in ordor:",len(ordor))

main()