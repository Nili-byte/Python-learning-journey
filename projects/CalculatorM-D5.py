print("hello world")

H = "Welocme to menu calculator"

print(H.center(50))


c = 0

print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = EXIT")
while(5!=c):
    c = int(input("choose the operation by inputting coresponding digit\n"))
    if(c == 1):
     a = int(input("Enter you 1st numbers : "))
    
     b = int(input("Enter you 2nd numbers : "))
   
     print(int(a)+int(b))

    elif(c == 2):
     a = int(input("Enter you 1st numbers : "))
    
     b = int(input("Enter you 2nd numbers : "))
   
     print(int(a)-int(b))

    elif(c == 3):
     a = int(input("Enter you 1st numbers : "))
    
     b = int(input("Enter you 2nd numbers : "))
   
     print(int(a)*int(b))

    elif(c == 4):
     a = int(input("Enter you 1st numbers : "))
    
     b = int(input("Enter you 2nd numbers : "))
   
     print(int(a)/int(b))

    else:print("Thankyou for using our servies")