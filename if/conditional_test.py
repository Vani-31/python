car = 'subaru'
print("Is car =='sabaru'? I predict True.")
print(car=='subaru')

print("\nIs car=='audi'? I predict False.")
print(car == 'audi')



age= int(input("\nenter age: "))
if(age>18):
    print("Hurry! you are eligible to drive.")
elif(age==18):
    print("you just got eligible to drive ")
else:
    print(" sorry you need to wait to get 18 . then you can drive")


name= input("enter user name :")
if(name.lower()=="vani"):
    print(f"Hello{name}, good to see you again .")
else:
    print("invalid username. TryAgain  .")


grade=int(input("Enter Grade:"))
if (grade>90 and grade<100):
    print("A grade")
elif (grade>80 and grade<90):
    print("B grade")
elif (grade>70 and grade<80):
    print("C grade")
elif (grade>60 and grade<70):
    print("D grade")
elif (grade>50 and grade<60):
    print("E grade")
elif (grade>0 and grade<50):
    print("F grade")


a="apple"
if(a=="mango"):
    print()
