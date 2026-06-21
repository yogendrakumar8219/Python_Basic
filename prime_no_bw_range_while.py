import os
os.system('cls')
x =int(input("Enter starting point"))
y =int(input("Enter end point"))
while x<=y:
    i=2
    while i<x:
        r=x%i
        if r==0:
            break
        i += 1
    if i==x:
        print(x)
    x += 1

