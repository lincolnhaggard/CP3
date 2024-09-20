import random

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
    #Something
    time=0
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
    bubble(data)


