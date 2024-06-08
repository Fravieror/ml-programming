import math

def remainder(a,b):
    return a % b

def hello_there(name_input_here):
    return f"Hello there, {name_input_here}"

def radius(radius):
    return math.pi*radius**2

a = int(input("num 1: "))
b = int(input("num 2: "))
print(remainder(a,b))

print(hello_there(input("your name: ")))
print(radius(2))


