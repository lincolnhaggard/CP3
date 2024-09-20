import random
import time as t
"""
bubble
insertion
selection
quicksort
heapsort
mergesort
countingsort
radixsort
bucketsort
bingosort
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

def quicksort(data):
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
                data=quicksort(data.copy()[:i])[0]+[data[i]]+quicksort(data.copy()[i+1:])[0]
                break
        return (data,time)
    else:
        return (data,0)
print(quicksort([723,541,746,163,964,163,498,274,976,275,959]))

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


