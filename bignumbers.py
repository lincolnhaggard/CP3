import time
import math

class BigNum:
    def __init__(self,num=0):
        self.num=[num]
        self.simplify()
    def __str__(self):
        numends={
            (0,3):"",
            (4,6):"K",
            (7,9):"M",
            (10,12):"B",
            (13,15):"T",
            (16,18):"Qa",
            (19,21):"Qi",
            (22,24):"S",
            (25,27):"Sp",
            (28,30):"O",
            (31,33):"N",
            (34,36):"De",
            (37,39):"UDe",
            (40,42):"DDe",
            (43,45):"TDe",
            (46,48):"QaDe",
            (49,51):"QiDe",
            (52,54):"SDe",
            (55,57):"SpDe",
            (58,60):"OcDe",
            (61,63):"NDe",
            (64,66):"Vi",
            (67,69):"UnVi",
            (70,72):"DVi",
            (73,75):"TVi",
            (76,78):"QaVi",
            (79,81):"QiVi",
            (82,84):"SVi",
            (85,87):"SpVi",
            (88,90):"OVi",
            (91,93):"NVi",
            (94,96):"Tr",
            (97,99):"UTr",
            (100,102):"DTr",
            (103,105):"TTr",
            (106,108):"QaTr",
            (109,111):"QiTr",
            (112,114):"STr",
            (115,117):"SpTr",
            (118,120):"OTr",
            (121,123):"NTr",
            (124,126):"Qua",
            (127,129):"UQua",
            (130,132):"DQua",
            (133,135):"TQua",
            (136,138):"QaQua",
            (139,141):"QiQua",
            (142,144):"SQua",
            (145,147):"SpQua",
            (148,150):"OQua",
            (151,153):"NQua",
            (154,156):"Qui"#Sx,Se,Oi,Ni
        }
        return str(self.num)
    def __add__(self,other):
        if isinstance(other,BigNum):
            newnum=BigNum()
            if len(other.num)>len(self.num):
                newnum.num=[0]*len(other.num)
            else:
                newnum.num=[0]*len(self.num)
            for i in range(1,len(other.num)+1):
                newnum.num[-i]+=other.num[-i]
            for i in range(1,len(self.num)+1):
                newnum.num[-i]+=self.num[-i]
        newnum.simplify()
        return newnum
    def simplify(self):
        done=False
        while not done:
            done=True
            for i in self.num:
                if i>9:
                    done=False
            for i in range(1,len(self.num)+1):
                if self.num[-i]>9:
                    biggestdigit=math.floor(math.log(abs(self.num[-i]),10))
                else:
                    biggestdigit=1
                if self.num[-i]>10**(biggestdigit)-1:
                    self.num[-i]-=10**(biggestdigit)
                    if i==len(self.num):
                        self.num.insert(0,10**(biggestdigit-1))
                    else:
                        self.num[-(i+1)]+=10**(biggestdigit-1)
                    break
                
                

money=BigNum(934851245)
dollars =BigNum(453098)
print(money+dollars)