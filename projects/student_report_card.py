headline = "Welcome to student report card system"

print(headline.center(40))



def validmarks(subject):
 while True:
  print("Enter your score " + subject )
  mark = int(input())
  if(mark>100 or mark<0):
   print("invalid")
  else:
   return
  
english = validmarks("english")
maths = validmarks("maths")
history = validmarks("history")
science = validmarks("science")
computer = validmarks("computer")
  



  


 



  





 



 
