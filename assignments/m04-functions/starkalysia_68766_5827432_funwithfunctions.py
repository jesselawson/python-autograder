"""
Module 04 Assignment: "Fun with Functions"

Alysia Stark 
CIS 157 - Intro to Python Programming 
CCC Spring 2020
Professor Jesse Lawson


OVERVIEW
================================================================================

This file contains six programming problems that involve writing functions 
from scratch. 

"""

"""
Problem 0
Write a function called "hello_world".
It should take one string argument, "name".
It should print "Hello {name}, and hello world!"
"""

def hello_world(name):
    print(f"Hello {name}, and hello world!")

hello_world("Oliver")
"""
Problem 1
Write a function called "string_compare".
It should take two string arguments.
It should return True if both strings are equal.
It should return False if both strings are not equal.
"""

def string_compare(str1, str2):
    if str1 == str2:
      return True
    else:
      return False

print(string_compare("dog", "cat"))


""" 
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument. 
"""

# Solution #1
def string_append(arg1, arg2):
    new_string = (arg1 + arg2)
    return new_string

print(string_append("Jennifer ", "let the dogs out."))

# Solution #2
def string_append2(arg3, arg4):
    new_string2 = " ".join((arg3, arg4))
    return new_string2

print(string_append2("Andy", "has left for the day."))

"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 
"""

def first_five_letters(word1):
    return word1[:5]

print(first_five_letters("Unbelievable"))

"""
Problem 4
Write a function called "calculate_shipping_costs".

It should take two integer arguments, "total_packages" and "total_weight".

It should return the product of "total_packages" and 12.50
when "total_weight" is less than 50. 

It should return the product of "total_packages" and 19.75
when "total_weight" is 50 or more. 
"""

def calculate_shipping_costs(total_packages, total_weight):
    if total_weight < 50:
       return (total_packages * 12.50)
    elif total_packages >= 50:
       return (total_packages * 19.75)

print(calculate_shipping_costs(51, 300))

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

def favorite_color(name):
    if name == "Jack" or name == "Michelle":
       return "Blue"
    elif name == "Robert":
       return "Green"
    elif name == "Jesse":
       return "Purple"
    elif name == "Sami":
       return "Seafoam"
    else:
       return "Black"


print(f"Michelle's favorite color is {favorite_color('Michelle')}")

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

def is_spam(subject):
    greeting = "Greeting" 
    coupons = "Re: Fwd: Coupons"
    sp_offer = "Special Offer !"
    if greeting in subject:
       return True
    elif coupons in subject:
       return True
    elif sp_offer in subject:
       return True
    else:
       return False

#Testing...
print(is_spam("Special Offer ! Don't wait"))
print(is_spam("Re: Fwd: Coupons Inside"))
print(is_spam("Greetings Dear citizens:"))
print(is_spam("Special offer!"))
print(is_spam("Coupons inside"))
print(is_spam("Anything else"))