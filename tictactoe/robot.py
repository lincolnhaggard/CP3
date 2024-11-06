import random

class Robot:
    def __init__(self,vals=None):
        self.vals=[]
        if vals==None:
            for i in range(100):
                self.vals.append(float(random.randint(-100,100))/1000)
        else:
            for i in vals:
                self.vals.append(i+(float(random.randint(-10,10))/1000))
    