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

# def ... 

#x="helloSir"
#y="hiThere"


def string_compare(x,y): 
    if x==y: 
        return True

"""
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument. 
"""


# def ... 

def string_append(x,y): 
    print(x+y)

#string_compare(x,y)
#string_append(x,y)

"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 
"""
"""

# def ...
i= len(x)

"""

def first_five_letters(x):
    firstFive = x[0: 5]
    return firstFive

#first_five_letters(x)
"""
Problem 4
Write a function called "calculate_shipping_costs".

It should take two integer arguments, "total_packages" and "total_weight".

It should return the product of "total_packages" and 12.50
when "total_weight" is less than 50. 

It should return the product of "total_packages" and 19.75
when "total_weight" is 50 or more. 
"""

# def ...

#total_packages=2
#total_weight=49
def calculate_shipping_costs(total_packages,total_weight):
    if(total_weight<50):
        prod = total_packages*12.5
        return prod
    elif(total_weight>=50): 
        prod = total_packages*19.5
        return prod 

#calculate_shipping_costs(total_packages,total_weight)

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

# def ...
def favorite_color(name):
    if(name=="Jack" or name=="Michelle"):
        return "Blue"
    if(name=="Jesse"):
        return "Purple"
    if(name=="Sami"):
        return "Seafoam"
    else:
        return "Black"

#favorite_color("Jesse")
#print(favorite_color("Jesse"))




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

# def ...


def is_spam(subject):
    if("Greeting , " in subject):
        return True
    if("Special Offer !" in subject):
        return True
    if("Re: Fwd: Coupons" in subject):
        return True
    else:
        return False


#print(is_spam("≤å®ßmek.arsrs;lkgnal;ngn"))
