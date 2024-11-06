import csv
class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def __str__(self):
        return f"{self.name} is a {self.breed}"
dogs=[
]

with open('dog_practices/dogs.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        if lines[0]!="DogName":
            dogs.append(Dog(lines[0],lines[1]))

for i in dogs:
    print(i)