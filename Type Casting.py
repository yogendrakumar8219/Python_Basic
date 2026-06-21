"""a = 5        # int
b = 2.5      # float
c = a + b    # int + float → float
print(c)     # 7.5
print(type(c))"""

x = "100"
y = int(x)          # string → int
z = float(y)        # int → float
print(y, type(y))   # 100 <class 'int'>
print(z, type(z))   # 100.0 <class 'float'>

# Another example
a = 10
print(str(a))       # "10"
print(bool(a))      # True