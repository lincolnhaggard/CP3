import time
import math

class BigNum:
    def __init__(self,num=0):
        self.num=[num]
        self.simplify()
    def __str__(self):
        numends=[
            "","K","M","B","T","Qa","Qi","S","Sp","Oc","N","De"
            ]
        numendsends=[
            "De","Vi","Ti","Qai","Qii","Si","Spi","Oi","Ni"
        ]
        numendspres=[
            "","U","D","T","Qa","Qi","S","Sp","O","N"
        ]
        toret=""
        toret+=str(self.num[0])
        if (len(self.num)%3==2 or len(self.num)%3==0) and len(self.num)>1:
            toret+=str(self.num[1])
            if len(self.num)%3!=0:
                toret+="."
        elif len(self.num)>1:
            toret+="."
            toret+=str(self.num[1])
        
        if len(self.num)>2:
            toret+=str(self.num[2])
        numbersuffix=math.floor((len(self.num)+2)/3)-1
        if numbersuffix<len(numends):
            toret+=numends[numbersuffix]
        else:
            
            toret+=numendspres[numbersuffix%10-1]
            toret+=numendsends[math.floor((numbersuffix-1)/10)-1]
            print(numbersuffix)
        return toret
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
    def __mul__(self,other):
        if isinstance(other,BigNum):
            newnum=BigNum()
            newnum.num=[0]*(len(other.num)+len(self.num))
            for x,i in enumerate(self.num):
                for y,k in enumerate(other.num):
                    #print(abs(x-(len(self.num)-1)),abs(y-(len(other.num)-1)),i,k)
                    newnum.num[-((abs(x-(len(self.num)-1))+abs(y-(len(other.num)))))]+=i*k
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
        while self.num[0]==0 and len(self.num)>1:
            self.num.pop(0)
                
                

money=BigNum(14765)
dollars =BigNum(1245674)
print(money*dollars)
print(dollars)