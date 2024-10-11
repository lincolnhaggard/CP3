menu={
    "Drink":{"Coke":10.99,"Root beer without the root":5,"Bebsi":4.72},
    "Appetizer":{"Green":255,"Yellow":23.23,"Orange":8.00},
    "Main Course":{"Chicken salard":15.23,"Bime prib":32.4,"Road":0.25},
    "Side":{"Apple sus":5.6,"Spoon":3.45,"Laundry deterunt":7.5},
    "Second Side":{"Apple sus":5.6,"Spoon":3.45,"Laundry deterunt":7.5},
    "Dessert":{"Sand":0.01,"Crab":14.5,"Scorpion":29.1}
}


class Ordor:
    def __init__(self):
        self.items=[]
        done=False
        while not done:
            for i in menu.keys():
                if i!="Second Side" or self.items[-1] in menu["Side"]:
                    inp=input(f"Would you like a {i}: ").lower()
                    if inp=="yes":
                        for k in menu[i].keys():
                            print(f"{k}:{menu[i][k]}",end=", ")
                        print()
                        inp=input(f"What would you like: ").lower().capitalize()
                        while not inp in menu[i].keys():
                            print("that item is not available")
                            for k in menu[i].keys():
                                print(f"{k}:{menu[i][k]}",end=", ")
                            print()
                            inp=input("What woud you like: ").lower().capitalize()
                        self.items.append(inp)
                        done=True
                    elif i=="Side":
                        self.items.append("")
                        self.items.append("")
                    else:
                        self.items.append("")
            if not done:
                print("you didn't ordor anything")
                print("try again")
                self.items=[]
    def __str__(self):
        toret=""
        menukeys=[]
        for i in menu.keys():
            menukeys.append(i)
        for x,i in enumerate(self.items):
            if i!="":
                toret+=f"{menukeys[x]}: {i}\n"
        return toret
    def price(self):
        total=0.0
        for i in self.items:
            for k in menu.keys():
                if i in menu[k].keys():
                    total+=menu[k][i]
                    break

        total*=1.0485
        total=round(total,2)
        return total
    def changeitem(self,item):
        for i in menu.keys():
            ismenu=None
            for k in self.items:
                if k in menu[i].keys():
                    ismenu=k
o=Ordor()
print(o)
print(o.price())