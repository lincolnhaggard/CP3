import random
from operator import attrgetter
li = (9,1,4,6,4,8,1,3,5,7,8,6,2,4,9,6,1)
#for i in range(1000000):
#    li.append(random.randint(1,i+2))
slist = sorted(li)
#print(slist)


class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return "({},{},${})".format(self.name,self.age,self.salary)


e1 = Employee("Carl",37,70000)
e2 = Employee("Sarah",29,80000)
e3 = Employee("John",43,90000)


employees=[e1,e2,e3]
def e_sort(emp):
    return emp.age
s_employees=sorted(employees,key=attrgetter("age"),reverse="string")

print(s_employees)