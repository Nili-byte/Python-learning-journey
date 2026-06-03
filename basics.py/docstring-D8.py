print("hello world")

def doc (x):
    "so here we will derive cube of any number"
    a = int(input("enter number: "))
    print(a**3)

doc(1)
print(doc.__doc__)
