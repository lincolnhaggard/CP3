import random
import math
import time

class Monster:
    def __init__(self,name,biome):
        self.name=name
        self.biome=biome
    def __str__(self):
        return self.name
    def depthstr(self):
        return f"{self.name}: A:{self.attackstat} S:{self.speedstat} H:{self.healthstat} B:{self.biome}"
    def attack(self,other):
        pass
    def breed(self,other):
        species=random.choice((self,other))
        extra=random.choice(list("abcdefghijklmnopqrstuvwxyz"))
        extra1=random.choice(list("abcdefghijklmnopqrstuvwxyz"))
        extra2=random.choice(list("abcdefghijklmnopqrstuvwxyz"))
        if isinstance(species,Arachnid):
            newmonster=Arachnid(extra1+self.name[:math.floor(len(self.name)/2)-3]+extra+other.name[math.floor(len(other.name)/2)+3:]+extra2,random.choice((self.biome,other.biome)))
        if isinstance(species,Reptile):
            newmonster=Reptile(extra1+self.name[:math.floor(len(self.name)/2)-3]+extra+other.name[math.floor(len(other.name)/2)+3:]+extra2,random.choice((self.biome,other.biome)))
        if isinstance(species,Mammal):
            newmonster=Mammal(extra1+self.name[:math.floor(len(self.name)/2)-3]+extra+other.name[math.floor(len(other.name)/2)+3:]+extra2,random.choice((self.biome,other.biome)))
        if isinstance(species,Slime):
            newmonster=Slime(extra1+self.name[:math.floor(len(self.name)/2)]+extra+other.name[math.floor(len(other.name)/2):]+extra2,random.choice((self.biome,other.biome)))
        newmonster.speedstat=random.choice((self.speedstat,other.speedstat))+random.randint(-1,1)
        newmonster.attackstat=random.choice((self.attackstat,other.attackstat))+random.randint(-1,1)
        newmonster.healthstat=random.choice((self.healthstat,other.healthstat))+random.randint(-1,1)
        newmonster.health=newmonster.healthstat
        return newmonster

class Arachnid(Monster):
    def __init__(self,name,biome):
        super().__init__(name,biome)
        self.speedstat=random.randint(7,10)
        self.attackstat=random.randint(3,6)
        self.healthstat=random.randint(1,4)*3
        self.health=self.healthstat
    def attack(self,other):
        for i in range(math.floor(self.speedstat/4)):
            other.health-=math.floor(self.attackstat/2)

class Reptile(Monster):
    def __init__(self,name,biome):

        super().__init__(name,biome)
        self.speedstat=random.randint(1,4)
        self.attackstat=random.randint(7,10)
        self.healthstat=random.randint(3,6)*3
        self.health=self.healthstat
    def attack(self,other):
        other.health-=self.attackstat

class Mammal(Monster):
    def __init__(self,name,biome):

        super().__init__(name,biome)
        self.speedstat=random.randint(2,5)
        self.attackstat=random.randint(2,5)
        self.healthstat=random.randint(7,10)*3
        self.health=self.healthstat
    def attack(self,other):
        for i in range(self.attackstat):
            other.health-=math.ceil(random.randint(1,3)/2)

class Slime(Monster):
    def __init__(self,name,biome):

        super().__init__(name,biome)
        self.speedstat=random.randint(1,4)
        self.attackstat=random.randint(5,8)
        self.healthstat=random.randint(5,8)*3
        self.health=self.healthstat
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
    count=0
    while len(contestants)>2:
        while contestants[count].health>0 and contestants[count+1].health>0:
            if contestants[count].speedstat>contestants[count+1].speedstat:
                contestants[count].attack(contestants[count+1])
                if contestants[count+1].health>0:
                    contestants[count+1].attack(contestants[count])
            else:
                contestants[count+1].attack(contestants[count])
                if contestants[count].health>0:
                    contestants[count].attack(contestants[count+1])

        if contestants[count].health<0:
            print(f"{contestants[count+1]} has deafeated {contestants[count]}")
            contestants.pop(count)
        else:
            print(f"{contestants[count]} has deafeated {contestants[count+1]}")
            contestants.pop(count+1)
        
        count+=1
        if count+1>len(contestants):
            count=0
            for i in contestants:
                i.health=i.healthstat
        time.sleep(0.1)
    for i in range(2**5-2):
        if random.randint(1,2)==1:
            contestants.append(contestants[0].breed(contestants[1]))
        else:
            contestants.append(contestants[1].breed(contestants[0]))
    toret=""
    print(contestants[0].depthstr())
    print(contestants[1].depthstr())
    for i in contestants:
        toret+=str(i)+" , "
    print(toret)

