"""

M06 "Better Pizza Calculator"

INTRODUCTION
================================================================================

Last week, we build a calculator for the owner of a pizza parlor to quickly 
get prices for pizzas and, perhaps most importantly, display the price at which 
the owner should sell the pizzas so that she keeps a 30% profit margin. 

This week, we are going to refactor parts of that tool to create a more efficient
system for calculating total costs. We aren't going to rewrite the whole tool, 
but you are more than welcome to do that on your own time. In fact, I encourage 
you to incorporate the work you will do in this week's assignment with your 
pizza calculator from last week as a personal challenge. 


- Professor Lawson

OVERVIEW
================================================================================
This week we are refactoring parts of our pizza calculator. Our main goal is to 
centralize all of the data we will use (i.e., the prices of everything) into 
a single location in the script, giving us an easier way to update the script 
when the prices inevitably change in the future. 

We are not rewriting the whole thing. In fact, the starter code below does not 
include a lot of the code that you wrote last week. However, something new that 
I have included are *unit tests*. When you click the big "run" button here on 
Repl.it--or when you execute the file on your computer--you will see the result 
of all the tests at the end of this file. 

To receive full credits for this assignment, all your tests must pass. If you have 
a failing test, you will be marked down. 

Here are the information tables from Module 5. We will still be using these.

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

1. Update the three toppings lists--`topping_ids`, `topping_names`, and
   `topping_costs`.
   They should contain all the IDs, names, and costs in the correct 
   list positions for the toppings from the provided tables in the Overview 
   section of this assignment.

2. Update the three size lists--`size_ids`, `size_names`, and
   `size_costs`.
   They should contain all the IDs, names, and costs in the correct 
   list positions for the sizes from the provided tables in the Overview 
   section of this assignment.

3. Update the three sauce lists--`sauce_ids`, `sauce_names`, and
   `sauce_costs`.
   They should contain all the IDs, names, and costs in the correct 
   list positions for the sauces from the provided tables in the Overview 
   section of this assignment.

4. Update the three specialty lists--`specialty_ids`, `specialty_names`, and
   `specialty_costs`.
   They should contain all the IDs, names, and costs in the correct 
   list positions for the specialty pizzas from the provided tables in the Overview 
   section of this assignment.
   They MUST use `get_topping_cost()` to get the appropriate topping costs.
   I highly recommend you store the costs in a separate variable, like I have 
     done for `specialty_a_cost` and `specialty_b_cost`.

5. Add at least one custom specialty pizza to the lists from #4 above. You can name it 
   anything you want as long as its G-rated, and add any combination of toppings you want.

6. Modify the function `get_size_cost`.
   It should take one argument, the id of the pizza size.
   It should use `get_index_from_selection` to return the cost 
      of the pizza size when given the ID. 
   Hint: use `get_topping_cost` as a reference.

7. Modify the function `get_sauce_cost`.
   It should take one argument, the id of the sauce type.
   It should use `get_index_from_selection` to return the cost 
      of the pizza sauce when given the ID. 
   Hint: use `get_topping_cost` as a reference.

8. Modify the function `get_specialty_cost`.
   It should take one argument, the id of the specialty pizza.
   It should use `get_index_from_selection` to return the cost 
      of the specialty pizza when given the ID. 
   Hint: use `get_topping_cost` as a reference.

9. Modify the function `get_sauce_selection`.
   It should use a for loop to enumerate over the `sauce_names` list,
   and print the ID, name, and cost of each element.
   Hint: use `get_size_selection` as a reference.

10. Modify the function `get_specialty_selection`.
   It should use a for loop to enumerate over the `specialty_names` list,
   and print the ID, name, and cost of each element.
   Hint: use `get_size_selection` as a reference.

11. There should be no errors when you run this script. 

12. Save your file as "betterpizzacalc.py". 

13. Upload this completed file to the assignment in Canvas.

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

# This is a helper function that I am providing to you. We built this in the 
# demo here: https://repl.it/@professorlawson/m06-lists-toppings-demo
def get_index_from_selection(the_list, the_selection):
    """
    Returns the index value from the_list where the_selection is found.
    Returns -1 if no the_selection is found in the_list.
    """
    # Loop over all the elements in the_list
    for n in range(len(the_list)):
        if the_list[n] == the_selection:
            # Return the index number (n)
            return n 

    # This next part is out of the scope of the for-loop, so the only way 
    # it will trigger is if we looped through each item in the for-loop 
    # and the if-condition was not satisifed. In other words, we only 
    # return -1 if no items in the list match the selection.
    return -1




"""
TOPPINGS 
Make sure you add one new element to each list, and that each 
element lines up with the associated data (e.g., the value at 
topping_ids[x] is associated with topping_costs[x], etc etc)
"""
topping_ids =   [     'C',         'I',       'P','O','H','K','Y','N']
topping_names = ['Cheese', 'Pepperoni', 'Peppers','Mushrooms','Ham','Pickles','Yogurt','Spinach']
topping_costs = [    0.45,        0.85,      0.55,0.25,1.15,0.75,2.10,0.95]

# Get the cost of a topping
def get_topping_cost(topping_id):
    # Returns the cost of a topping based on its topping_id
    return topping_costs[get_index_from_selection(topping_ids, topping_id)]

"""
SIZES
"""
size_ids =   ['S','M','L']
size_names = ['Small', 'Medium', 'Large']
size_costs = [3.00, 4.00, 5.00]

# Get the cost of a size
def get_size_cost(size_id):
    return size_costs[get_index_from_selection(size_ids, size_id)]

"""
SAUCE TYPES
"""
sauce_ids =   ['R', 'W']
sauce_names = ['Red', 'White']
sauce_costs = [1.35, 2.15]

# Get the cost of a sauce type
def get_sauce_cost(sauce_id):
    return sauce_costs[get_index_from_selection(sauce_ids, sauce_id)]

"""
SPECIALTY PIZZAS
"""
specialty_ids =   ['A', 'B', 'C', 'D', 'E']
specialty_names = ['The Super California', 'The Salty Manhattan', 'The Unkissable', 'Meaty McMeatface', 'The Vegetarian']

# The Super California
specialty_a_cost = get_topping_cost('C') + get_topping_cost('Y') + get_topping_cost('N')

# The Salty Manhattan
# Note how I am using the backslash character \ to break up long lines of code
specialty_b_cost = get_topping_cost('H') + get_topping_cost('O') + \
                    get_topping_cost('C') + get_topping_cost('K')

specialty_c_cost = get_topping_cost('K') + get_topping_cost('Y')
specialty_d_cost = get_topping_cost('C') + get_topping_cost('I') + get_topping_cost('P') + get_topping_cost('O')
specialty_e_cost = get_topping_cost('O') + get_topping_cost('N')

# When you're done creating variables for each specialty pizza, stick them 
# in the list below
specialty_costs = [specialty_a_cost, specialty_b_cost,specialty_c_cost,specialty_d_cost,specialty_e_cost]

# Get the cost of a specialty pizza
def get_specialty_cost(specialty_id):
    return specialty_costs[get_index_from_selection(specialty_ids, specialty_id)]



def get_topping_selection(excluded_topping=''):
    print("\nSelect a topping: ")
    for i,topping in enumerate(topping_names):
        if topping_ids[i] != excluded_topping: # Omit this from the functions below
            print(f"[{topping_ids[i]}] {topping} (${round(topping_costs[i], 2)})")
    return input(f"Your selection? (Default: {topping_ids[0]}) ")

def get_size_selection():
    print("\nSelect a size:")
    for i,size in enumerate(size_names):
        print(f"[{size_ids[i]}] {size} (${round(size_costs[i], 2)})")
    return input(f"Your selection? (Default: {size_ids[0]}) ")
  
def get_sauce_selection():
    print("\nSelect a sauce:")
    for i,sauce in enumerate(sauce_names):
        print(f"[{sauce_ids[i]}] {sauce} (${round(sauce_costs[i], 2)})")
    return input(f"Your selection? (Default: {sauce_ids[0]}) ")

def get_specialty_selection():
    print("\Select a specialty pizza:")
    for i,specialty in enumerate(specialty_names):
        print(f"[{specialty_ids[i]}] {specialty} (${round(specialty_costs[i], 2)})")
    return input(f"Your selection? (Default: {specialty_ids[0]}) ")

"""
Everything below is provided to you so that the script will execute correctly.
You do not need to modify anything below.
"""
def get_choice_custom_2topping_pizza():
    print("CUSTOM 2-TOPPING PIZZA")
    print("===================================================================")
    
    # Create some variables to hold the topping IDs
    topping1 = get_topping_selection()
    topping2 = get_topping_selection(topping1)

    # Get the index location from the topping_ids list so we can 
    # get the associated data from topping_costs and topping_names
    index1 = get_index_from_selection(topping_ids, topping1)
    index2 = get_index_from_selection(topping_ids, topping2)

    # Calculate the total cost with both toppings
    total_toppings_cost = round(get_topping_cost(topping1) + get_topping_cost(topping2), 2)

    return round(total_toppings_cost, 2)

def get_choice_specialty_pizza():
    print("SPECIALTY PIZZA")
    print("===================================================================")
      
    choice = get_specialty_selection()

    return get_specialty_cost(choice)
    
# All the main program logic will exist inside the main() function, which is 
# called at the very end of this file with "sys.exit(main())".
# Need a refresher? https://realpython.com/python-main-function/
def main():
    print("Pizza Parlor Tool")
    print("===================================================================")

    size = get_size_selection()
    sauce = get_sauce_selection()
    
    print("Enter the letter of your choice: ")

    print("[A] Specialty Pizza")
    print("[B] Custom Two-Topping Pizza")
    print("-------------------------------------------------------------------")
    choice = input("Selection (default B): ")

    # Calculate total cost of pizza given size, sauce, and topping selections 
    # based on whether they selected A or B at the menu
    
    # Start with zero
    total_cost = 0
    
    # Process user selection. 
    if choice == 'A':
        # If the user selected "[A] Specialty Pizza", increase total_cost
        # by the return value of get_choice_specialty_pizza()
        total_cost += get_choice_specialty_pizza()
    else:
        # If the user selected "[B] Custom Two-Topping Pizza", increase 
        # total_cost by the return value of get_choice_custom_2topping_pizza()
        total_cost += get_choice_custom_2topping_pizza()

    # Add the size and sauce costs
    total_cost += get_size_cost(size)
    total_cost += get_sauce_cost(sauce)

    # Finally, add 30% markup
    final_cost = total_cost * 1.30

    # Output the totals. I'm using round() to ensure that no number is displayed
    # with more than two decimal places. Do you think it's necessary for me 
    # to repeat these calls to round() here?
    print('-------------------------------------------------------------------')
    print(f"Cost to make: ${round(total_cost, 2)}")
    print(f"Sale price: ${round(final_cost, 2)}")
    print(f"Total profit: ${round(final_cost - total_cost, 2)}")

# If you don't remember why we do this, read here: 
# https://realpython.com/python-main-function/
if __name__ == '__main__':
    main()