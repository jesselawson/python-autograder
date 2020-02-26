import pytest
import sys
b1 =9
b2 =9

def string_compare(n1,n2):
  if n1 == n2 :
#comparison
    return True
  else:
    return False


print(string_compare(b1,b2))





def string_append(Country,Great='Amazing'):
   return'{}, {}' .format(Country,Great)

print (string_append('America', Great = 'Amazing'))



def first_five_letters(string1):
  return string1[0:5]

print(first_five_letters("Amazing"))



def calculate_shipping_costs(total_packages,total_weight):
  if total_weight < 50:
   return total_packages * 12.50
  else:
     return total_packages * 19.75


print(calculate_shipping_costs(5,40))




def favorite_color(name):
    if name == "Jack":
        return "Blue"
    elif name == "Robert":
        return "Green"
    elif name == "Jesse":
        return "Purple"
    elif name == "Seafoam":
        return "Sami"
    else:
        return "Black"

print(f"Jack favorite color is {favorite_color('Jack')}")


print(f"Robert favorite color is {favorite_color('Robert')}")


print(f"Jesse favorite color is {favorite_color('Jesse')}")


print(f"Seafoam favorite color is {favorite_color('Seafoam')}")


print(f"Tony favorite color is {favorite_color('Tony')}")



def is_spam(subject):
  if "Greetings" in subject:
     return True
  elif "Re: Fwd: Coupons" in subject:
      return True
  elif "Special Offer !" in subject:
    return True
  return False

print(is_spam("Greetings Tony"))










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
Student: cuevastony
Compiled: 25-Feb-2020

Here are the results of some automated unit tests:

True
America, Amazing
Amazi
62.5
Jack favorite color is Blue
Robert favorite color is Green
Jesse favorite color is Purple
Seafoam favorite color is Sami
Tony favorite color is Black
True
* Test #1 FAILED: string_compare() failed before test due to a TypeError: string_compare() missing 1 required positional argument: 'n2'

* Test #2 FAILED: string_append() failed to append second argument to first argument!

* Test #3 passed: is_spam() should classify 'Special Offer !' as spam

* Test #4 passed: is_spam() should classify 'Re: Fwd: Coupons' as spam

* Test #5 FAILED: is_spam() failed to classify 'Greeting ,' as spam!

* Test #6 passed: is_spam() should not classify 'Special Offer!' as spam

* Test #7 FAILED: is_spam() failed to not classify 'Greetings,' as spam!

* Test #8 passed: first_five_letters() should return the first five letters of the string

* Test #9 FAILED: favorite_color() failed to return 'Seafoam' when input is 'Sami'!

* Test #10 passed: favorite_color() should return 'Green' when input is 'Robert'

* Test #11 passed: favorite_color() should return 'Purple' when input is 'Jesse'

* Test #12 passed: favorite_color() should return 'Blue' when input is 'Jack'

* Test #13 passed: calculate_shipping_costs() should return 5 * 19.75

* Test #14 passed: calculate_shipping_costs() should return 5 * 12.50



"""
