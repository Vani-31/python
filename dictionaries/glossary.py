glossary={
    "loop":"looping is a property where you go to all element one by one but not manually",
    "break":"use to break the loop",
    "list":"they are array like in which you can store anything ",
    "range":"it gives you range between numbers",

}

   
glossary["set"]="it is a collection of unique data "

for key,value in glossary.items():
    print(f"\nWord : {key}")
    print(f"Meaning : {value}")