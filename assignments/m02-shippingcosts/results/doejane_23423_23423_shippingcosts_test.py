import pytest
import sys
"""
M02 Assignment: "Shipping Costs"

DIRECTIONS 
1. Read through this file, completing the tasks as required. Pay attention 
   to the comments because that is where you will find out what to do. 

2. When you are finished, upload this file to the Canvas assignment. 

"""

### Let's begin!

"""
In this assignment, you'll be writing a very basic shipping costs calculator 
for Big Tuna's Shipping Company. This calculator will be static and 
simply calculate the shipping costs based on the code. In other words, 
there is no interactive component. 
"""

# Below you will see some print statements that output the name
# of the program. But something is wrong! Correct the Python code 
# below so that the print statements will work.

print("* * * * * * * * * *") # Hint: this line is correct
print("Shipping Costs Calculator")
print("Written by <your name>") # Put your name in the print statement!
               
# At Big Tuna's Shipping Company, there are 44 packages ready. 
# Create a variable named "num_packages_ready" to hold that value.
num_packages_ready = 44 # I did this one for you.

# Ten additional packages came in last night from a midnight flight. 
# Create a variable named "additional_packages" to hold that value:
additional_packages = 10

# We need the total number of packages to calculate shipping costs. 
# The total number of packages is equal to the sum of the number
# of packages ready and the number of additional packages. 
# Create a new variable called "total_packages", and make its value 
# equal to the sum of "num_packages_ready" and "additional_packages":
total_packages = num_packages_ready + additional_packages

# Let's now calculate the total shipping costs. Our shipping and 
# receiving department has indicated that each package costs three
# dollars to ship. 
# Create a variable called "package_cost" to hold the shipping cost
# of each individual package (hint: <variable> = 3)
package_cost = 3

# Now let's figure out the total cost of all these packages. 

# Create a variable called "total_costs" and set its value to be equal to 
# the the sum of all packages (the number of packages ready plus the 
# additional packages) multiplied by the individual package cost:
total_costs = package_cost * total_packages


# If you did everything correctly, you should be able to execute this 
# script and see the message "(You did it!)" If, instead, you see
# the message "(Uh oh!)", that means you need to go back and carefully 
# read through the comments, ensuring you followed the directions. 










################# Professor Lawson's Section ###########################
# You can ignore everything below this, or keep reading if you're curious.
# This is all stuff you'll learn about very soon. I like to 
# keep code like this in your assignments because it shows you some
# practical application of the concepts you will learn in this course.
# 
# Feel free to tinker around with this and explore--but only AFTER you have 
# completed and turned in this assignment!
########################################################################

message = f"It will cost ${int(total_costs)} to ship {total_packages} packages."

if message == "It will cost $162 to ship 54 packages.":
  print("(You did it!)")
else: 
  print("(Uh oh!)")






### BEGIN AUTOGRADER INJECTION ###

# Test helpers for shipping costs assignment

def get_num_packages_ready():
	num_packages_ready
		
def get_additional_packages():
	additional_packages
	
def get_total_packages():
	total_packages

def get_total_costs():
	total_costs



### END AUTOGRADER INJECTION ###








"""
(30-Jan-2020 Professor Lawson) Below you will find all the test 
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

def test_num_packages_ready():
	assert(num_packages_ready == 44)
		
def test_additional_packages():
	assert(additional_packages == 10)
	
def test_total_packages():
	assert(total_packages == num_packages_ready + additional_packages)

def test_total_costs():
	assert(total_costs == ((44+10)*3))



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
    output += str(r) 
    output += "\n"
print(output)
        




"""
TEST RUNNER RESULTS
======================================
Assignment: m02-shippingcosts/
Student: doejane
Compiled: 30-Jan-2020

* * * * * * * * * *
Shipping Costs Calculator
Written by <your name>
(You did it!)
None
None
None
None


"""
