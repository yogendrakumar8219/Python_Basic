import os
os.system('cls')
c= input("Are you citizen of India (Y/N)")
age=int(input("Enter your age :"))
citizen=False
if c=="Y" or c=="y":
    citizen=True
else:
    citizen=False
if age >=18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Under age")