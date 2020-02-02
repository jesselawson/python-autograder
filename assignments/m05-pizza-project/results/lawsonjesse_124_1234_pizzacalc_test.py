import pytest
import sys
"""

M05 "Pizza Parlor Project"

INTRODUCTION
================================================================================

Welcome to the first project of this course! 

The only difference between a project and a regular assignment is that the 
project wont have any starter code. In other words, you will be writing these 
from scratch! Since you will be starting from scratch, this is the only
assignment you will be doing for this module. You don't have to focus on 
anything else!

So read the directions CAREFULLY, and follow ALL INSTRUCTIONS precisely. 

If you have any questions, please first reach out to the class via the 
Course Related Discussions forum in Canvas. I monitor those just as closely as 
I do my email and Canvas inbox. 

Drink water. Be comfortable with being frustrated. Trust that you can do this.

I believe in you.

- Professor Lawson

OVERVIEW
================================================================================
Michelle, the owner of Fountain Valley Pizza, has asked us to write her a 
special calculator that can tell her how much it would cost for her to make 
different "specialty" pizzas--ones with lots of fancy toppings--and, more 
importantly, how much she should charge for these pizzas if she wants to 
maintain a 30% profit margin. 

She has given us the following information about the material costs by size, 
sauce type, and kind of topping:

| ID  | Size   | Cost |           Pizza Sizes
+-----|--------+------+
|  L  | Large  | 5.00 |
|  M  | Medium | 4.00 |
|  S  | Small  | 3.00 |

| ID  | Sauce  | Cost |           Sauce Types
+-----+-------+------+
|  R  | Red    | 1.35 |
|  W  | White  | 2.15 |

| ID  | Topping    | Cost |       Toppings
+-----+------------+------+
|  C  | Cheese     | 0.45 |
|  I  | Pepperoni  | 0.85 |
|  P  | Peppers    | 0.55 |
|  O  | Mushrooms  | 0.25 |
|  H  | Ham        | 1.15 |
|  K  | Pickles    | 0.75 |
|  Y  | Yogurt     | 2.10 |
|  N  | Spinach    | 0.95 |

| Specialty Pizza      | Toppings                              | Specialty
+----------------------+---------------------------------------+ Pizzas
| The Super California | Cheese, Yogurt, Spinach               |
| The Salty Manhattan  | Ham, Mushrooms, Cheese, Pickles       |
| The Unkissable       | Pickles, Yogurt                       |
| Meaty McMeatface     | Cheese, Pepperoni, Peppers, Mushrooms |
| The Vegetarian       | Mushrooms, Spinach                    |


ASSUMPTIONS
================================================================================
* Assume that the cost of each topping is the same for all pizza sizes.
* Assume you can only have one of each topping.
* Assume you can only have one of each sauce.
* Assume you can only type UPPER CASE LETTERS in the input.



INSTRUCTIONS
================================================================================

1. Create a function named `get_size_cost`.
   It should take one argument: the size ID.
   It should return the cost of a large pizza when the argument is 'L'.
   It should return the cost of a medium pizza when the argument is 'M'.
   It should return the cost of a small pizza when the argument is 'S'.

2. Create a function named `get_sauce_cost`.
   It should take one argument: the sauce type ID.
   It should return the cost of red sauce when the argument is 'R'.
   It should return the cost of white sauce when the argument is 'W'.

3. Create a function named `get_topping_cost`. 
   It should take take one argument: the topping ID. 
   It should return the cost of Cheese when the argument is 'C'.
   It should return the cost of Pepperoni when the argument is 'I'.
   It should return the cost of Peppers when the argument is 'P'.
   It should return the cost of Mushrooms when the argument is 'O'.
   It should return the cost of Ham when the argument is 'H'.
   It should return the cost of Pickles when the argument is 'K'.
   It should return the cost of Yogurt when the argument is 'Y'.
   It should return the cost of Spinach when the argument is 'N'.

4. Create a function named `get_specialty_cost`.
   It should take one argument: the name of the specialty pizza.
   It should return the cost of Cheese, Yogurt, and Spinach
      when the argument is 'The Super California'.
   It should return the cost of Ham, Mushrooms, Cheese, and Pickles
      when the argument is 'The Salty Manhattan'.
   It should return the cost of Pickles and Yogurt
      when the argument is 'The Unkissable'.
   It should return the cost of Cheese, Pepperoni, Peppers, and Mushrooms
      when the argument is 'Meaty McMeatface'.
   It should return the cost of Mushrooms and Spinach
      when the argument is 'The Vegetarian'.
   Note: You should be using the functions you created in 1, 2, and 3.

5. Update function `process_choice_specialty_pizza`.
     It should use `get_specialty_cost` to return the value of a
        specialty pizza based on the user's choice.
     (Hint: I have provided the first one for you; use if-elif-else to 
      process choices. Use the else keyword to return the default value, 
      which you can find in the input() function's argument)

6. Update the comment section at the bottom of this code file that starts with 
   "HOW TO USE THIS SCRIPT". 
   Write detailed instructions for Michelle, the person who will be using this 
   script, detailing how to run it and when to make what choices. 
   
   Assume she only knows how to execute the file; she doesn't know Python.
   
   Include enough detailed instructions for a non-programmer to be confident 
   in how to use this script.

7. There should be no errors when you run this script. 

8. Upload this completed file to the assignment in Canvas.

TIPS FOR SUCCESS
========================================================
* All monetary numbers should be expressed with two decimals at all times. For 
  example, `return 5.00` or `ham_cost = 1.15`.

* You are coming up with the variable and argument names. I have provided 
  the names of the required functions only. 

* Store the values of each table in their own variables. For example, 

* How to round an integer to the nearest two decimal places:
https://stackoverflow.com/a/20457115

"""

# Create your functions starting here
def get_size_cost(size):
    return 5.00 # Delete this before you begin writing this function

def get_sauce_cost(sauce):
    return 0.00 # Delete this before you begin writing this function

def get_topping_cost(topping):
    return 0.00 # Delete this before you begin writing this function

# def ...
#   etc.

# print_toppings
# DESCRIPTION
#   Prints the toppings in a menu-like format, along with their IDs.
# USAGE
#   1. print_toppings()                 Prints all the toppings
#   2. print_topping('A")               Prints all the toppings except for 
#                                       the one where ID == A
def print_toppings(except_this_one=''):
    if except_this_one =='A':
        print("[A] Cheese")
    if except_this_one == 'B':
        print("[B] Pickles")
    if except_this_one == 'C':
        print("[C] Pepperoni")
    if except_this_one == 'D':
        print("[D] Mushrooms")
    if except_this_one == 'E':
        print("[E] Ham")
    if except_this_one == 'F':
        print("[F] Yogurt")
    if except_this_one == 'G':
        print("[G] Spinach")
    if except_this_one == 'H':
        print("[H] Peppers")

# process_choice_custom_2topping_pizza
# DESCRIPTION
#   Queries the user to get the first and second topping for a custom 
#   two-topping pizza, then returns the sum cost of both toppings.
# USAGE     
#   total = process_choice_custom_2topping_pizza()
#   ... 
#   print(f"Total cost: ${total}")
def process_choice_custom_2topping_pizza():
    print("CUSTOM 2-TOPPING PIZZA")
    print("===================================================================")
    
    print("Select the first topping:")
    print_toppings()
    print("-------------------------------------------------------------------")  
    topping1 = input("Topping 1 (default A): ")
  
    if topping1 == "":
        topping1 = "A"

    print("Select the second topping:")
    print_toppings()
    print("-------------------------------------------------------------------")  
    topping2 = input("Topping 2 (default B): ")

    if topping2 == "":
        topping2 = "B"

    # The total cost is the sum of the cost of topping1 and topping2
    total_cost = get_topping_cost(topping1) + get_topping_cost(topping2)

    return round(total_cost, 2)

# process_choice_specialty_pizza
# DESCRIPTION
#   Queries the user to get the name of the specialty pizza they want, 
#   then returns the cost of that pizza using `get_specialty_cost()`
# USAGE     
#   total = process_choice_specialty_pizza()
#   ... 
#   print(f"Total cost: ${total}")
def process_choice_specialty_pizza():
    print("SPECIALTY PIZZA")
    print("===================================================================")
    print("Select one of the specialty pizzas:")
    print("[A] The Super California      [B] The Salty Manhattan")
    print("[C] The Unkissable            [D] Meaty McMeatface")
    print("[E] The Vegetarian")
    print("-------------------------------------------------------------------")  
  
    choice = input("Selection (default A): ")
  
    if choice == 'A':
        return get_specialty_cost("The Super California")
    # elif ...

# All the main program logic will exist inside the main() function, which is 
# called at the very end of this file with "sys.exit(main())".
# Need a refresher? https://realpython.com/python-main-function/
def main():
    print("Pizza Parlor Tool")
    print("===================================================================")

    size = input("Enter Size (S, M, or L; Default: M)> ")
    sauce = input("Enter Sauce (R or W; Default: R)> ")
    
    print("Enter the letter of your choice: ")

    print("[A] Specialty Pizza")
    print("[B] Custom Two-Topping Pizza")
    print("-------------------------------------------------------------------")
    choice = input("Selection (default A): ")

    # Calculate total cost of pizza given size, sauce, and topping selections 
    # based on whether they selected A or B at the menu
    
    # Start with zero
    total_cost = 0
    
    # Process user selection. 
    if choice == 'A':
        # If the user selected "[A] Specialty Pizza", increase total_cost
        # by the return value of process_choice_specialty_pizza()
        total_cost += process_choice_specialty_pizza()
    elif choice == 'B':
        # If the user selected "[B] Custom Two-Topping Pizza", increase 
        # total_cost by the return value of process_choice_custom_2topping_pizza()
        total_cost += process_choice_custom_2topping_pizza()

    # Add the size and sauce costs
    total_cost += get_size_cost(size)
    total_cost += get_sauce_cost(sauce)

    # Finally, add 30% markup
    final_cost = total_cost * 0.30

    # Output the totals. I'm using round() to ensure that no number is displayed
    # with more than two decimal places. Do you think it's necessary for me 
    # to repeat these calls to round() here?
    print(f"Cost to make: ${round(total_cost, 2)}")
    print(f"Sale price: ${round(final_cost, 2)}")
    print(f"Total profit: ${round(final_cost - total_cost, 2)}")

# If you don't remember why we do this, read here: 
# https://realpython.com/python-main-function/
if __name__ == '__main__':
    main()


"""
HOW TO USE THIS SCRIPT

...

"""






"""
(01-Feb-2020 Professor Lawson) Below you will find all the test 
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

"""
Assignment test suite for M05 Pizza Project Assignment

For the Better Pizza Tool, we should be using while 
loops to capture input correctly. For example, if someone 
enters in an invalid option, it should loop back around 
and remind the person that it was not a valid option. 

"""

# Problem 1
problem1_target = "get_size_cost()"

def test_get_size_cost_L():
    try:
        return jel_assert(
                problem1_target, 
                get_size_cost('L') == 5.00, 
                "return 5.00 when given 'L'"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_size_cost_M():
    try:
        return jel_assert(
                problem1_target, 
                get_size_cost('M') == 4.00, 
                "return 4.00 when given 'M'"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_size_cost_S():
    try:
        return jel_assert(
                problem1_target, 
                get_size_cost('S') == 3.00, 
                "return 3.00 when given 'S'"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)      

# Problem 2
problem2_target = "get_sauce_cost()"

def test_get_sauce_cost_R():
    try:
        return jel_assert(
                problem2_target, 
                get_sauce_cost('R') == 1.35, 
                "return 1.35 when given 'R'"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

def test_get_sauce_cost_W():
    try:
        return jel_assert(
                problem2_target, 
                get_sauce_cost('W') == 2.15, 
                "return 2.15 when given 'W'"
        )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

# Problem 3
problem3_target = "get_topping_cost()"

def build_test_for_topping(id, price):
    try:
        return jel_assert(
                problem3_target, 
                get_topping_cost(id) == price,
                f"return {price} when given '{id}'"
        )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_topping_cost_C():
    return build_test_for_topping('C', 0.45)

def test_get_topping_cost_I():
    return build_test_for_topping('I', 0.85)

def test_get_topping_cost_P():
    return build_test_for_topping('P', 0.55)

def test_get_topping_cost_O():
    return build_test_for_topping('O', 0.25)

def test_get_topping_cost_H():
    return build_test_for_topping('H', 1.15)

def test_get_topping_cost_K():
    return build_test_for_topping('K', 0.75)

def test_get_topping_cost_Y():
    return build_test_for_topping('Y', 2.10)

def test_get_topping_cost_N():
    return build_test_for_topping('N', 0.95)

# Problem 4
problem4_target = "get_specialty_cost()"

def test_get_specialty_cost_california():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("The Super California") == (
                    get_topping_cost("C") + 
                    get_topping_cost("Y") + 
                    get_topping_cost("N")
                ), 
                "return 3.50 when given 'The Super California'"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_manhattan():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("The Salty Manhattan") == (
                    get_topping_cost("H") + 
                    get_topping_cost("O") + 
                    get_topping_cost("C") +
                    get_topping_cost("K")
                ), 
                "return 2.60 when given 'The Salty Manhattan'"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_unkissable():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("The Unkissable") == (
                    get_topping_cost("K") + 
                    get_topping_cost("Y")
                ), 
                "return 2.85 when given 'The Unkissable'"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_mcmeatface():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("Meaty McMeatface") == (
                    get_topping_cost("C") + 
                    get_topping_cost("I") +
                    get_topping_cost("P") +
                    get_topping_cost("O")
                ), 
                "return 2.10 when given 'Meaty McMeatface'"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_vegetarian():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("The Vegetarian") == (
                    get_topping_cost("O") + 
                    get_topping_cost("N")
                ), 
                "return 1.20 when given 'The Vegetarian'"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

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
Assignment: m05-pizza-project
Student: lawsonjesse
Compiled: 01-Feb-2020

Pizza Parlor Tool
===================================================================
Enter Size (S, M, or L; Default: M)> Enter Sauce (R or W; Default: R)> Enter the letter of your choice: 
[A] Specialty Pizza
[B] Custom Two-Topping Pizza
-------------------------------------------------------------------
Selection (default A): Cost to make: $5.0
Sale price: $1.5
Total profit: $-3.5
Test #1 FAILED: get_topping_cost() failed to return 2.1 when given 'Y'!
Test #2 FAILED: get_topping_cost() failed to return 0.55 when given 'P'!
Test #3 FAILED: get_topping_cost() failed to return 0.25 when given 'O'!
Test #4 FAILED: get_topping_cost() failed to return 0.95 when given 'N'!
Test #5 FAILED: get_topping_cost() failed to return 0.75 when given 'K'!
Test #6 FAILED: get_topping_cost() failed to return 0.85 when given 'I'!
Test #7 FAILED: get_topping_cost() failed to return 1.15 when given 'H'!
Test #8 FAILED: get_topping_cost() failed to return 0.45 when given 'C'!
Test #9 FAILED: get_specialty_cost() failed before test due to a NameError: name 'get_specialty_cost' is not defined
Test #10 FAILED: get_specialty_cost() failed before test due to a NameError: name 'get_specialty_cost' is not defined
Test #11 FAILED: get_specialty_cost() failed before test due to a NameError: name 'get_specialty_cost' is not defined
Test #12 FAILED: get_specialty_cost() failed before test due to a NameError: name 'get_specialty_cost' is not defined
Test #13 FAILED: get_specialty_cost() failed before test due to a NameError: name 'get_specialty_cost' is not defined
Test #14 FAILED: get_size_cost() failed to return 3.00 when given 'S'!
Test #15 FAILED: get_size_cost() failed to return 4.00 when given 'M'!
Test #16 passed: get_size_cost() should return 5.00 when given 'L'
Test #17 FAILED: get_sauce_cost() failed to return 2.15 when given 'W'!
Test #18 FAILED: get_sauce_cost() failed to return 1.35 when given 'R'!


"""
