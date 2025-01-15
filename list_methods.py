from functools import reduce
import random
import sys
mylist = [1,2,3,4,6,5,7,8,9,11,10]
for i in range(10000):
    mylist.append(random.randint(1,i+2))
newlist = ["","Argentina","","Brazil","Chile","","Colombia","","Ecuador","","","Venezuela"]

def increase(num):
    return num+1
def multiple(num): 
    if num%3==0: return num

print(list(map(increase, mylist)))
print(list(filter(multiple,mylist)))
print(list(filter(lambda num: num%3==0, mylist)))
print(list(filter(None,newlist)))


multiplier = lambda x,y: x*y
sys.set_int_max_str_digits(43000)
print(reduce(multiplier, mylist))