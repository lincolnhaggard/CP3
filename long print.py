import time
canvas=(40,20)
#"\033c"+
sr="\033c"+((" "*canvas[0])+"|\n")*canvas[1]
totalsr=""
x=0.0
y=0.0
vx=0.02
vy=0.01
for i in range(10000):
    newsr=sr
    newsr=newsr[:int(x)+(int(y)*(canvas[0]+2))+2]+"■"+newsr[int(x)+(int(y)*(canvas[0]+2))+3:]
    x+=vx
    y+=vy
    if x>=canvas[0]-2:
        vx*=-1
    if x<=0:
        vx*=-1
    if y>=canvas[1]-1:
        vy*=-1
    if y<=0:
        vy*=-1
    #print(newsr)
    totalsr+=newsr
    #time.sleep(0.1)
print(totalsr)