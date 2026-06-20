import random
import string

def randmchar():
    return random.choice(string.ascii_letters)


h = "Welcome to Private Messanger"
print(h.center(85))

print("Entrypt Msg (1)  ")
print("derypt Msg (2)  ")
print("TO Exit (0) ")
while True:
 choice = int(input("Enter the operation int : "))
 if(choice<0 or choice>2):
     print("Invalid : ")
 
    





 if(choice==1):

    c = input("Enter you Msg to Encode : ")

    words = c.split(" ")
    msg = []

    for word in words:
        if(len(word)<=3):
            msg.append(word[::-1])
        else:
            a = (word[1:]+word[0])
            anew = randmchar() + randmchar() + randmchar() + a + randmchar() + randmchar() + randmchar()
            msg.append(anew)  

    print(" ".join(msg))

 elif(choice==2):

        c = input("Enter you Msg to Decode : ")

        words = c.split(" ")
        msg = []

        for word in words:
         if(len(word)<=3):
            msg.append(word[::-1])
         else:
            shave = word[3:-3]
            a = shave[-1]+(shave[:-1])
            anew = a
            msg.append(anew)

        print(" ".join(msg))
    
 
 elif(choice==0):
    print("Thankyou for using our tool")
    break
        
