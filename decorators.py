#decorators add onto the function

def cough(func):


    def func_wrapper():
        #stuff before the function
        print("*cough*")
        func()

        #stuff after the function
        print("*cough*")
    return func_wrapper

@cough
def awkward():
    print("Can I get a discount?")

@cough
def answer():
    print("This is a dollar tree. . . ")

awkward()
answer()