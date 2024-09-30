import random
from math import *
class card:
    def __init__(self,typ,num,tnum):
        self.typ=typ
        self.num=num
        self.tnum=tnum
    def __repr__(self):
        return self.num+" of "+self.typ

deck=[]
for i in ["Club","Spade","Heart","Diamond"]:
    for x,k in enumerate(["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]):
        deck.append(card(i,k,x))
shuffled_deck=[]
while len(deck)>0:
    shuffled_deck.append(random.choice(deck))
    deck.remove(shuffled_deck[-1])
deck=shuffled_deck
class player:
    def __init__(self):
        self.hand=[]
        for i in range(5):
            self.hand.append(deck[-1])
            deck.remove(self.hand[-1])
players=[player(),player(),player(),player()]
board=[[],[],[],[],[],[],[],[]]



end=False
turn=0
while not end:




    turn+=1
    if turn==4:
        turn=0
    for i in players:
        if len(i.hand)==0:
            end=True