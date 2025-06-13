current_users=["vani","dhruv","shridhi","pawani","gaurav"]
new_users=["dhruv","shira","jinya","Gaurav","shivay"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Enter new username")
    else:
        print("username available")
