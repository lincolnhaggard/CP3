class Tech:
    def __init__(self,name,storage):
        self.name=name
        self.storage=storage

class Phone(Tech):
    def __init__(self,name,storage,color):
        super().__init__(name,storage)
        self.color=color

    def __str__(self):
        return f"A {self.color} {self.name} with {self.storage}GB of storage"

    def __repr__(self):
        return f"Phone({self.name}, {self.storage}, {self.color})"

class Laptop(Tech):
    def __init__(self,name,storage,size):
        super().__init__(name,storage)
        self.size=size

    def __str__(self):
        return f"{self.size}-inch {self.name} with {self.storage}GB of storage"
    
    def __repr__(self):
        return f"Laptop({self.name}, {self.storage}, {self.size})"