list=[1,2,3,4,5,6,7,8,9,0]
love=list[:]
love.append(10)
list.append(12)
print(list)
print(love)
print("the first three item of the list are:")
for value in list[:3]:
    print(value)
print("the middle three item of the list are:")
for value in list[3:6]:
    print (value)
print("the last three item of the list are:")
for value in list[-3:]:
    print(value)
for value in list[:]:
    print(value)
for value in love [:]:
    print(value)
