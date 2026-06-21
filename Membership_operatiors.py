# With strings
print("p" in "apple")       # True
print("z" not in "apple")   # True

# With lists
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)       # True
print("grape" not in fruits)    # True

# With dictionaries (checks only keys by default)
my_dict = {"name": "John", "age": 30}
print("name" in my_dict)        # True
print("John" in my_dict)        # False (because it checks keys, not values)
print("John" in my_dict.values())  # True