# f = open("example.txt","w")
# s = f.write()
# f.close()   #write also create a file if not already exist same as create


f = open("example.txt","w")
s = f.write("Hello world this just overwites every thing")
f.close()



a = open("example.txt","a")
r = a.write(" yo i was added by append")
a.close()

with open("Again.txt","a") as test:
 test.write("YO im shortcut")