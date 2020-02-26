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

