class PetStore:
    name = "Pet Smart"
    def __init__(self, id_number):
        self.id_number=id_number
        self.animals = []
        self.featured_pet = None
        
    def add_pet(self,animal):
        assert isinstance(animal, Animal) #is instance checks if it is an instance of the class animal
        self.animals.append(animal)  #assert ends the function if the next if false

    def remove_pet(self, animal):
        try:
            self.animals.remove(animal)
        except:
            print("No aminal")
        else:
            print(animal, "removed")

    def feature(self,name):
        for pet in self.animals:
            if pet.name==name:
                self.featured_pet = pet
                print("Featured pet. . .",pet)
                break
        else:
            print("There is no such pet")
    
    def get_featured(self):
        return self.featured_pet
    
    def feed(self):
        for pet in self.animals:
            pet.eat()
    
    def get_mammals(self):
        return self.get_by_type(Mammal)
    
    def get_reptiles(self):
        return self.get_by_type(Reptile)
    
    def get_birds(self):
        return self.get_by_type(Bird)
    
    def get_amphibian(self):
        return self.get_by_type(Amphibian)
    
    def get_fish(self):
        return self.get_by_type(Fish)
    
    def get_by_type(self,typ):
        return [pet for pet in self.animals if isinstance(pet,typ)]
    

class Animal:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"This is {self.name}"
    def eat(self):
        print(self.name, "is eating", self.diet)
    def __lt__(self, other):
        return self.name<other.name

class Mammal(Animal):
    pass

class Cat(Mammal):
    def __init__(self,name,diet):
        super().__init__(name)
        self.diet = diet
    diet = "mice"

class Dog(Mammal):
    diet = "kibble"

class Reptile(Animal):
    pass

class Snake(Reptile):
    diet = "rodents"

class Turtle(Reptile):
    diet = "carrot"

class Bird(Animal):
    pass

class Parakeet(Bird):
    diet = "seeds"

class Tokan(Bird):
    diet = "catipilar"

class Amphibian(Animal):
    pass

class Frog(Amphibian):
    diet = "flies"

class Newt(Amphibian):
    diet = "worms"

class Fish(Animal):
    pass

class Koi(Fish):
    diet = "algae"

class Guppy(Fish):
    diet = "flakes"
print(dir(Turtle))
store = PetStore(1)
shelly = Turtle("Shelly")
flash = Turtle("Flash")
robin = Snake("Robin")
pets = [shelly,flash,robin]
store.add_pet(shelly)
store.add_pet(Cat("Joe",'gun'))
store.add_pet(flash)
store.add_pet(robin)
pets.sort()
for pet in pets:
    print(pet)
store.feature("Flash")
store.feed()

print("Reptiles: ")
for pet in store.get_reptiles():
    print(pet)