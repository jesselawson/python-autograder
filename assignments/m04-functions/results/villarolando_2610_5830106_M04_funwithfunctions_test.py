import pytest
import sys
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("* * * * * * * * * * * * * * * * * * * * *") # Hint: this line is correct
print()
print ("Module 04 Assignment: Fun with Functions")
print("Written by <Rolando Villa>") # Put your name in the print statement!
print()
print("* * * * * * * * * * * * * * * * * * * * *")
print()
"""
Created on Fri Feb 21 18:37:31 2020

@author: rolando villa
"""

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
print ("Problem 0: Hello World")
def hello_world(name):
 #This function outputs a greeting to a nemed person
    print(f"Hello {name}, and hello world!") 


hello_world ("Rolando")  

print() #this provides an extra line space between the problem solutions.
"""
Problem 1
Write a function called "string_compare".
It should take two string arguments.
It should return True if both strings are equal.
It should return False if both strings are not equal.
"""

string1 = "computer"
string2 = "computers"

print("Problem 1: String Compare")
def string_compare():
 #This function compares two string variables to see if they are equal.
   test = True
   if string1 == string2:
      print (f" Comparison is {test}")
   else:
      print (" Comparison is NOT True")

string_compare()


print() #this provides an extra line space between the problem solutions.
""" 
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument.
"""

day1 = "Today is Tuesday"
day2 = "Tomorrow is Wednesday"

print("Problem 2: String Append") 


def string_append():
#This function takes two strngs and modifies them to match the first with the second string
    print (day1)
    print (day2)  
    print()   

    print (day1)
    print (day2.replace("Tomorrow is Wednesday" , "Today is Tuesday"))
    print (day2)


string_append()



print() #this provides an extra line space between the problem solutions.
"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 
"""

print("Problem 3:First Five Letters") 
def first_five_letters():
#This function looks at a given string and outputs specific parts of the given string
    text1 = "ENCYCLOPAEDIA"
    
    print ( text1 [ :5])
    
    
first_five_letters()    

print() #this provides an extra line space between the problem solutions.
"""
Problem 4
Write a function called "calculate_shipping_costs".
It should take two integer arguments, "total_packages" and "total_weight".
It should return the product of "total_packages" and 12.50
when "total_weight" is less than 50. 
It should return the product of "total_packages" and 19.75
when "total_weight" is 50 or more. 
"""

print("Problem 4: Calculating Shipping Costs") 
def calculate_shipping_costs ():

    total_packages = 10
    total_weight = 100
    
    if total_weight <50:
         print (f" The total cost is ${total_packages * 12.50}")
    else:
         print (f" The total cost is ${total_packages * 19.75}")
    
    
calculate_shipping_costs ()
    
print() #this provides an extra line space between the problem solutions.
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

print("Problem 5: Favorite Colors") 
def favorite_color(name):
    if name == "Jack":
        return "Blue"
    if name == "Michelle":
        return "Blue"
    elif name == "Robert":
        return "Green"
    elif name == "Jesse":
        return "Purple"
    elif name == "Sami":
        return "Seafoam"
    else:
        return "Black" 
    
print (f"Jack favorite color is {favorite_color('Jack')}.") 
print (f"Michelle's favorite color is {favorite_color('Michelle')}.")
print (f"Robert's favorite color is {favorite_color('Robert')}.")
print (f"Jesse's favorite color is {favorite_color('Jesse')}.")
print (f"Sami's favorite color is {favorite_color('Sami')}.")
print (f"John's favorite color is {favorite_color('John')}")


print() #this provides an extra line space between the problem solutions.
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

print("Problem 6: Spam ") 
def is_spam():
# This function scans the subject line and/or header of an email and determines if it is spam by filtering out the keywords.
    subject = ["Greeting , " , "Re:", "Fwd:", "Coupons", "Special Offer !"]
   
    for keyword in subject:
        print (" mail contains spam")   
    
      
is_spam()
    









"""
(25-Feb-2020 Professor Lawson) Below you will find all the test 
functions I have used to evaluate your submission. You are free to 
download this file and tinker around with it. In fact, 
I encourage it!

"""


# Obfuscated name to prevent possible conflict with student file
test_qwertyuioplkjhgfdsa_number = 0

def jel_NameError(target, e):
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    return m + f"FAILED: {target} failed before test due to a NameError: {e}"

def jel_TypeError(target, e):
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    return m + f"FAILED: {target} failed before test due to a TypeError: {e}"

def jel_assert(target, expr, should_msg):
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    try:
        assert expr
    except AssertionError as e:
        return m + f"FAILED: {target} failed to {should_msg}!"
    except NameError as e:
        return m + f"FAILED: {target} failed to {should_msg}! NameError: {e}"
    except TypeError as e:
        return m + f"FAILED: {target} failed to {should_msg}! TypeError: {e}"
    else:
        return m + f"passed: {target} should {should_msg}"
    
# BEGIN TEST SUITE INJECTION ===================================================


# Test suite for M04 Functions

# Problem 1
def test_string_compare():
    target = "string_compare()"
    try:
        return jel_assert(
                target, 
                string_compare( "this is a test") == True, 
                "return true if strings are the same"
            )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
# Problem 2
def test_string_append():
    target = "string_append()"
    try:
        return jel_assert(target, string_append("Coastline ", "Community College") == "Coastline Community College", "append second argument to first argument")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
# Problem 3
def test_first_five_letters():
    target = "first_five_letters()"
    try:
        return jel_assert(target, first_five_letters( "Abcdefghijklmnopqrstuvqxyz") == "Abcde", "return the first five letters of the string")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
# Problem 4
def test_calculate_shipping_costs_when_weight_is_less_than_50():
    target = "calculate_shipping_costs()"
    try:
        return jel_assert(target, calculate_shipping_costs( 5, 49 ) == 62.50, "return 5 * 12.50")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_calculate_shipping_costs_when_weight_is_more_than_50():
    target = "calculate_shipping_costs()"
    try:
        return jel_assert("calculate_shipping_costs()", calculate_shipping_costs( 5, 51 ) == 98.75, "return 5 * 19.75")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
# Problem 5 
def test_favorite_color_when_jack_or_michelle():
    target = "favorte_color()"
    try:
        return jel_assert("favorite_color()", favorite_color( "Jack" ) == "Blue", "return 'Blue' when input is 'Jack'")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_favorite_color_when_robbie():
    target = "favorte_color()"
    try:
        return jel_assert("favorite_color()", favorite_color( "Robert" ) == "Green", "return 'Green' when input is 'Robert'")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_favorite_color_when_jesse():
    target = "favorte_color()"
    try:
        return jel_assert( "favorite_color()", favorite_color( "Jesse" ) == "Purple", "return 'Purple' when input is 'Jesse'")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_favorite_color_when_sami():
    target = "favorte_color()"
    try:
        return jel_assert( "favorite_color()", favorite_color( "Sami" ) == "Seafoam", "return 'Seafoam' when input is 'Sami'")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)


# Problem 6
def test_is_spam_should_return_true_if_subject_contains_greeting():
    target = "is_spam()"
    try:
        return jel_assert( "is_spam()", is_spam( "Ah good morning and Greeting , kind sir" ) == True, "classify 'Greeting ,' as spam")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_is_spam_should_return_true_if_subject_contains_refwdcoupons():
    target = "is_spam()"
    try:
        return jel_assert(  "is_spam()", is_spam( "Special Offer! Re: Fwd: Coupons for you!" ) == True, "classify 'Re: Fwd: Coupons' as spam")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_is_spam_should_return_true_if_subject_contains_specialoffer():
    target = "is_spam()"
    try:
        return jel_assert(  "is_spam()", is_spam( "Look For This Special Offer !" ) == True, "classify 'Special Offer !' as spam")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_is_spam_should_return_false_if_not_spam():
    target = "is_spam()"
    try:
        return jel_assert(  "is_spam()", is_spam("Season's Greetings, Friend.") == False, "not classify 'Greetings,' as spam")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
    
def test_is_spam_should_return_false_if_not_spam2():
    target = "is_spam()"
    try:
        return jel_assert(  "is_spam()", is_spam("Re: Fwd: Help on the spreadsheet") == False, "not classify 'Re: Fwd: Help' as spam")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_is_spam_should_return_false_if_not_spam2():
    target = "is_spam()"
    try:
        return jel_assert(  "is_spam()", is_spam("Special Offer! We can do this!") == False, "not classify 'Special Offer!' as spam")
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)


# END TEST SUITE INJECTION =====================================================

# Custom test runner
test_results = []
dir_result = dir(sys.modules[__name__])
dir_result.reverse()
for some_function in dir_result:
    item = getattr(sys.modules[__name__], some_function)
    if some_function.startswith("test_") and callable(item):
        r = item()
        test_results.append(r) # All tests call jel_assert, which returns a string message
output = ""
test_results
for r in test_results:
    output += "* "
    output += str(r) 
    output += "\n\n"
print(output)
        




"""
TEST RUNNER RESULTS
======================================
Assignment: m04-functions
Student: villarolando
Compiled: 25-Feb-2020

Here are the results of some automated unit tests:

* * * * * * * * * * * * * * * * * * * * *

Module 04 Assignment: Fun with Functions
Written by <Rolando Villa>

* * * * * * * * * * * * * * * * * * * * *

Problem 0: Hello World
Hello Rolando, and hello world!

Problem 1: String Compare
 Comparison is NOT True

Problem 2: String Append
Today is Tuesday
Tomorrow is Wednesday

Today is Tuesday
Today is Tuesday
Tomorrow is Wednesday

Problem 3:First Five Letters
ENCYC

Problem 4: Calculating Shipping Costs
 The total cost is $197.5

Problem 5: Favorite Colors
Jack favorite color is Blue.
Michelle's favorite color is Blue.
Robert's favorite color is Green.
Jesse's favorite color is Purple.
Sami's favorite color is Seafoam.
John's favorite color is Black

Problem 6: Spam 
 mail contains spam
 mail contains spam
 mail contains spam
 mail contains spam
 mail contains spam
* Test #1 FAILED: string_compare() failed before test due to a TypeError: string_compare() takes 0 positional arguments but 1 was given

* Test #2 FAILED: string_append() failed before test due to a TypeError: string_append() takes 0 positional arguments but 2 were given

* Test #3 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #4 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #5 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #6 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #7 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #8 FAILED: first_five_letters() failed before test due to a TypeError: first_five_letters() takes 0 positional arguments but 1 was given

* Test #9 passed: favorite_color() should return 'Seafoam' when input is 'Sami'

* Test #10 passed: favorite_color() should return 'Green' when input is 'Robert'

* Test #11 passed: favorite_color() should return 'Purple' when input is 'Jesse'

* Test #12 passed: favorite_color() should return 'Blue' when input is 'Jack'

* Test #13 FAILED: calculate_shipping_costs() failed before test due to a TypeError: calculate_shipping_costs() takes 0 positional arguments but 2 were given

* Test #14 FAILED: calculate_shipping_costs() failed before test due to a TypeError: calculate_shipping_costs() takes 0 positional arguments but 2 were given



"""
