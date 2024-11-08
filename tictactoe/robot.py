import random

class Robot:
    def __init__(self,vals=None):
        self.vals=[]
        if vals==None:
            for i in range(1000):
                self.vals.append(float(random.randint(-100,100)))
        else:
            for i in vals:
                self.vals.append(round(i+(float(random.randint(-10,10))),1))
    def make_choice(self,board,turn):
        count=0
        choice=[[0,0,0],[0,0,0],[0,0,0]]
        for i in board:
            for k in i:
                if k=="N":
                    for x in range(3):
                        for y in range(3):
                            choice[x][y]+=self.vals[count]
                            count+=1
                else:
                    count+=9
                if (k=="X" and turn=="X") or (k=="O" and turn=="O"):
                    for x in range(3):
                        for y in range(3):
                            choice[x][y]+=self.vals[count]
                            count+=1
                else:
                    count+=9
                if (k=="O" and turn=="X") or (k=="X" and turn=="O"):
                    for x in range(3):
                        for y in range(3):
                            choice[x][y]+=self.vals[count]
                            count+=1
                else:
                    count+=9
        max=-100000
        toret=(0,0)
        for x,i in enumerate(choice):
            for y,k in enumerate(i):
                if k>max and board[x][y]=="N":
                    max=k
                    toret=(x,y)
        return toret

    