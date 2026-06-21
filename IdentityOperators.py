a = [1, 2, 3]
b = a          # both refer to same list in memory
c = [1, 2, 3]  # same values but different object

print(a is b)        # True  (same object)
print(a is c)        # False (different objects, even if values match)
print(a == c)        # True  (values are equal, but not same object)
print(a is not c)    # True  (different objects)

my_var = None
if my_var is None:
    print("Variable is None")