#pro1:
def greet_user(name):
    print(f"hello,{name}")
    
greet_user("john")
print()

#pro 2:
def greet_user(name="guest"):
    print(f"hello,{name}")
    
greet_user()
greet_user("john")
print()

#pro 3:
def calculate_area(length,breadth):
    return length*breadth

area=calculate_area(5,3)
print(f"area of rectangle is {area}")
print()
