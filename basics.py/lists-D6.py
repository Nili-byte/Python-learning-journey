print("hello world")

A = [1 , 4 , 5 ,8 ,8 ,6,5,4,3,3,5,0 ,8,]
print(A)
print(A[3])

if 0 in A:
    print("yes")
else:
    print("no")    

b =[1.2,3,3,4,5,6,7,8,9,0,]


b.append(899)
print (b)

b.insert(1 , 299)
print(b)

b.extend(A)

print(b)


c = [2,4,6,88,99,34,23,6,6,6,6,]

c.sort()
print(c)
c.sort(reverse=True)
print(c)


print(c.count(6))

e = ["apple" , "banana" , "mango"]
print(e.index("apple"))
