import math
import os
import time
import random

class BigNum:
    def __init__(self,num=0):
        if isinstance(num,BigNum):
            self.num=num.num
            self.digits=num.digits
        else:
            self.num=str(num)
            self.digits=len(str(num))
            self.num=self.num[:5]
            self.check()
           
            
    def check(self,e=0):
        
        if self.digits>100:
            self.digits=BigNum(self.digits)
        if self.digits>60:
            if isinstance(self.digits,BigNum):
                e=self.digits.check(e)+1
            else:
                e+=1
        self.numofe=e
        return e
        

    def __gt__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits>num.digits:
                return True
            elif self.digits==num.digits:
                if int(self.num)>int(num.num):
                    return True
            else:
                return False
    def __lt__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits<num.digits:
                return True
            elif self.digits==num.digits:
                if int(self.num)<int(num.num):
                    return True
            else:
                return False
    def __eq__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits==num.digits and self.num==num.num:
                return True
            else:
                return False
    def __ne__(self,num):
        return not self.__eq__(num)
    
    def __ge__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits>=num.digits:
                return True
            elif self.digits==num.digits:
                if int(self.num)>=int(num.num):
                    return True
            else:
                return False
    def __le__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits<=num.digits:
                return True
            elif self.digits==num.digits:
                if int(self.num)<=int(num.num):
                    return True
            else:
                return False

    def __add__(self,num):
        
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits>=num.digits+5:
                return self
            if self.digits+5<=num.digits:
                return self
            if num.digits<5 or self.digits<5:
                newnum=BigNum(int(int(self.num)+(int(num.num))))
            elif self.digits>num.digits:
                newnum=BigNum(int(int(self.num)+(int(num.num)/(self.digits-num.digits))))
                newnum.digits=self.digits
                if len(str(int(int(self.num)+(int(num.num)/(self.digits-num.digits)))))>len(self.num):
                    newnum.digits+=1
            elif self.digits<num.digits:
                newnum=BigNum(int((int(self.num)/(num.digits-self.digits))+int(num.num)))
                newnum.digits=num.digits
                if len(str(int((int(self.num)/(num.digits-self.digits))+int(num.num))))>len(self.num):
                    newnum.digits+=1
            else:
                newnum=BigNum(int(self.num)+int(num.num))
                newnum.digits=self.digits
                if len(str(int(self.num)+int(num.num)))>len(str(self.num)):
                    newnum.digits+=1
            newnum.check()
            return newnum
    def __sub__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            if self.digits>=num.digits+5:
                return self
            if self.digits+5<=num.digits:
                return self
            if num.digits<5 or self.digits<5:
                newnum=BigNum(int(int(self.num)-(int(num.num))))
            elif self.digits>num.digits:
                newnum=BigNum(int(int(self.num)-(int(num.num)/(self.digits-num.digits))))
                newnum.digits=self.digits
                if len(str(int(int(self.num)-(int(num.num)/(self.digits-num.digits)))))<len(self.num):
                    newnum.digits-=1
            elif self.digits<num.digits:
                newnum=BigNum(int((int(self.num)/(num.digits-self.digits))+int(num.num)))
                newnum.digits=num.digits
                if len(str(int((int(self.num)/(num.digits-self.digits))-int(num.num))))<len(self.num):
                    newnum.digits-=1
            else:
                newnum=BigNum(int(self.num)-int(num.num))
                newnum.digits=self.digits
                if len(str(int(self.num)-int(num.num)))<len(str(self.num)):
                    newnum.digits-=1
            newnum.check()
            return newnum
    def __mul__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            newnum=BigNum(int(self.num)*int(num.num))
            newnum.digits=(self.digits+num.digits)
            newnum.digits-=1
            if len(str(int(self.num)*int(num.num)))>len(self.num)+len(num.num)-1:
                newnum.digits+=1
            newnum.check()
            return newnum
    def __pow__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            #I can't figure out how to get the numbers to behave
            #unil I do, we will just use random as a replacement
            newnum=BigNum(int(self.num)**random.choice((2,4,5,6)))
            newnum.digits=num*self.digits
            newnum.check()
            return newnum
    
    def __int__(self):
        if self.digits<=5:
            return int(self.num)
        elif self.digits<=100:
            return int(self.num)*(10**self.digits)
        else:
            return "to large"
    
    def get_lowest(self):
        if isinstance(self.digits,BigNum):
            return self.digits.get_lowest()
        else:
            return self

    def __str__(self):
        toret=""
        if self.digits<=3:
            toret=self.num
        elif self.numofe>3:
            toret=f"{self.num[0]}.{self.num[1:3]}J{self.numofe}E{self.digits.get_lowest()-1}"
        elif self.digits>60:
            toret=f"{self.num[0]}.{self.num[1:3]}E{self.digits-1}"

        elif self.digits>3:
            #1k:3, 1M:6, 1B:9, 1T:12, 1Qa:15, 1Qi:18, 1Vi:57
            suffixs=("K","M","B","T","Qa","Qi","Sx","Sp","N","D",
                        "uD","dD","tD","qaD","qiD","sxD","spD","nD","Vi")
            toret=self.num[:3]
            if (int(self.digits)-1)%3==0:
                toret=toret[:1]+"."+toret[1:]
            elif (int(self.digits)-1)%3==1:
                toret=toret[:2]+"."+toret[2:]
            toret+=suffixs[math.floor((int(self.digits)-4)/3)]
        return toret
    def __repr__(self):
        if isinstance(self.digits,BigNum):
            return f"Num: {self.num}, NumofE: {self.numofe}, Digits: {self.digits.__repr__()}"
        return f"Num: {self.num}, NumofE: {self.numofe}, Digits: {self.digits}"


money=BigNum(100000)
#money.digits=1000
money.check()
print(money)
print(money.__repr__())
money-=1
print(money)
print(money.__repr__())

for i in range(1000):
    money=money**money
    os.system("clear")
    print(money)
    #print(money.__repr__())
    time.sleep(0.1)
