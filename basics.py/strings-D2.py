print("hello world")
A = "apple is red"
print(len(A)) #len() is used to find length
print(A[0:5]) # here 0 to 5 means print print 5 letter starting from 0 , not counting 5th


# negative slicing

a = "harry"
print(a[-3:-2])
# here -3 so a is 5 letter we subtravt 3 then 2
# by that we get new index [2:3 so it print 2:3]


print(a.upper())
print(a.lower())
print(a.capitalize())

print(a.center(44))
print(len(a.center(44)))

print(a.isalnum())
print(a.isalpha())
b = "!!!nihal898@@@"
print(b.isalpha())



print(b.islower())
print(b.isupper())

print(b.rstrip("@"))

c = "i got my eyes on you"
print(c.split())

d = "love"
print(d.replace( "love"  ,"more love"))

print(d.find("o"))
print(d.endswith("e"))

print(d.startswith("d"))

print(d.index("e"))

print(c.title())

print(c.count("o"))

N="Nihal is coding"
print(N.endswith("is", 0 , 8))



