import os
os.system('cls') #windows
name="Pakhi"
age=12
#using f-string
print(f"My name is {name} and I am {age} years old.")
#.format() method
print("My name is {} and I am {} year old.".format(name,age))
#using index numbers
print("My name is {0} and I am {1} year old.".format(name,age))
#using name arguments
print("My name is {n} and I am {a} year old.".format(n=name,a=age)) 
#using % formatting
print("My name is %s and I am %d year old." %(name,age))
pi=3.14159
print("Value of pi is %.2f" %pi) #rounding to 2 decimal places