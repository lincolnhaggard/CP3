from robot import Robot
import time
robot=Robot(5,9)
correct=[3,1,2,1,3]
guesses=0
while len(robot.posibles)>1:
    guess=robot.getguess()
    check=[False]*5
    guesses+=1
    for x,i in enumerate(guess):
        user=input(f"Is {i} the correct one for the {x+1} place(y/m/n): ")
        if user=="y":
            check[x]=True
        elif user=="m":
            check[x]=None
    robot.addguess(guess,check)
    print(guess)
    print(check)
    time.sleep(1)
    del guess
    del check
print(guesses)
print(robot.posibles)
