import pytest
import sys
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

    ******MY NOTES: tackling this by starting with the assignment first, without reading- as I expect I might do 
    if I were working on a real project- I wouldn't have a book with directions to guide me

"""









"""

Problem 0
Write a function called "hello_world".
It should take one string argument, "name".
It should print "Hello {name}, and hello world!"
"""

"""
def hello_world(name):
print(f"Hello {name}, and hello world!")
"""

#above is what I was provided. It's pretty simple, but there's a lot I had to work through, and 
#doesn't provide an output

#first, I know  that I need to put something inside the curly brackets for {name}. That I know
#from last week's projects, where we used them for f-strings. That raises the question, however
#what the {} actually do. This came in handy: https://stackoverflow.com/questions/9197324/what-is-the-meaning-of-curly-braces

#it says that curly braces define dictionaries, and a dictionary is "a data structure that maps one value to another" , with example: 
#dict = {"a" : "Apple",
#    "b" : "Banana",}

#in this case, it wasn't necessary, but I think would become so if we needed to deal with multiple print issues??
name = "Paula"
def hello_world(name):
    print(f"Hello {name}, and hello world!")
hello_world(name)

"""
Problem 1
Write a function called "string_compare".
It should take two string arguments.
It should return True if both strings are equal.
It should return False if both strings are not equal.
"""

# def ... 
string1 = "1"
string2 = "2"

def string_compare():
    #had trouble figuring out which parameters to put in parenthesis above
    if string1 == string2:
        #kept having trouble above- and it's because you always forget the colon.
        #also didn't realize that (==) is the 'equality operator', which tests if two variables 
        #(which apparently can also be strings) are equal.
        print("True")
    else: print("False")
    #tried to have the two above with print("True"), which could probably work, but still nothing was working
    #Another colon problem! need 'else:'
    #originally here, and on problem 2, I used 'return'- but in the student discussion, it seems that everyone
    #is using print- so there's likely a good reason for it. figure out why that is. 
string_compare()












""" 
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument. 
"""

def string_append():
   string3 = (string1 + string2)
   print(string3)
string_append()

#looked this up, and adding two strings together turns out to be a concept called 'concatenation'
#at first you had the strings 1 and strings 2 as 'a' and 'b'. Does it matter if they're numbers or not?
#how come when this isn't working, it's not printing the results of the other functions? I guess I'm used to R
#giving me outputs until something fails???
#orginally: def string_append():
#               return string1 += string2
#           string_append()
"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 


"""
string4 = "This is the assignment for module 4"
def first_five_letters():
    print (string4[0:5])
first_five_letters()

#note- this didn't work at first. you need parenthesis around (string4[0:5]).
    
#this is an introduction to using what's called the subscript operator: []. You need to give it 
#three instructions separated by colons: [start of index position: end of index position: step size]
#learned some of this before. Note that the index starts at '0', not '1'. what you get is called 
#a slice of the string- a substring. (from https://thispointer.com/python-how-to-get-first-n-characters-in-a-string/)

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
total_packages = 5
total_weight = 40
def calculate_shipping_costs():
    if total_weight < 50:
        print(total_packages * 12.50)
    if total_weight >50:
        print(total_packages * 19.75)
calculate_shipping_costs()
#got this right on more or less the first try!! (minus the ever-present issue I have with colons)

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
name = "Doug"
def favorite_color():
    if "Jack" in name or "Michelle" in name:
    #if name == ("Jack" or "Michelle"): ---- why didn't that work????
    #if name == "Jack" or name == "Michelle" - does not work
        print ("Blue")
        #so obviously I tried to use 'or' first, which seems to just not do what I need to have done here. I'd like
        #to do this in one line of code, but can't get it to work- I could brute force it and write two lines, but I'd 
        #like to figure something better out. (original: if name == ("Jack" or "Michelle"):  )
        #solution comes here: https://python-forum.io/Thread-Multiple-expressions-with-or-keyword
        #also: https://python-forum.io/Thread-Simplifying-multiple-or-conditions-in-if-statement
        #actually got it from here:https://stackoverflow.com/questions/12774279/how-to-check-if-a-variable-is-equal-to-one-string-or-another-string
    elif name == "Robert":
        print("Green")
    elif name == "Jesse":
        print("Purple")
    elif name == "Sami":
        print ("Seafoam")
    else:
        print ("False")
favorite_color()


# def ...

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

subject = "Hello"
def is_spam():
    if "Greeting , " in subject or "Re: Fwd: Coupons" in subject or "Special Offer !" in subject:
        print ("True")
    else: 
        print ("False")
    
is_spam()

# def ...








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
Student: gardnerpaula
Compiled: 25-Feb-2020

Here are the results of some automated unit tests:

Hello Paula, and hello world!
False
12
This 
62.5
False
False
* Test #1 FAILED: string_compare() failed before test due to a TypeError: string_compare() takes 0 positional arguments but 1 was given

* Test #2 FAILED: string_append() failed before test due to a TypeError: string_append() takes 0 positional arguments but 2 were given

* Test #3 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #4 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #5 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #6 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #7 FAILED: is_spam() failed before test due to a TypeError: is_spam() takes 0 positional arguments but 1 was given

* Test #8 FAILED: first_five_letters() failed before test due to a TypeError: first_five_letters() takes 0 positional arguments but 1 was given

* Test #9 FAILED: favorte_color() failed before test due to a TypeError: favorite_color() takes 0 positional arguments but 1 was given

* Test #10 FAILED: favorte_color() failed before test due to a TypeError: favorite_color() takes 0 positional arguments but 1 was given

* Test #11 FAILED: favorte_color() failed before test due to a TypeError: favorite_color() takes 0 positional arguments but 1 was given

* Test #12 FAILED: favorte_color() failed before test due to a TypeError: favorite_color() takes 0 positional arguments but 1 was given

* Test #13 FAILED: calculate_shipping_costs() failed before test due to a TypeError: calculate_shipping_costs() takes 0 positional arguments but 2 were given

* Test #14 FAILED: calculate_shipping_costs() failed before test due to a TypeError: calculate_shipping_costs() takes 0 positional arguments but 2 were given



"""
