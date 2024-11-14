from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self,name):
        self.name=name
        self.tax_percent=7.25

    def __str__(self):
        return self.name
    
    def calculate_tax(self):
        return self.calculate_cost()*self.tax_percent/100

    @abstractmethod
    def calculate_cost(self):
        pass

class Candy(DessertItem):
    def __init__(self,name,candy_weight,price_per_pound):
        super().__init__(name)#Pass up to DessertItem
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound

    def calculate_cost(self):
        return self.price_per_pound*self.candy_weight

class Cookie(DessertItem):
    def __init__(self,name,cookie_quantity,price_per_dozen):
        super().__init__(name)#Pass up to DessertItem
        self.cookie_quantity=cookie_quantity
        self.price_per_dozen=price_per_dozen

    def calculate_cost(self):
        return self.cookie_quantity/12*self.price_per_dozen

class IceCream(DessertItem):
    def __init__(self,name,scoop_count,price_per_scoop):
        super().__init__(name)#Pass up to DessertItem
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop

    def calculate_cost(self):
        return self.scoop_count*self.price_per_scoop

class Sundae(IceCream):
    def __init__(self,name,scoop_count,price_per_scoop,topping_name,topping_price):
        super().__init__(name,scoop_count,price_per_scoop)#Pass up to IceCream class
        self.topping_name=topping_name
        self.topping_price=topping_price
    
    def calculate_cost(self):
        return super().calculate_cost()+(self.topping_price)

class Order:
    def __init__(self):
        self.ordor=[]

    def add(self,item):
        if isinstance(item,DessertItem):
            self.ordor.append(item)
    
    def __len__(self):
        return len(self.ordor)

    def ordor_cost(self):
        total=0
        for item in self.ordor:
            total+=item.calculate_cost()
        return total
    
    def ordor_tax(self):
        total_tax=0
        for item in self.ordor:
            total_tax+=item.calculate_tax()
        return total_tax



