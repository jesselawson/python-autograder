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
  #string1 = input('Please enter a string: ')
  #string2 = input('Please enter another string: ')
  if string1 == string2:
      print('True')
  else :
      print('False')
string_compare()



""" 
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument. 
"""

# def def.. 
def string_append():
  #string1 = input('Please enter a string: ')
  #string2 = input('Please enter another string: ')
  newString = string1 +" "+ string2
  print(newString)
string_append()

"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument. 
It should return the first five letters of the string argument. 
"""

def first_five_letters():
  #string = input('Please enter a string: ')
  newString = string[ 0 : 5 ]
  print(newString)
first_five_letters()
# def ...

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
  #total_packages = int(input('Please enter the total number of packages: '))
  #total_weight = int(input('Please enter the total weight of the packages: '))
  total1 = total_weight * 12.5
  total2 = total_weight * 19.75
  if total_weight <50:
    print('The total shipping cost is:')
    print(total1)
  else:
      print('The total shipping cost is')
      print(total2)
calculate_shipping_costs()
# d

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
  #name = input('What is your name? ')
  if (name == "Jack") or (name =="Michelle"):
      print('Blue')
  elif name =="Robert":
      print('Green')
  elif name == "Jesse":
      print('Purple')
  elif name == "Sami":
      print('Seafoam')
  else:
       print('Black')
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
def is_spam():
  #subject = input('Please enter one string arguement: ')
  if ("Greeting , " in subject) or ("Re: Fwd: Coupons" in subject) or ("Special Offer !" in subject):
      print(" True")
  else:
    print("False")
is_spam()
# def ...



    
    



