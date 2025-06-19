fav_lang={
    "sarah":"c",
    "pawani":"ruby",
    "shridhi":"python",
    "vani":"c++",


}
people=["kavita","sarah","satakshi","janvi","shridhi"]
for name in people:
    if name in fav_lang:
        print(f"thankyou {name} for responding the mail")

    else:
        print(f"{name} please take the poll.")