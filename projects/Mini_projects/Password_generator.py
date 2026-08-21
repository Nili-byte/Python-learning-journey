import random
import string

lower = list(string.ascii_lowercase)

upper = list(string.ascii_uppercase)

digits = list(str(string.digits))

spec_char = list(string.punctuation)



wl = lower + upper + spec_char + digits
password = ""
while True:
    try:
            usrlen = int(input(("Enter the length of your password : ")))
            break
    except(ValueError):
          print("Invalid! Try again : ")

for i in range(usrlen):
    i = random.choice(wl)
    password = password + i

print("Your Password has been generated -", password)    
#BYE
      




    
