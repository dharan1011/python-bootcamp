"""
Code Hosted @ Github

Repo Link : 

Agenda:
    1. Basic Data Structures in Python
    2. Variable
    3. Basic Operators
    4. Little Bit About Strings
"""

"""
Compiled:
    1. Code in compile -> reports error
    2. Running the code

Interpreted:
    1. Execute the code on the fly
"""

"""
Giving instruction to the computer to get some work done
"""

"""
Primitive Data Structures

Integer: [-inf, inf] -> 1, 9, 99, -99
Float: 1.0, 2.0, -9.0, 9.333333, 10.342151
String: "vinay", "is", "23"
Boolean: True, False

These are container which store a homogenous set of data
"""

"""
Variable are used to refer the stored data

LHS = RHS
variable_name = 1 or 1.0 or "vinay"

"""

# Write a program to store age name and print them
age = 23
name = "vinay"
print(age, name)

# Write a program to convert 23 celsius to fahrenheit
# F = C * (9/5) + 32

temp_in_cel = 23
temp_in_far = temp_in_cel * (9/5) + 32
print(temp_in_far)

"""
Int, Float :
+ : add
- : subtract
* : multiply
/ :  float division
// : integer
"""

"""
String:
+ : Concatenation
"""

first_name = "vinay"
last_name = "karaka"
full_name = first_name + last_name
print(full_name)

"""
Boolean:
    And, Or, Not

T And T = T
T And F = F
F and T = F
F and F = F

T Or T = T
T Or F = T
F Or T = T
F Or F = F

Not T = F
Not F = T
"""

# Write a program to print person name if he is alive
person_name = "Vinay Karaka"
is_alive = True
if is_alive:
    print(person_name)
else:
    print("RIP")


