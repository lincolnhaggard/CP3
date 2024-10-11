import random
from math import *
import copy
import time



class player:
    def __init__(self,num=False):
        if num==False:
            self.num=[1]*100
        else:
            self.num=[]
            for i in num:
                self.num.append(round(random.randint(-10,10)/10+i,2))
        self.cm=3
        self.ba=0
    def startfight(self):
        if self.num[-1]>1:
            self.a=3
            if self.num[-2]>0:
                self.h=2
                self.m=1
            else:
                self.m=2
                self.h=1
        elif self.num[-2]>1:
            self.h=3
            if self.num[-1]>0:
                self.a=2
                self.m=1
            else:
                self.m=2
                self.a=1
        else:
            self.m=3
            if self.num[-1]>0:
                self.a=2
                self.h=1
            else:
                self.a=1
                self.h=2
        self.ch=self.h*4
    def attack(self,oh,om,turns):
        self.choice=[1,1,1,1]
        count=0
        for i in range(4):
            self.choice[i]+=oh*self.num[count]
            count+=1
        for i in range(4):
            self.choice[i]+=om*self.num[count]
            count+=1
        for i in range(4):
            self.choice[i]+=self.ch*self.num[count]
            count+=1
        for i in range(4):
            self.choice[i]+=self.cm*self.num[count]
            count+=1
        for i in range(4):
            self.choice[i]+=self.ba*self.num[count]
            count+=1
        for i in range(4):
            self.choice[i]+=turns*self.num[count]
            count+=1
        max=1
        for i in range(1,len(self.choice)+1):
            if self.choice[i-1]>self.choice[max]:
                max=i

        return max
        
        
        

    
        
            
    
        

p=[]
for i in range(100):
    p.append(player([1]*100))
    p[-1].startfight()
wins=[0]*1000
#print(p.guess())

end=False
turn=0
count=-900
shown=False
while True:
    count+=1
    print(count)
    time.sleep(0.001)
    for x,i in enumerate(p):
        for y,k in enumerate(p):
            turns=0
            k.ch=k.h*4
            k.cm=3
            i.cm=3
            i.ch=k.h*4
            i.ba=0
            k.ba=0
            while k.ch>0 and i.ch>0:
                
                first=i.attack(k.ch,k.cm,turns)
                second=k.attack(i.ch,i.cm,turns)

                k.cm+=k.m
                i.cm+=i.m
                #print(f"I Health:{i.ch} Mana:{i.cm} Bonus:{i.ba} Choice: {first}")
                #print(f"K Health:{k.ch} Mana:{k.cm} Bonus:{k.ba} Choice: {second}")
                #time.sleep(1)
                if first==1:
                    k.ch-=i.a+i.ba
                elif first==2 and i.cm>=3:
                    i.ba+=i.a
                    i.cm-=3
                elif first==3 and i.cm>=3:
                    i.cm-=3
                    i.ch+=i.h
                elif first==4 and i.cm>=3:
                    i.cm-=3
                    k.ch-=(i.a+i.ba)*2
                else:
                    pass
                if second==1:
                    i.ch-=k.a+k.ba
                elif second==2 and k.cm>=3:
                    k.ba+=k.a
                    k.cm-=3
                elif second==3 and k.cm>=3:
                    k.cm-=3
                    k.ch+=k.h
                elif second==4 and k.cm>=3:
                    k.cm-=3
                    i.ch-=(k.a+k.ba)*2
                else:
                    pass
                if turns>10:
                    k.ch-=turns-10
                    i.ch-=turns-10
                turns+=1
            
            if i.ch==0:
                wins[y]+=1
            else:
                wins[x]+=1
            if count==100:
                shown=True
            
    best=wins.index(max(wins))
    wins=[0]*100
    p2=[]
    for i in range(100):
        p2.append(player(p[best].num))
        p2[-1].startfight()
    if count==100:
        break
    p=p2
    
print(p[best].num)
f=open("Ai scores","a")
f.write("\n\n"+str(p[best].num))
f.close()

k=p[best]
k.ch=k.h*4
i=player()
i.startfight()
turns=0
while k.ch>0 and i.ch>0:
                print(f"Enemy H: {k.ch}, M: {k.cm}, T: {turns}")
                print(f"H: {i.ch}, M: {i.cm}, Ba: {i.ba}")
                first=int(input("What do you do, 1-4"))
                second=k.attack(i.ch,i.cm,turns)

                k.cm+=k.m
                i.cm+=i.m
                #print(f"I Health:{i.ch} Mana:{i.cm} Bonus:{i.ba} Choice: {first}")
                #print(f"K Health:{k.ch} Mana:{k.cm} Bonus:{k.ba} Choice: {second}")
                #time.sleep(1)
                if first==1:
                    k.ch-=i.a+i.ba
                elif first==2 and i.cm>=3:
                    i.ba+=i.a
                    i.cm-=3
                elif first==3 and i.cm>=3:
                    i.cm-=3
                    i.ch+=i.h
                elif first==4 and i.cm>=3:
                    i.cm-=3
                    k.ch-=(i.a+i.ba)*2
                else:
                    pass
                if second==1:
                    i.ch-=k.a+k.ba
                elif second==2 and k.cm>=3:
                    k.ba+=k.a
                    k.cm-=3
                elif second==3 and k.cm>=3:
                    k.cm-=3
                    k.ch+=k.h
                elif second==4 and k.cm>=3:
                    k.cm-=3
                    i.ch-=(k.a+k.ba)*2
                else:
                    pass
                if turns>10:
                    k.ch-=turns-10
                    i.ch-=turns-10
                turns+=1
                print(f"Enemy H: {k.ch}, M: {k.cm}, T: {turns}")
                print(f"H: {i.ch}, M: {i.cm}, Ba: {i.ba}")