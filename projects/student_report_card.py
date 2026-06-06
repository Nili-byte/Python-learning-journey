def validmarks(sub):
    while True:
        mark=int(input(f"Enter your {sub} mark (0-100): "))
        if(mark<0 or mark>100):
            print("Invalid")
        else:
            return mark

def avg(marks):
    total = sum(marks)/len(marks)
    return total


def grade(total):
    if(total>=90):
        return "A"
    elif(total>=80):
        return "B"
    elif(total>=70):
        return "C"
    elif(total>=60):
        return "D"
    elif(total>=50):
        return "E"
    else:
        return "F"
    
def report(name , subjects , average , grade , result):
    print("="*30)
    heading = "Welcome to report card system summary generater"
    
    print(heading.center(50))
    print("="*30)
    print(f"Name:{n}")
    print("="*30)
    print(f"English :", marks[0])
    print(f"Maths :", marks[1])
    print(f"Physics :", marks[2])
    print(f"Chemsitry :", marks[3])
    print(f"CS. :", marks[4])
    print("="*30)
    print(f"Score : {sum(marks)}/500")
    print(f"Percentage : {score}%")
    print(f"Grade : {grd}")
    if(score<35):
        print(f"Status : Failed")
    else:
        print(f"Status : Passed")
    print("")
    print("="*30)




marks = []
while True:
    n = input("Enter your name: ")

    marks.append(validmarks("English"))
    marks.append(validmarks("Maths"))
    marks.append(validmarks("Physics"))
    marks.append(validmarks("Chemistry"))
    marks.append(validmarks("CS"))

    
    score = avg(marks)
    grd = grade(score)



    r = report("name","subject","grade","result","average")

    print(r)
    
    ans = input("Add another(yes/no)")
    if(ans == "no"):
        break
   



















  



  


 



  





 



 
