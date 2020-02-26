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
x = 'Hello world'
y = 'Hello world'

if x == y:
    print("true")

else:
    print("false")


""" 
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument. 
"""

str1 = ' red'
str2 = 'The dog was the color'
print(str2 + str1)


"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 
"""

varA = '123456789'[:5]
print(varA)

"""
Problem 4
Write a function called "calculate_shipping_costs".

It should take two integer arguments, "total_packages" and "total_weight".

It should return the product of "total_packages" and 12.50
when "total_weight" is less than 50. 

It should return the product of "total_packages" and 19.75
when "total_weight" is 50 or more. 
"""

total_packages = 10
total_weight = 51

if total_weight > 50:
    print(total_packages + 12.50)

if total_weight <= 50:
    print(total_packages + 19.75)

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
name = 'Jack'
if name == 'Jack' or 'Michelle':
    print('Blue')
elif name == 'Robert':
    print('Green')
elif name == 'Jesse':
    print('Purple')
elif name == 'Sami':
    print('Seafoam')
else:
    print('black')
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

str_subject = 'Special offer !'
if str_subject == 'Special offer !' or 'Re: Fwd: Coupons' or 'Greeting , ':
    print('true')








