import random
import math

def generate_num():
    toret=""
    for i in range(4):
        toret+=str(random.randint(0,9))
    return int(toret)
    
def isprime(num):
    if num > 1:
       
        for i in range(2, (num//2)+1):
           
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def rate_number(num):
    rarity=0
    mathness=0
    coolness=0
    specialness=10
    nums={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
    for x,i in enumerate(str(num)):
        if int(i)==7:
            coolness+=10
            specialness-=2
        if str(num)[x]==str(num)[-(x+1)]:
            coolness+=5
        if i=="0":
            mathness+=5
            coolness+=3
            specialness-=1
        if i=="8":
            coolness+=5
        if i=="9":
            coolness+=5
        nums[str(i)]+=1
    #for k in range(1,num):
    #    if num%k==0:
    #        mathness+=2
    #if isprime(num):
    #    specialness+=10
    #    mathness-=10
    
    for k in range(1,num):
        if num%k==0:
            mathness*=1.5
            specialness*=2
        else:
            break
    
    
    for k in nums.keys():
        coolness*=2**nums[k]
    if math.sqrt(num)==math.floor(math.sqrt(num)):
        mathness+=10
    specialness-=math.sqrt(abs(num))
    rarity+=mathness*0.1
    rarity+=coolness*1
    rarity+=specialness*0.5
    if rarity<0:
        rarity=0
    del nums
    return rarity
def rarity_stars(rarity):
    stars=int(math.sqrt(math.sqrt(rarity))**0.75/10.2*10)
    if stars<1:
        stars=1
    return str(stars)+" stars"
nums={12252240:int(rate_number(12252240))}
highest=nums[12252240]
hignum=12252240
newnums={}
#1441440
for k in range(100000):
    del newnums
    newnums={}
    for i in range(100000):
        newnum=random.randint(10000,99999)
        nums[i+(100000*k)+44699999]=int(rate_number(i+(100000*k)+44699999))
        newnums[i+(100000*k)+44699999]=nums[i+(100000*k)+44699999]
    print(list(nums.keys())[-1],nums[list(nums.keys())[-1]])
    
    for i in list(newnums.keys()):
        if newnums[i]>highest:
            highest=nums[i]
            hignum=i
    print(hignum,highest)
#print(rate_number(int(input("Enter a number: "))))
while True:
    try:
        print(rarity_stars(rate_number(int(input("Enter a number: ")))))
    except:
        print("enter a whole number please")