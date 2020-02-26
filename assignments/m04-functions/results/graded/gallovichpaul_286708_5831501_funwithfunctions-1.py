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

# Function that takes two string arguments "first_string" and "second_string" which passes them to the if statement to
# compare to see if they are equal. Prints or returns True if they match. Returns False if they do not match.
def string_compare(first_string, second_string):
    if first_string == second_string:
        return True
    else:
        return False
# Declare two variables to store the first and second string to pass to the function.
first_string = "Enter the string to compare."
second_string = "Enter the string to compare."

# Call the function to compare the first and second string to compare.
string_compare(first_string, second_string)


""" 
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument. 
"""

# Function that takes two string arguments "first_string" and "second_string" which passes them to be concatenated.
# Concatenated string is stored in a variable called "combined_string" which is printed to the screen.
def string_append(first_string, second_string):
    combined_string = first_string + ' ' + second_string
    return combined_string

# Declare two variables to store the first and second string to pass to the function.
first_string = "Simple is better than complex."
second_string = "Readability counts."

# Call the function to concatenate the first and second string.
string_append(first_string, second_string)

"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 
"""
# Function that takes a string argument called "first_string". It then prints the first 5 characters of the string
# using string slicing.
def first_five_letters(first_string):
    return(first_string[0:5])

# Declare variable to store the string to pass to the function.
first_string = "Enter the string."

# Call the function with the string that was typed in by the user.
first_five_letters(first_string)

"""
Problem 4
Write a function called "calculate_shipping_costs".

It should take two integer arguments, "total_packages" and "total_weight".

It should return the product of "total_packages" and 12.50
when "total_weight" is less than 50. 

It should return the product of "total_packages" and 19.75
when "total_weight" is 50 or more. 
"""

# Definition for function that takes user input and checks the condition to see if the total_weight is less than 50 or greater than
# or equal to 50. The function then calculates the shipping cost by multiplying total_weight times the constant value
# that is used in the if statement. The shipping cost is then printed.
def calculate_shipping_costs(total_packages, total_weight):
    if total_weight < 50:
        shipping_cost = total_packages * 12.50
        return shipping_cost
    if total_weight >= 50:
        shipping_cost = total_packages * 19.75
        return shipping_cost

# Declare two variables called "total_packages" and "total_weight" to store total number of packages and total weight.
total_packages = 1
total_weight = 49

# Call the function with the values entered by the user and convert to integer values.
calculate_shipping_costs(int(total_packages), int(total_weight))



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
# Definition for function that accepts a name and checks for a match based on the if statement below.
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

# Defines a variable to store the name typed in by the user.
name = "Jack"
# Calls the function named favorite_color and passes the name typed in by the user as a parameter.
favorite_color(name)

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
# Definition for function that accepts the variable subject and checks for a match based on the if statement below.
def is_spam(subject):
    if subject == "Greeting , ":
        return True
    elif subject == "Re: Fwd: Coupons":
        return True
    elif subject == "Special Offer !":
        return True
    else:
        return False
# Defines a variable called subject that stored the string typed in by the user.
subject = "Re: Fwd: Coupons"
# Calls the function called is_spam and passes the string typed in by the user as a parameter.
is_spam(subject)