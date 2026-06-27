a = 9 # this is global varibale can be used anywhere

def hello():
    
    global a
    a = 16
    b = 9  # both 4-5 lines are local variable can be only use in function
    print(a)


hello()