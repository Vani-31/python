age=int(input("enter age :"))
if age<2:
    print("person is a baby")
elif age>=2 and age<4:
    print("person is toddler")
elif age>=4 and age<13:
    print("person is a kid")
elif age>=13 and age<20:
    print("person is a teenager.")
elif age>=65:
    print("person is elder")