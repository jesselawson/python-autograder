"""
Module 04 Assignment: "Fun with Functions"

OVERVIEW
================================================================================

This file contains six programming problems that involve writing functions
from scratch.

Remember that you have to copy and paste this assignment into a file on your
local machine, save that file as "funwithfunctions.py", then upload that file
to the Canvas assignment.

DIRECTIONS
================================================================================

Each of the six Problems you are expected to finish have specifications ("specs")
inside a code block, followed by a placeholder block of code where I want you
to write the function that satisfies the specs. This is exactly how the mid-term
and final examinations will take place--big files like this with a problem
written in comments and then a section immediately after where you are to
write your answer--in the form of code, of course.

Follow the directions, paying close attention to what is being asked, the
logical conditions, and the expected outcomes. Each Problem requires you to
write a separate function specific to that problem.

I have provided an example called "Problem 0".

When you are finished, upload the complete file on the Canvas assignment page.

"""

"""
Problem 0
Write a function called "hello_world".
It should take one string argument, "name".
It should print "Hello {name}, and hello world!"
"""

def hello_world(name):
    print(f"Hello {name}, and hello world!")


"""
Problem 1
Write a function called "string_compare".
It should take two string arguments.
It should return True if both strings are equal.
It should return False if both strings are not equal.
"""

def string_compare():
    a = "1"
    b = "2"
    if a == b:
        print("true")
    else:
        print("False")

"""
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument.
"""

def string_append():
    a = "2"
    b = "4"
    return a+b
"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument.
It should return the first five letters of the string argument.
"""

def first_five_letters():
    a = "rendezvous"
    return a[:5]

"""
Problem 4
Write a function called "calculate_shipping_costs".

It should take two integer arguments, "total_packages" and "total_weight".

It should return the product of "total_packages" and 12.50
when "total_weight" is less than 50.

It should return the product of "total_packages" and 19.75
when "total_weight" is 50 or more.
"""

def calculate_shipping_costs():
    total_packages = 15
    total_weight = 60
    if total_weight < 50.0:
        return total_packages+12.50
    elif total_weight >= 50.0:
        return total_packages+19.75
"""
Problem 5
Write a function called "favorite_color".
It should take one string argument, "name".
It should return "Blue" when "name" is "Jack" or "Michelle".
It should return "Green" when "name" is "Robert".
It should return "Purple" when "name" is "Jesse".
It should return "Seafoam" when "name" is "Sami".
It should return "Black" in any other case.
"""

def favorite_color():
    name = input()
    if name == "Jack" or "Michelle":
        return "Blue"
    elif name == "Robert":
        return "green"
    elif name == "Jesse":
        return "Purple"
    elif name == "Sami":
        return "Seafoam"
    else:
        return "Black"



"""
Problem 6
Write a function called "is_spam".
It should take one string argument, "subject".
It should return True if any of the following are true:
    * "subject" contains the string "Greeting , "
    * "subject" contains the string "Re: Fwd: Coupons"
    * "subject" contains the string "Special Offer !"
(pay attention to special characters and spaces in this one!)

"""

def is_spam():
    subject = "Greeting , "
    if subject == "Greeting , ":
        return True
    elif subject == "Re: Fwd: Coupons":
        return True
    elif subject == "Special Offer !":
        return True    
