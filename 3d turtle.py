from math import *
t= turtle.Turtle()
t.tracer(0,0)
class point:
    def __init__(self,x,y,z):
        self.x=x
        self.ox=x/100
        self.y=y
        self.oy=y
        self.z=z
        self.oz=z/100
    def get_2d(self):
        return (self.x/sqrt(float(self.z)/50),self.y/sqrt(float(self.z)/50))
    def threeDToTwoD(self, point, cam):
        f = point[2] - cam[2]
        x = (point[0] - cam[0]) * (f / point[2]) + cam[0]
        y = (point[1] - cam[1]) * (f / point[2]) + cam[1]
        return (x, y) 
    
points=[point(100,100,250),point(-100,100,250),point(-100,-100,250),point(100,-100,250),
        point(100,100,50),point(-100,100,50),point(-100,-100,50),point(100,-100,50)
        ]
penup()
speed(0)
r=0
time=0

while True:
    r+=0.1
    time+=1
    cam=[0,0,0]
    for i in points:
        
        angle = radians(1)
        cos_val = cos(angle)
        sin_val = sin(angle)
        i.x -= 0
        i.z -= 150
        i.x = i.x * cos_val - i.z * sin_val - i.y * sin_val
        i.z = i.x * sin_val + i.z * cos_val - i.y * sin_val
        i.y= i.x * sin_val + i.z * sin_val + i.y * cos_val
        i.z+=150
    #print(points[0].z)
    for i in points:
        for k in points:
            color((i.x,i.y,i.z))
            goto(i.threeDToTwoD((i.x,i.y,i.z), cam)[0],i.threeDToTwoD((i.x,i.y,i.z), cam)[1])
            pendown()
            goto(k.threeDToTwoD((k.x,k.y,k.z), cam)[0],k.threeDToTwoD((k.x,k.y,k.z), cam)[1])
            penup()
    
    t.update()
    clear()