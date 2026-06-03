   

# f0 = 0
# f1 = 1
#fn = fn-1 + fn -2


def fibo(i):

   if(i==0):
      return 0
   elif(i==1):
      return 1
   else:
      return fibo(i-1)+fibo(i-2)
   

print(fibo(8))
   



