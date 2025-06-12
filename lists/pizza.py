pizzas=["margarita","farmfresh","corn pizza"]
for pizza in pizzas:
    print(f"I like {pizza}")
print(f"i like {pizzas[2]} soo much ")
print("i like corns and onion in pizza")
print("i like thin  crust pizza")
print("i really love pizza!!!")
my_friendpizza=pizzas[:]
pizzas.append("onion")
my_friendpizza.append("capcicum")
print("my pizzas are :")
for value in pizzas[:]:
    print(value)
print("my friend pizza are :")
for value in my_friendpizza[:]:
    print(value)