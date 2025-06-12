#this this a smart greeting chatbot which stops only when you write exit as a name 
while True:
    name=input("what is your name?")

    if name.lower()=="exit":
        print("goodbye:)")
        break
    age=int(input(f"what is your age {name} ?"))
    hobby=input("what do you like to do in free time ?")
    fav_lang=input(f"what is your favorite language {name}?")
    message =f"hey {name}, i hope you doing well. You like to {hobby} in your free time . you are {age},"
    if(age<18):
        message=message+"Still in school? Keep learning! "
    else:
        message=message+"Great time to level up your tech skills! "
    if(fav_lang.lower()=="python"):
        message=message+"and you like python ! welcome to python team."
    else:
        message=message+f"and you like {fav_lang} . great choice, {name} !"
    print(message)
