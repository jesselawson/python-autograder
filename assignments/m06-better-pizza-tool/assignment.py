"""

M06 Assignment "Better Pizza Tool

INTRODUCTION
================================================================================

After learning about lists and iterators, we can now go back to the Pizza 
Parlor Project code we wrote last week and begin *refactoring* it. Refactoring 
is the process of changing code, often times in ways that make it run faster, 
more efficiently, and with greater clarity. 

The first step to refactoring is identifying areas where code could be
refactored. The first and foremost area is in all these hard-coded relationships 
between some variable (size, sauce, topping, etc) and its associated cost. 

After learning about lists this module, refactor your pizza parlor project 
code 

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

TODO

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
# def ...
#   etc. 
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
  
    if choice in ['A', 'B', 'C', 'D', 'E']:
        return get_specialty_cost(choice)
    else: 
        return get_specialty_cost('A')

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