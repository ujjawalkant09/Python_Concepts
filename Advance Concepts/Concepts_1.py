# Basic  unpacking
a,b,c = [1,2,3]
print(f"a: {a}, b: {b}, c: {c}\n")

# Extend Trerable Unpacking with *

a,b,*c = [1,2,3,4,5,6,7,8]
print(f"a: {a}, b: {b}, c: {c}\n")

a,*b,c = [1,2,3,4,5,6,7,8]
print(f"a: {a}, b: {b}, c: {c}\n")


# Ignoring Values
# Use _ (inderscore)
a,_,c = [1,2,3]


# Unpacking Nested Structures
data = ("Alice",(25,"Engineer"))

name,(age,profession) = data

print(f"name : {name}, profession : {profession}, age : {age}")


# Unpacking in function arguments

def print_name(*names):
    for name in names:
        print(name)

print_name("Alice","Bob","Charlie",[1,2,43])

# Combining Lists with unpacking
list1 = [1,2,3]
list2 = [4,5,6]

combined = [*list1,*list2]
print(f"Combined List : {combined}\n")

# Unpacking Dictionaries with **
dict1 = {"a":1,"b":1}
dict2 = {"c":1,"d":1}
combined_dict = {**dict1,**dict2}
print(f"combined dct : {combined_dict}\n")