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

| ID  | Specialty Pizza      | Toppings                              | Specialty
+-----+----------------------+---------------------------------------+ Pizzas
|  A  | The Super California | Cheese, Yogurt, Spinach               |
|  B  | The Salty Manhattan  | Ham, Mushrooms, Cheese, Pickles       |
|  C  | The Unkissable       | Pickles, Yogurt                       |
|  D  | Meaty McMeatface     | Cheese, Pepperoni, Peppers, Mushrooms |
|  E  | The Vegetarian       | Mushrooms, Spinach                    |


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
    It should take one argument: 
        the name of the specialty pizza
        OR
        the ID of the specialty pizza
    It should return the cost of all toppings for The Super California
        when the argument is A'.
    It should return the cost of all toppings for The Salty Manhattan
        when the argument is 'B'.
    It should return the cost of all toppings for The Unkissable
        when the argument is 'C'.
    It should return the cost of all toppings for Meaty McMeatface
        when the argument is 'Meaty McMeatface'.
    It should return the cost of Mushrooms and Spinach
        when the argument is 'The Vegetarian'.
    Note: You should be using the functions you created in 1, 2, and 3.

5. Update function `process_choice_specialty_pizza`.
    It should take one argument: the specialty pizza ID as `choice`.
    It should return the specialty cost of the pizza corresponding to `choice`
        when `choice` is 'A', 'B', 'C', 'D', or 'E'
        using the get_specialty_cost function.
        Otherwise, 
        It should return the specialty cost of the pizza corresponding to 'A'
        using the get_specialty_cost function.
    
    (Hint: You should be using get_specialty_cost to get the cost of a 
    specialty pizza; you should not be hard-coding numbers into this function.)

6. Update function `main`. 
    Find the comment section starting with the comment `PROCESS USER SELECTION`.
    Underneath that, create an if-elif-else block according to the 
    comments in that section.

7. Update function `main`.
    Find the comment section starting with the comment `ADD SIZE AND SAUCE TYPE COSTS`.
    Underneath that:
        increment total_costs by the sauce cost given `sauce`;
        increment total_costs by the size cost given `size`.

8. Update the function `main`.
    Find the comment section starting with the comment `CALCULATE FINAL COST`.
    Underneath that:
        create a variable named `final_cost`. 
        It should be equal to total_costs + 30%.
    (Hint: Follow the instructions in the comment section in the main() function!)
    
9. Update the comment section at the bottom of this code file that starts with 
   "HOW TO USE THIS SCRIPT". 
   
   Write detailed instructions for Michelle, the person who will be using this 
   script, detailing how to run it and when to make what choices. Be as 
   thorough or succinct as you feel necessary. Be sure to mention that she 
   needs to remember to select two different toppings when building a custom 
   two-topping pizza since there is nothing that checks whether topping1 
   is the same as topping2--but communicate this to her in a non-programmer way. 
   
   Assume she only knows how to execute the file; she doesn't know the Python
   programming language.
   
   Include enough detailed instructions for a non-programmer to be confident 
   in how to use this script.

10. There should be no errors when you run this script. 

11. Upload this completed file to the assignment in Canvas.

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

def process_choice_specialty_pizza(choice):
    return 0.00 # Remove this and follow the directions from INSTRUCTIONS #5

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

# get_choice_custom_2topping_pizza
# DESCRIPTION
#   Queries the user to get the first and second topping for a custom 
#   two-topping pizza, then returns the sum cost of both toppings.
# USAGE     
#   total = get_choice_custom_2topping_pizza()
#   ... 
#   print(f"Total cost: ${total}")
def get_choice_custom_2topping_pizza():
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

# get_choice_specialty_pizza
# DESCRIPTION
#   Queries the user to get the name of the specialty pizza they want, 
#   then returns the cost of that pizza using `get_specialty_cost()`
# USAGE     
#   total = get_choice_specialty_pizza()
#   ... 
#   print(f"Total cost: ${total}")
def get_choice_specialty_pizza():
    print("SPECIALTY PIZZA")
    print("===================================================================")
    print("Select one of the specialty pizzas:")
    print("[A] The Super California      [B] The Salty Manhattan")
    print("[C] The Unkissable            [D] Meaty McMeatface")
    print("[E] The Vegetarian")
    print("-------------------------------------------------------------------")  
  
    choice = input("Selection (default A): ")

    return process_choice_specialty_pizza(choice)
    
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
    
    """ PROCESS USER SELECTION
    |    
    |   If the user selected "[A] Specialty Pizza" (e.g., if choice is 'A'), 
    |   increase total_cost by the return value of get_choice_specialty_pizza()
    |   
    |    But if the user selected "[B] Custom Two-Topping Pizza", 
    |   increase total_cost by the return value of get_choice_custom_2topping_pizza()
    |   
    |   Otherwise, assume the choice was 'A'.
    |
    |   (Hint: Write your if-elif-else block right below this comment block, 
        BEFORE the part below where we add the size and sauce costs)
    |
    |"""

    # if ...
    # elif ...
    # else ...

    # ADD SIZE AND SAUCE TYPE COSTS
    # total_cost += ??
    # total_cost += ??

    # CALCULATE FINAL COST
    # Finally, create a variable `final_cost` 
    # and set it to be total_cost with 30% markup.
    # (Hint: To add a 10% markup to a hypothetical variable `wine_cost`, 
    #  you would do this: final_cost = wine_cost + (wine_cost * 0.30))
    final_cost = 0.00 # CHANGE THIS

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