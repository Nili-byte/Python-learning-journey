# class Data:
#     Name = "Nihal"
#     age = "18"
#     occupation = "Learner"


# r = Data()
# print(r.Name , r.age)
# print(r.occupation)

# r.Name = "rahul"
# print(r.Name , r.age)


class Student():
    def __init__(self,Name,surname ,age):
     self.Name = Name
     self.surname = surname
     self.age = age


a = Student("Mehul","bhaliya","18")
print(a.Name , a.surname)


a2 = Student("Satyam","Yadav","18")
print(a2.Name , a2.surname)


