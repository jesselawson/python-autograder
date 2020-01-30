import pytest
import sys
def test_num_packages_ready():
	assert(get_num_packages_ready() == 44)
		
def test_additional_packages():
	assert(get_additional_packages() == 10)
	
def test_total_packages():
	assert(get_total_packages() == get_num_packages() + get_additional_packages())

def test_total_costs():
	assert(get_total_costs() == ((44+10)*3))








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

Traceback (most recent call last):
  File "m02-shippingcosts//results/doejane_23423_23423_shippingcosts_test_test.py", line 88, in <module>
    r = item()
  File "m02-shippingcosts//results/doejane_23423_23423_shippingcosts_test_test.py", line 72, in test_total_packages
    assert(total_packages == num_packages_ready + additional_packages)
NameError: name 'total_packages' is not defined

"""
