import os
os.system('cls')
total_no = int(input("Enter total five subject number"))
per = total_no*100/500
print(f"% markes={per:.2f} ")
if per >100:
    print("Invalid total number")
elif per<=100  and per >=60:
    print("Ist division")
elif per<60 and per >=45:
    print("2nd division")
elif per<45 and per>=33:
    print("3rd division")
else:
    print("fail")
