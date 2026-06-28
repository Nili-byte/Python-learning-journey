l = [1,2,3,4,5,6,7,8,9,99,88,34,232,12,32,444,999,786,9999,567392]

# r = list(map(lambda x: x**3, l)) #this goes to all interate and does what def is told

# print(r)


# a = list(filter(lambda s: s>=60,l)) # this verify the condition in function if true then he shows output
# print (a)




from functools import reduce

x = reduce(lambda c,n : c*n,l)
print (x)