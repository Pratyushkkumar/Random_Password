import random
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_"
pass_length=int(input("Enter Length of the password :"))
pass_count=int(input("Enter No of the password :"))
print("The generated passwords are :")
print("\n")
for i in range(0,pass_count):
    password=""
    for j in range(0,pass_length):
        pass_char=random.choice(char)
        password+=pass_char
    print(password)
