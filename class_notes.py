"""
notes
we start classes with keyword class and we name them usinc PascalCase
"""


class Animal:
    #We start with constructor(defines the attributes)
    def __init__(self,name,species,age,gender,rarity):
        self.name=name
        self.species=species
        self.age=age
        self.gender=gender
        self.rarity=rarity
        self.losses=0

    #Methods are functions inside of the class
    def fight(self,other):
        if len(self.name)>len(other.name):
            other.losses+=1
            return self.name
        elif len(self.name)<len(other.name):
            self.losses+=1
            return other.name
        else:
            self.losses+=1
            other.losses+=1
            return "Tie"
    
    #Makes a more readable string when printing it
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nSpecies: {self.species}\nGender: {self.gender}\nRarity: {self.rarity}"
    


#WE generaly stro objects in variables (individually or in a list) so we can use it later
cat=Animal("Tom","cat",21,"Male","Common")
frog=Animal("Jarrod","Posion Dart Frog",500, "Female","Rare")


#To call a method you put the name of the object, then we use . name of the method and in () any parrameters
print(cat.fight(frog))



cat.name="Thomas"
print(cat.losses)


print(cat.fight(frog))
print(cat.losses)
print(frog.losses)


cat=None
print(cat)