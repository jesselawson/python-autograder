import pytest
import sys
"""
M02 Assignment: "Shipping Costs"

Objectives: 
1. Demonstrate how to correct basic syntax errors in Python.
2. Demonstrate how to create a variable in Python
3. Demonstrate how to do basic math with variables in Python
 
To complete this assignment, do the following:

1. Save a copy of this file onto your computer. 

2. Execute this python file, observing the errors.

3. Use the errors to correct the code. Continue fixing/writing code until
   all errors are gone.
   
4. Submit the error-free version of this file to the appropriate 
   assignment in Canvas.

"""

# Welcome to the "Shipping Costs" assignment. You will be writing code to 
# help compute the shipping costs of various packages for a shipping 
# company. 

# Go through this file line-by-line, readinge every comment. Follow any 
# instructions to fix code OR write new code. If you see syntax errors,
# correct them. 

# When you are finished, execute this file. If there are any errors, go back 
# and correct them. Continue the cycle of correcting/writing and executing until
# you are satisifed that there are no errors. 

# When you have reached the end of the file, save it, and submit it to 
# the appropriate assignment in Canvas. 

print("* * * * * * * * * *") # Hint: this line is correct
print("Shipping Costs Calculator") # Hint: this line is NOT correct
print("Based on my calculations...")


# There are 44 packages ready for delivery:
num_packages_ready = 
# Here you want to make num_packages_ready equal to 44
# so the correct answer is:
# num_packages_ready = 44


# Today, ten additional packages were added to the inventory:
additional_packages = 10

# We need the total number of packages to calculate shipping costs. 
# The total number of packages is equal to the sum of the number
# of packages ready and the number of additional packages:
total_packages = 44+10;

# Let's now calculate the total shipping costs. Our shipping and 
# receiving department has indicated that each package costs three
# dollars to ship. Here, we must multiply the total packages by the 
# per package shipping cost: 
total_costs = 3 * total_packages

# CHECK YOUR PROGRESS ###############################################################
# DO NOT modify anything in here. This is only here to help you check your 
# progress. 
message = f"It will cost ${int(total_costs)} to ship {total_packages} packages."
print(message)

if message == "It will cost $162 to ship 54 packages.":
  print("You completed Step 2 successfully!")
else: 
  print("You need to keep working on Step 2. Hang in there!")
  
# END STEP 2 CHECK ##################################################################











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
Student: millerted
Compiled: 30-Jan-2020

  File "m02-shippingcosts//results/millerted_234234_23434_shippingcosts_test.py", line 46
    num_packages_ready = 
                        ^
SyntaxError: invalid syntax

"""
