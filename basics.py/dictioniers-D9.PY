dic = {"Apple": "120rs", "mango" : "180rs", "pineapple" : "180rs"}

print(type(dic))
print(dic)

print(dic.get("mango"))

dic.update({"banana":"60rs"})
print(dic)


# dic.clear() #this clear the dictioneries

print(dic.keys())# this will print all keys from dic
print(dic.values())#this prints value from dic

dic.update({"Mac":"200k"})


dic.pop("Mac")#this remove a single or pop
print(dic)


for value in dic.values():
    print(value)



# print(dic.popitem())#this removes the last added dic item
# print(dic)

del dic