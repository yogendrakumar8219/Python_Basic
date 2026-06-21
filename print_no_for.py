import os
os.system('cls')
x =int(input("Enter starting point"))
y =int(input("Enter end point"))
for num in range(x,y+1):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num>1:
        print(num)