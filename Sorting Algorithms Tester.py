import random
import time as t
"""
heapsort
countingsort
radixsort
bucketsort


shellsort
timsort
combsort
pigeonholesort
cyclesort
cocktailsort
strandsort
bitonicsort
"""
#Functions

def bubble(data):
    time=0
    #done is only complete when no swaps have been made
    done=False
    while not done:
        done=True
        for i in range(len(data)-1):
            #checks if needs to be swapped
            if data[i]>data[i+1]:
                #swaps
                (data[i],data[i+1])=(data[i+1],data[i])
                done=False
                time+=1
    return (data,time)

def insertion(data):
    time=0
    
    for i in range(1,len(data)):
        var=data[i]
        k=i-1
        while k>=0 and data[k]>var:
            data[k+1]=data[k]
            k-=1
        data[k+1]=var
    return data

def selection(data):
    time=0
    newdata=[]
    for i in range(len(data)):
        min=data[0]
        for k in range(len(data)):

            if data[k]<min:
                min=data[k]
        newdata.append(min)
        data.remove(min)
    return newdata

def quick(data):
    if len(data)>1:
        time=0
        i=-1
        j=0
        pivot=len(data)-1
        for _ in range(len(data)):
            if data[j]<data[pivot]:
                i+=1
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
            j+=1
            if j==pivot:
                i+=1
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
                data=quick(data.copy()[:i])[0]+[data[i]]+quick(data.copy()[i+1:])[0]
                break
        return (data,time)
    else:
        return (data,0)
def merge(data):
    if len(data)<=1:
        return data
    left=merge(data[:len(data)//2])
    right=merge(data[len(data)//2:])


    newdata = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            newdata.append(left[i])
            i += 1
        else:
            newdata.append(right[j])
            j += 1

    newdata=newdata+left[i:]
    newdata=newdata+right[j:]
    return newdata

def bingo(data):
    time=0
    newdata=[]
    min=data[0]
    max=data[0]
    
    for k in range(len(data)):
        if data[k]>max:
            max=data[k]
        if data[k]<min:
            min=data[k]
    bingo=max
    j=0
    while min<bingo:
        for i in range(j,len(data)):
            if data[i]==min:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
                j+=1
            elif data[i]<bingo:
                bingo=data[i]
        min=bingo
        bingo=max
        

    
        
    return data

def combsort(data):
    gap=len(data)//1.3
    done=False
    while not done:
        done=True
        for i in range(len(data)):
            if i+int(gap)<len(data):
                if data[i]>data[i+int(gap)]:
                    temp=data[i]
                    data[i]=data[i+int(gap)]
                    data[i+int(gap)]=temp
                    done=False
        if gap!=1:
            gap=gap//1.3
            print(gap)
            done=False
        
    return data

def fancynum(num):
    if num==1:
        return "1st"
    elif num==2:
        return "2nd"
    elif num==3:
        return "3rd"
    else:
        return str(num)+"th"

sort=input("What sorting algorithm would you like to use?: ").lower()
datatyp=input("Whould you like to input your own data?(otherwise a random set will be generated): ").lower()
if datatyp=="yes" or datatyp=="data" or datatyp=="enter data" or datatyp=="enter":
    done=False
    while not done:
        try:
            varnum=int(input("How many values would you like in your data: "))
            done=True
        except:
            print("Something went wrong try again")
    data=[]


    for i in range(varnum):
        done=False
        while not done:
            try:
                data.append(int(input(f"Enter the {fancynum(i+1)} value: ")))
                done=True
            except:
                print("Something went wrong try again")
else:
    data=[]
    for i in range(random.randint(5,50)):
        data.append(random.randint(0,50))


if sort=="bubble" or sort=="bubblesort" or sort=="bubble sort":
    output=bubble(data)

print(output[0])
print(output[1])


