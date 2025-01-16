import math
import os
import time

class BigNum:
    def __init__(self,num=0):
        if isinstance(num,BigNum):
            self.num=num.num
            self.digits=num.digits
        else:
            self.num=str(num)
            self.digits=len(str(num))
            self.num=self.num[:5]
            if self.digits>100:
                self.digits=BigNum(self.digits)
    def check(self):
        if self.digits>100:
            self.digits=BigNum(self.digits)

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
            #print(self.digits,num.digits)
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
            print(self.digits,num.digits,self.digits+num.digits,newnum.digits)
            if len(str(int(self.num)*int(num.num)))>len(self.num)+len(num.num)-1:
                newnum.digits+=1
            newnum.check()
            return newnum
    def __pow__(self,num):
        if isinstance(num,int):
            num=BigNum(num)
        if isinstance(num,BigNum):
            pass
    def __str__(self):
        toret=""
        if self.digits<=3:
            toret=self.num
        elif self.digits>60:
            toret=f"{self.num[0]}.{self.num[1:3]}e{self.digits-1}"

        elif self.digits>3:
            #1k:3, 1M:6, 1B:9, 1T:12, 1Qa:15, 1Qi:18, 1Vi:57
            suffixs=("K","M","B","T","Qa","Qi","Sx","Sp","N","D",
                        "uD","dD","tD","qaD","qiD","sxD","spD","nD","Vi")
            toret=self.num[:3]
            if (self.digits-1)%3==0:
                toret=toret[:1]+"."+toret[1:]
            elif (self.digits-1)%3==1:
                toret=toret[:2]+"."+toret[2:]
            toret+=suffixs[math.floor((self.digits-4)/3)]
        return toret
    def __repr__(self):
        if isinstance(self.digits,BigNum):
            return f"Num: {self.num}, Digits: {self.digits.__repr__()}"
        return f"Num: {self.num}, Digits: {self.digits}"


money=BigNum(100000)
#money.digits=1000
money.check()
print(money)
print(money.__repr__())
money-=1
print(money)
print(money.__repr__())
for i in range(150):
    money=money**4
    os.system("clear")
    print(money)
    print(money.__repr__())
    time.sleep(0.1)
