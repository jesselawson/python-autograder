"""
Module 04 Assignment: "Fun with Functions"

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

def string_compare(string1, string2):
    if(string1 == string2):
        print("True")
    else:
        print("False")


"""
Problem 2
Write a function called "string_append".
It should take two string arguments.
It should return a new string equal to the contents of the first argument
and the contents of the second argument.
"""

def string_append(string1, string2):
    print(string1+string2)

"""
Problem 3
Write a function called "first_five_letters".
It should take one string argument.
It should return the first five letters of the string argument.
"""

def first_five_letters(string1):
    letter = string1[0] + string1[1] + string1[2] + string1[3] +string1[4]
    print(letter)

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
    int_total_packages = int(total_packages)
    int_total_weight = int(total_weight)
    if(int_total_weight <= 50):
        print(int_total_packages * 12.50)
    else:
        print(int_total_packages * 19.75)

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
    if(name == 'Jack'):
        print("Blue")
    elif(name == 'Michelle'):
        print("Blue")
    elif(name == 'Robert'):
        print("Green")
    elif(name == 'Jesse'):
        print("Purple")
    elif(name == 'Sami'):
        print("Seafoam")
    else:
        print("Black")


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
    if(subject == "Greeting , "):
        print("True")
    elif(subject == "Re: Fwd: Coupons"):
        print("True")
    elif(subject == "Special Offer !"):
        print("True")
    else:
        print("false")
