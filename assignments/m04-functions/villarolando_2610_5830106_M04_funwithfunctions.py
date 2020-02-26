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
    


