import random
import time as t
import timeit
"""
/|bubble
/|Insertion
/|Selection
/|quick
O|Heap
/|Merge
/|Counting
/|Radix
O|Bucket
/|Bingo
/|Shell
//|Tim
/|Comb
/|pigeonhole
O|Cycle
/|Cocktail
O|Strand
O|Bitonic

"""
#Functions

def bubble(data,show):
    time=0
    #done is only complete when no swaps have been made
    done=False
    while not done:
        done=True
        for i in range(len(data)-1):
            #checks if needs to be swapped
            if show:
                print(data)
                t.sleep(1)
                print("Swap "+str(data[i])+" and "+str(data[i+1])+" if "+str(data[i])+" is greater than "+str(data[i+1]))
                t.sleep(1)
                print(str(data[i])+">"+str(data[i+1])+"="+str(data[i]>data[i+1]))
                t.sleep(1)
            if data[i]>data[i+1]:
                if show:
                    print("Swaped "+str(data[i])+" and "+str(data[i+1]))
                    t.sleep(1)
                (data[i],data[i+1])=(data[i+1],data[i])
                
                done=False
    return data


def insertion(data,show):
    time=0
    
    for i in range(1,len(data)):
        var=data[i]
        if show:
            print(data)
            print(f"Inserting {var}")
            t.sleep(1)
        k=i-1
        while k>=0 and data[k]>var:
            data[k+1]=data[k]
            k-=1
        data[k+1]=var
        if show:
            print(str(var)+f" goes in the {k+1}s slot")
            t.sleep(1)
    return data

def selection(data,show):
    time=0
    newdata=[]
    if show:
        print(data)
    for i in range(len(data)):
        min=data[0]
        for k in range(len(data)):

            if data[k]<min:
                min=data[k]
        if show:
            print(f"The min is {min}")
            t.sleep(1)
            print("Put the min at the beginning of new list")
        newdata.append(min)
        if show:
            print(newdata)
            t.sleep(1)
        data.remove(min)
    return newdata

def quick(data,show):
    if len(data)>1:
        time=0
        i=-1
        j=0
        pivot=len(data)-1
        for _ in range(len(data)):
            if show:
                print(data)
                print(f"pointer 1: {i}")
                t.sleep(1)
                print(f"pointer 2: {j}")
                t.sleep(1)
                print(f"Is {data[j]} less than"+f" {data[pivot]}")
                t.sleep(1)
            if data[j]<data[pivot]:
                if show:
                    print("Yes, incremeant pointer 1 by 1 and swap")
                    t.sleep(1)
                i+=1
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
            if show:
                print("Increament pointer 2 by 1")
                t.sleep(1)
            j+=1
            if show:
                print("Is pointer 2 at the piviot?")
                t.sleep(1)
            if j==pivot:
                i+=1
                if show:
                    print("Yes, increament pointer 1 by 1")
                    t.sleep(1)
                    print("Swap the number at pointer 1 and the piviot")
                    t.sleep(1)
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
                if show:
                    print("Split the list around the piviot and repeat")
                    t.sleep(1)
                data=quick(data.copy()[:i],show)+[data[i]]+quick(data.copy()[i+1:],show)
                if show:
                    print("combine back together")
                break
        return data
    else:
        return data

def merge(data,show):
    if show:
        print("Check if the data has a length greater than 1")
        t.sleep(1)
    if len(data)<=1:
        if show:
            print("The data is one item long return data")
            t.sleep(1)
        return data
    if show:
        print(data)
        print("Split the data into left and right half down the middle and do merge sort on each of them")
        t.sleep(1)
        print(f"Left: {data[:len(data)//2]}")
        t.sleep(1)
        print(f"Right: {data[len(data)//2:]}")
        t.sleep(1)
    left=merge(data[:len(data)//2],show)
    right=merge(data[len(data)//2:],show)
    if show:
        print("Make a new list")
        t.sleep(1)

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
    if show:
        print("Combine the data into the right order")
        t.sleep(1)

    newdata=newdata+left[i:]
    newdata=newdata+right[j:]
    if show:
        print(newdata)
        print("Return the new data")
        t.sleep(1)
    return newdata

def counting(data,show):
    max=data[0]
    newdata=[0]*len(data)
    for k in range(len(data)):
        if data[k]>max:
            max=data[k]
    if show:
        print("Find the max of the data")
        t.sleep(1)
    count=[0]*(max+1)
    if show:
        print("Make a list that has a length equal to the max of the data")
        t.sleep(1)
        print("Go through the data and add 1 to the corrosponding thing in count")
        t.sleep(1)
    for i in data:
        if show:
            print(f"Item: {i}")
            t.sleep(1)
        count[i]+=1
        if show:
            print(count)
            t.sleep(1)
            print(f"Added the item to the {i}'s slot")
            t.sleep(1)
    if show:
        print("Go through the new list and add the previous item the the next")
        t.sleep(1)
    for i in range(1,max+1):
        if show:
            print(f"Adding {count[i-1]} to the "+f"{i}'s slot")
            t.sleep(1)
            print(count)
            t.sleep(1)
        count[i]+=count[i-1]
    if show:
        print("Make the final list")
        t.sleep(1)
        print("then go through each item in the orignal list")
        t.sleep(1)
    for i in range(len(data)):
        if show:
            print(f"Set the item in the final list to {data[i]} "+f"At the slot corrosponding to the 2nd list at the {data[i]} slot")
            t.sleep(1)
            print(f"Then subtract one from the 2nd list at the {data[i]} slot")
            t.sleep(1)
            print(newdata)
            t.sleep(1)
        newdata[count[data[i]]-1]=data[i]
        count[data[i]]-=1

    return newdata

def radix(data,show):
    max=data[0]
    for k in range(len(data)):
        if data[k]>max:
            max=data[k]
    if show:
        print("Find the max of the data")
        t.sleep(1)
    exp=1
    while max/exp>=1:
        if show:
            print("Preform counting sort for each digit of each part of the data")
            t.sleep(1)
        n = len(data)
        newdata=[0]*(n)
        count=[0]*(10)
        if show:
            print("Make a list that has a length equal to the max of the data")
            t.sleep(1)
            print("Go through the data and add 1 to the corrosponding thing in count")
            t.sleep(1)
        for i in range(0,n):
            if show:
                print(f"Item: {(data[i]//exp)%10}")
                t.sleep(1)
            count[(data[i]//exp)%10]+=1
            if show:
                print(count)
                t.sleep(1)
                print(f"Added the item to the {(data[i]//exp)%10}'s slot")
                t.sleep(1)
        if show:
            print("Go through the new list and add the previous item the the next")
            t.sleep(1)
        for i in range(1, 10):
            if show:
                print(f"Adding {count[i-1]} to the "+f"{i}'s slot")
                t.sleep(1)
                print(count)
                t.sleep(1)
            count[i]+=count[i-1]
        i=n-1
        if show:
            print("Make the final list")
            t.sleep(1)
            print("then go through each item in the orignal list")
            t.sleep(1)
        while i>=0:
            if show:
                print(f"Set the item in the final list to {(data[i]//exp)%10} "+f"At the slot corrosponding to the 2nd list at the {(data[i]//exp)%10} slot")
                t.sleep(1)
                print(f"Then subtract one from the 2nd list at the {(data[i]//exp)%10} slot")
                t.sleep(1)
                print(newdata)
                t.sleep(1)
            newdata[count[(data[i]//exp)%10]-1]=data[i]
            count[(data[i]//exp)%10]-=1
            i-=1
        i=0
        for i in range(0,len(data)):
            data[i]=newdata[i]
        exp*=10
    return data

def bingo(data,show):
    min=data[0]
    max=data[0]
    
    for k in range(len(data)):
        if data[k]>max:
            max=data[k]
        if data[k]<min:
            min=data[k]
    if show:
        print(f"Gets the min({min})"+f" and the max({max}) of the data")
        t.sleep(1)
        print("Bingo=max, and j=0")
        t.sleep(1)
    bingo=max
    j=0
    while min<bingo:
        print(f"Whie min<bingo go through the data starting at the j({j})'s place")
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

def shell(data,show):
    gap=len(data)//2
    while gap>0:
        gap2=gap
        while gap2<len(data):
            gap3=gap2-gap
            while gap3>=0:
                if data[gap3+gap]>data[gap3]:
                    break
                else:
                    temp=data[gap3+gap]
                    data[gap3+gap]=data[gap3]
                    data[gap3]=temp
                gap3-=gap
            gap2+=1
        gap=gap//2
    return data


def comb(data):
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

def pigeonhole(data):
    min=data[0]
    max=data[0]
    
    for k in range(len(data)):
        if data[k]>max:
            max=data[k]
        if data[k]<min:
            min=data[k]
    holes=[0]*(max-min+1)
    for i in data:
        print(i-min)
        holes[i-min]+=1
    newdata=[]
    for i in range(len(holes)):
        newdata+=[i+min]*holes[i]
    return newdata

def cocktail(data):
    time=0
    done=False
    while not done:
        done=True
        for i in range(len(data)-1):
            if data[i]>data[i+1]:
                (data[i],data[i+1])=(data[i+1],data[i])
                done=False
                time+=1
        for i in range(len(data)-1,0,-1):
            if data[i]<data[i-1]:
                (data[i],data[i-1])=(data[i-1],data[i])
                done=False
                time+=1
    return (data,time)



def fancynum(num):
    if num==1:
        return "1st"
    elif num==2:
        return "2nd"
    elif num==3:
        return "3rd"
    else:
        return str(num)+"th"


print("Bubble\nInsertion\nSelection\nQuick\nMerge\nCounting\nRadix\nBingo\nShell")
sort=input("What sorting algorithm would you like to use?: ").lower()
datatyp=input("Whould you like to input your own data?(otherwise a random set will be generated): ").lower()
if datatyp=="yes" or datatyp=="data" or datatyp=="enter data" or datatyp=="enter":
    done=False
    while not done:
        try:
            data=[]
            datainput=input("Please enter your data(Ex: 4,5,3,1,1):\n")
            temp=""
            print(datainput)
            for i in str(datainput):
                if i!=",":
                    temp+=i
                else:
                    data.append(int(temp))
                    temp=""
            data.append(int(temp))
            done=True
        except:
            print("Something went wrong try again")


    
else:
    done=False
    while not done:
        try:
            data=[]
            for i in range(int(input("How many numbers would you like: "))):
                data.append(random.randint(0,999))
            done=True
        except:
            print("Something went wrong try again")

show=input("Would you like to be shown step by step?: ").lower()
if show=="yes":
    show=True
if show=="no":
    show=False
    print(data)
if sort=="bubble" or sort=="bubblesort" or sort=="bubble sort":
    output=bubble(data,show)
    time1=t.time()
    bubble(data,False)
    time2=t.time()
if sort=="insertion" or sort=="insertionsort" or sort=="insertion sort":
    insertion(data,show)
    time1=t.time()
    insertion(data,False)
    time2=t.time()
if sort=="selection" or sort=="selectionsort" or sort=="selection sort":
    output=selection(data,show)
    time1=t.time()
    selection(data,False)
    time2=t.time()
if sort=="quick" or sort=="quicksort" or sort=="quick sort":
    output=quick(data,show)
    time1=t.time()
    quick(data,False)
    time2=t.time()
if sort=="merge" or sort=="mergesort" or sort=="merge sort":
    output=merge(data,show)
    time1=t.time()
    merge(data,False)
    time2=t.time()
if sort=="counting" or sort=="countingsort" or sort=="counting sort":
    output=counting(data,show)
    time1=t.time()
    counting(data,False)
    time2=t.time()
if sort=="radix" or sort=="radixsort" or sort=="radix sort":
    output=radix(data,show)
    time1=t.time()
    radix(data,False)
    time2=t.time()
if sort=="bingo" or sort=="bingosort" or sort=="bingo sort":
    output=bingo(data,show)
    time1=t.time()
    bingo(data,False)
    time2=t.time()
if sort=="shell" or sort=="shellsort" or sort=="shell sort":
    output=shell(data,show)
    time1=t.time()
    shell(data,False)
    time2=t.time()
print(output)
print(f"Time: {round((time2-time1)*1000,4)} milliseconds")




