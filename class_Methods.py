"""

"""


class Pokemon:
    def __init__(self,name,hp,typ,level):
        self.name=name
        self.hp=hp
        self.typ=typ
        self.level=level
    
    def combat(self,other):
        if self.level>other.level:
            return f"{self.name} won!"
        elif self.level<other.level:
            return f"{other.name} has defeated you!"
        else:
            return f"{self.name} and {other.name} lose!"
        
    

    def __str__(self):
        return(f"""name: {self.name}
Type: {self.typ}
Level: {self.level}
HP: {self.hp}
""")
    
    #@classmethod used to keep method from changing object instances!
    def level_up(self):
        self.level+=1
        self.hp=int(self.hp*1.5)
    @classmethod
    def pikachu(self):
        return Pokemon(input("Mustard"),50,"electric",1)
    #Static methotoudsht do not require self or class
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5
    
        

    
eevee=Pokemon("JayRod", 37, "electric", 2)
charizard= Pokemon("Bob", 1, "fire", 36)
pika=Pokemon.pikachu()
pika.hp = Pokemon.hp_update(pika)
print(pika)

