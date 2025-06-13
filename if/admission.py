age= int(input("enter age :"))
if age<4:
    price=0
elif age>=4 and age<18:
    price=10
else:
    price=45
print(f"As your age is {age} therefore your admission price will be {price} US Dollar.")