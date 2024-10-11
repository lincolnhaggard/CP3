menu={
    "Drink":{"Coke":10.99,"Root beer without the root":5,"Bebsi":4.72},
    "Appetizer":{"Green":255,"Yellow":23.23,"Orange":8.00},
    "Main Course":{"Chicken salard":15.23,"Bime prib":32.4,"Road":0.25},
    "Side":{"Apple sus":5.6,"Spoon":3.45,"Laundry deterunt":7.5},
    "Second side":{"Apple sus":5.6,"Spoon":3.45,"Laundry deterunt":7.5},
    "Dessert":{"Sand":0.01,"Crab":14.5,"Scorpion":29.1}
}


class Ordor:
    def __init__(self):
        self.items=[]
        self.special=False
        for i in menu.keys():
            if i!="Second Side" or self.items[-1] in menu["Side"]:
                inp=input(f"\nWould you like a {i}: \n").lower()
                if inp=="yes":
                    print()
                    for k in menu[i].keys():
                        print(f"{k}:{menu[i][k]}",end=", ")
                    print("\n")
                    inp=input(f"What would you like: \n").lower().capitalize()
                    while not inp in menu[i].keys():
                        print("\nthat item is not available\n")
                        inp=input(f"\nWould you like a {i}: \n").lower()
                        if inp=="yes":
                            for k in menu[i].keys():
                                print(f"{k}:{menu[i][k]}",end=", ")
                            print("\n")
                            inp=input("What woud you like: \n").lower().capitalize()
                        else:
                            inp=""
                            break
                    self.items.append(inp)
                    done=True
                elif i=="Side":
                    self.items.append("")
                    self.items.append("")
                else:
                    self.items.append("")
    def __str__(self):
        toret=""
        menukeys=[]
        for i in menu.keys():
            menukeys.append(i)
        for x,i in enumerate(self.items):
            if i!="":
                toret+=f"{menukeys[x]}: {i}\n"
        toret+=f"Total:{Ordor.price(self.items,False)}\n"
        return toret
    
    def changeitem(self,item):
        for x,i in enumerate(menu.keys()):
            
            if item==i:
                for k in menu[i].keys():
                    print(f"{k}:{menu[i][k]}",end=", ")
                print()
                inp=input(f"What would you like to change your item to: \n").lower().capitalize()
                while not inp in menu[i].keys():
                    print("That item is not available\n")
                    for k in menu[i].keys():
                        print(f"{k}:{menu[i][k]}",end=", ")
                    print()
                    inp=input(f"What would you like to change your item to: \n")
                self.items[x]=inp
                break
        self.special=False
    def checkordor(self):
        self.items.remove("")
        if len(self.items)>0:
            return True
        else:
            return False
    @classmethod
    def specials(self):
        print("\nGreen Coke, Double spoon, prime bib\n")
        inp=input("What special would you like: \n").lower()
        if inp=="green coke":
            self.items=["Coke","Green","","","",""]
            self.special=True
        elif inp=="double spoon":
            self.items=["","","","Spoon","Spoon",""]
            self.special=True
        elif inp=="prime bib":
            self.items=["Bebsi","Red","Bime prib","","","Crab"]
            self.special=True
    @staticmethod
    def price(items,special):
        total=0.0
        for i in items:
            for k in menu.keys():
                if i in menu[k].keys():
                    total+=menu[k][i]
                    break

        total*=1.0485
        if special:
            total*=0.9
        total=round(total,2)
        return format(total,".2f")
    def viewordorlist(ordors):
        toret="\n\n-----\n"
        for x,i in enumerate(ordors):
            toret+=f"\nOrdor #{x+1}\n"+str(i)+"\n-----\n"
        return toret
"""
o=Ordor()
print(o)
print(Ordor.price(o.items))
print(o.checkordor())
print(o.checkordor())
"""
inp=input("Would you like to place an ordor?: \n").lower()
ordors=[]
while inp=="yes":
    ordors.append(Ordor())
    done=False
    while not done:
        print("1.View ordors\n2.Edit Ordor\n3.Place new ordor")
        inp=input("")
        if inp=="1":
            print(Ordor.viewordorlist(ordors))
        elif inp=="2":
            print(Ordor.viewordorlist(ordors))
            inp=int(input("Wich ordor would you like to edit: \n"))
            ordors[inp-1].changeitem(input(f"What item would you like to change?: \nDrink, Appetizer, Main Course, Side, Second Side, Desert\n").lower().capitalize())
        elif inp=="3":
            break
print("ok bye")