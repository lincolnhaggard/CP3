import random
import math

class Monster:
    def __init__(self,name,biome):
        self.name=name
        self.biome=biome
    def __str__(self):
        return self.name
    def attack(self,other):
        pass
    def breed(self,other):
        if isinstance(Arachnid):
            newmonster=Arachnid(self.name[:math.floor(len(self.name)/2)]+other.name[math.floor(len(self.name)/2):],random.choice((self.biome,other.biome)))
        if isinstance(Reptile):
            newmonster=Reptile(self.name[:math.floor(len(self.name)/2)]+other.name[math.floor(len(self.name)/2):],random.choice((self.biome,other.biome)))
        if isinstance(Mammal):
            newmonster=Mammal(self.name[:math.floor(len(self.name)/2)]+other.name[math.floor(len(self.name)/2):],random.choice((self.biome,other.biome)))
        if isinstance(Slime):
            newmonster=Slime(self.name[:math.floor(len(self.name)/2)]+other.name[math.floor(len(self.name)/2):],random.choice((self.biome,other.biome)))
        newmonster.speedstat=random.choice((self.speedstat,other.speedstat))+random.randint(-1,1)
        newmonster.attackstat=random.choice((self.attackstat,other.attackstat))+random.randint(-1,1)
        newmonster.healthstat=random.choice((self.healthstat,other.healthstat))+random.randint(-1,1)
        newmonster.health=newmonster.healthstat

class Arachnid(Monster):
    speedstat=random.randint(7,10)
    attackstat=random.randint(3,6)
    healthstat=random.randint(1,4)
    health=healthstat
    def attack(self,other):
        for i in range(math.floor(self.speedstat/3)):
            other.health-=math.floor(self.attackstat/2)

class Reptile(Monster):
    speedstat=random.randint(1,4)
    attackstat=random.randint(7,10)
    healthstat=random.randint(3,6)
    health=healthstat
    def attack(self,other):
        other.health-=self.attackstat

class Mammal(Monster):
    speedstat=random.randint(2,5)
    attackstat=random.randint(2,5)
    healthstat=random.randint(7,10)
    health=healthstat
    def attack(self,other):
        for i in range(self.attackstat):
            other.health-=math.ceil(random.randint(1,3)/2)

class Slime(Monster):
    speedstat=random.randint(1,4)
    attackstat=random.randint(5,8)
    healthstat=random.randint(5,8)
    health=healthstat
    def attack(self,other):
        if self.healthstat>4:
            self.healthstat-=1
            other.health-=math.floor(self.attackstat*1.5)
        elif self.healthstat<4:
            self.healthstat+=1
        else:
            other.health-=self.attackstat

contestants=[
    Arachnid("JimJam","Desert"),
    Reptile("Grog","Plains"),
    Mammal("Erender","Jungle"),
    Slime("Yttppbur","Arctic"),
    Arachnid("GopTom","Desert"),
    Reptile("Vroc","Ocean"),
    Mammal("Xom","Forest"),
    Slime("WopQuap","River")
]

while True:
    number=math.floor(math.log(len(contestants),2))-1
    for i in range(number):
        counter=0
        for k in range(2**(number-i)):
            while contestants[counter].health>0 and contestants[counter+1].health>0:
                if contestants[counter].speedstat>=contestants[counter+1].speedstat:
                    contestants[counter].attack(contestants[counter+1])
                    if contestants[counter+1].health<0:
                        contestants[counter+1].attack(contestants[counter])
                else:
                    contestants[counter+1].attack(contestants[counter])
                    if contestants[counter].health<0:
                        contestants[counter].attack(contestants[counter+1])
            
            if contestants[counter+1].health<0:
                contestants.pop(counter+1)
                print(contestants[counter],"has defeated",contestants[counter+1])
            else:
                contestants.pop(counter)
                print(contestants[counter+1],"has defeated",contestants[counter])
            toret=""
            for k in contestants:
                toret+=str(k)+" , "
            print(toret)
            counter+=1
