"""
Functions is Block of code which runs when called.
Functions can take input and can also return a output

def function_name([parameters]):
    code
    [return value]
"""

def greet_user(name):
    print("Hello, ", name)

def add_numbers(x, y):
    return x + y

def square_number(x):
    sqr = x * x
    return sqr

def rectangle_area(l, w):
    area = l * w
    return area

def get_pi():
    return 3.14

def get_user_info(name, age, sex = "male"):
    print(name,"is",sex,"and is",age,"years old")


greet_user("Vinay")
print(add_numbers(10,11))
print(square_number(5))
get_user_info("Vinay", 23, "female")
get_user_info(age = 23, name="Danesh", sex = "female")



