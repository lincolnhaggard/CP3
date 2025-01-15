


class Robot:
    def __init__(self,length,maxnum):
        self.maxnum=maxnum
        self.length=length
        self.posibles=[]
        newlist=[1]*length
        while True:
            self.posibles.append(newlist.copy())
            if newlist==[maxnum]*length:
                break
            newlist[0]+=1
            for i in range(length):
                if newlist[i]>maxnum and i!=length-1:
                    newlist[i]-=maxnum
                    newlist[i+1]+=1
    
    def addguess(self,guess,checks):
        for i in range(self.maxnum):
            for x,i in enumerate(guess):
                for k in self.posibles:
                    if checks[x]==True:
                        if k[x]!=i:
                            self.posibles.remove(k)
                            del k
                    elif checks[x]==None:
                        if not i in k:
                            self.posibles.remove(k)
                            del k
                    else:
                        if i in k:
                            self.posibles.remove(k)
                            del k
    def getguess(self):
        nums=[]
        for i in range(self.length):
            nums.append([0]*self.maxnum)
        for i in self.posibles:
            for x,k in enumerate(i):
                nums[x][k-1]+=1
        half=len(self.posibles)//2
        guess=[]
        for i in nums:
            highest=0
            highscore=len(self.posibles)
            for x,k in enumerate(i):
                if abs(k-half)<highscore:
                    highscore=abs(k-half)
                    highest=x
            guess.append(highest+1)
            
        return guess
            
            

    