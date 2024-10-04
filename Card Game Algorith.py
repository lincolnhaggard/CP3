import random
from math import *
import copy
import time



class player:
    def __init__(self,num=False):
        if num==False:
            self.num=[1]*1000
        else:
            self.num=[]
            for i in num:
                self.num.append((random.randint(-10,10)/10)+i)
        self.cm=3
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
    def attack(self,oh,om):
        self.cm+=self.m
        self.choice=[1,1,1,1]
        count=0
        for i in range(4):
            self.choice+=oh*self.num[count]
            count+=1
        for i in range(4):
            self.choice+=om*self.num[count]
            count+=1
        for i in range(4):
            self.choice+=self.ch*self.num[count]
            count+=1
        for i in range(4):
            self.choice+=self.cm*self.num[count]
            count+=1
        max=0
        for i in range(len(self.choice)):
            if self.choice[i]>self.choice[max] and (i==1 or ((i==2 and self.cm>=1) or (i==3 and self.cm>=3) ir (i==3 and self.cm>=3))):
                max=i
        
        
        

    
        
            
    
        

p=[]
for i in range(100):
    p.append(player)
#print(p.guess())

end=False
turn=0
count=0
while True:
    for i in player:
        pass