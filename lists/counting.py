# for value in range(1,21):
#     print(value)
# one_million=list(range(1,1000001))
# for value in one_million:
#     print(value)
# print(min(one_million))
# print(max(one_million))
# print(sum(one_million)) 
# odd_no=list(range(1,20,2))
# for value in odd_no:
#     print(value)
# threes=list(range(3,31,3))
# for value in threes:
#     print(value)
# threes=[value*3 for value in range(1,11)]
# for value in threes:
#     print(value)
# print(threes)
cubes=[]
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
print(cubes)
for value in cubes:
    print(value)
cubeess=[value**3 for value in range(1,11)]
print(cubeess)
