# """
#   *
#  ***
# ***** 
# when n = 3
# """




# # a = int(input("Enter your number: "))
# # for i in range(1,a*2,2):
# #  print(" "*(((2*a)-i)//2),end = "")
# #  print("*"*i,end = "")
# #  print("\n")


# r = int(input("Enter your number: "))
# for t in range(1,r+1):
#     if(t==1 or t==r):
#         print("*"*r,)
#     else:
#         print("*",end="")
#         print(" "*(r-2),end="")
#         print("*")





class palace:
    amenities_pre = "swiming pool , gym , Ac , housekeeping, sea facing window"
    amenities_nor = "AC, WIFI , HOUSEKEEPING"
    apt_avaible = 0
    def __init__(self, _type , category , price ):
        self._type = _type
        self.category = category
        self.price = price
        
        palace.apt_avaible  += 1




apt1 = palace("Normal(1bhk)","couple",3000)
print(apt1.price)
print(apt1._type)
print(apt1.category)
print(apt1.amenities_nor)

print("-"*30)
apt2 = palace("premium(3bhk)","all",9002)
print(apt2.price)
print(apt2._type)
print(apt2.category)
print(apt2.amenities_pre)





apt3 = palace("suite(4bhk with balcony)","no requiment","14999rs")
print(apt3._type,apt3.apt_avaible,apt3.amenities_pre,apt3.price)






print("apt_vacant =",palace.apt_avaible)




# inhentirance is not that hard and its easy to remeber so i didn't code i just wotched the therory

