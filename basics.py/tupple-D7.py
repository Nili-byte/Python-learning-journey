print("hello world")

t = (1, 2, 3, 4, 5, "apple")
print(type(t))


# tupple are immutable they cannot be change same as constant

a=(2,3,5,7,55,22,11,34,5,6)
print(type(a))

a = list(a)
print(type(a))

a.append(999)
print(a)

a = tuple(a)
print(a)

b = (1,2,3,4,399,5,6,399.7,888,7,)



c = a + b
print(c)

print(b.index(888))
print(b.index(399,3,5))

print(b.count(7))