# f = open("example.txt","w")
# s = f.write()
# f.close()   #write also create a file if not already exist same as create


# f = open("example.txt","w")
# s = f.write("Hello world this just overwites every thing")
# f.close()



# a = open("example.txt","a")
# r = a.write(" yo i was added by append")
# a.close()

# with open("Again.txt","a") as test:
#  test.write("YO im shortcut")



# with open("Data.txt","x") as d:
#     d.write("Hello Nihal!")

i = 0
with open("Data.txt","r") as d:
    while True:
        i+=1
        
        r = d.readline()
        if not r:
                break
        d1 = r.split(",")[0]
        d2 = r.split(",")[1]
        d3 = r.split(",")[2]
        print(f"The marks of english of student {i} is {d1}")
        print(f"The marks of Maths of student {i} is {d2}")
        print(f"The marks of Physics of student {i} is {d3}")

        
print("Processed Completed")



with open("example.txt") as t:
     t.seek(6) #this just ignore the 6 letter or put my cursor on 6
     apple=t.read(5) #this just reads ahead of 5
     print(t.tell())
     print(apple)
     print(t.truncate(32))




  
