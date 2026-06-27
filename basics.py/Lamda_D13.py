square = lambda x: x**3
while True:
 
 try:
  A = float(input("Enter your number for calculating its cube : "))
  break
 except ValueError:
  print("Invalid! numbers only!")

print(square(A))


  

 
