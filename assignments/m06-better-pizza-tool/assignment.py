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

| Size   | Cost |
+--------+------+
| Large  | 5.00 |
| Medium | 4.00 |
| Small  | 3.00 |

| Sauce  | Cost |
+--------+------+
| Red    | 1.35 |
| White  | 2.15 |

| Topping    | Cost |
+------------+------+
| Cheese     | 0.45 |
| Pepperoni  | 0.85 |
| Peppers    | 0.55 |
| Mushrooms  | 0.25 |
| Ham        | 1.15 |
| Pickles    | 0.75 |
| Yogurt     | 2.10 |
| Spinach    | 0.95 |

TODO a table with the specialty pizzas and their 

ASSUMPTIONS
================================================================================
* Assume that the cost of each topping is the same for all pizza sizes
* Assume you can only have one of each topping
* Assume you can only have one of each sauce



INSTRUCTIONS
================================================================================

1. Create a function named `get_size_cost`.
   It should take one argument: the size of the pizza.
   It should return the cost of a large pizza when the argument is 'L'.
   It should return the cost of a medium pizza when the argument is 'M'.
   It should return the cost of a small pizza when the argument is 'S'.

2. Create a function named `get_sauce_cost`.
   It should take one argument: the sauce type.
   It should return the cost of red sauce when the argument is 'R'.
   It should return the cost of white sauce when the argument is 'W'.

3. Create a function named `get_topping_cost`. 
   It should take take one argument: the topping as a string (e.g., "Ham")
   It should return the cost of Cheese when the argument is "Cheese".
   It should return the cost of Pepperoni when the argument is "Pepperoni".
   It should return the cost of Peppers when the argument is "Peppers".
   It should return the cost of Mushrooms when the argument is "Mushrooms".
   It should return the cost of Ham when the argument is "Ham".
   It should return the cost of Pickles when the argument is "Pickles".
   It should return the cost of Yogurt when the argument is "Yogurt".
   It should return the cost of Spinach when the argument is "Spinach".

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

5. Create a function named `get_custom_two_topping_cost`.
   It should take four arguments: 
      - the size of the pizza as L, M, or S
      - the sauce type as R or W
      - the first topping as a string (e.g., "Pepperoni")
      - the second topping as a string (e.g., "Cheese")
   It should return the total cost
      given the selected size, sauce type, first topping, and second topping
   Note: You should be using the functions you created to retrieve the costs
         of individual things.

6. Create a function named `get_custom_three_topping_cost`.
    It should take five arguments: 
      - the size of the pizza as L, M, or S
      - the sauce type as R or W
      - the first topping as a string (e.g., "Pepperoni")
      - the second topping as a string (e.g., "Cheese")
      - the third topping as a string (e.g., "Ham")
   It should return the total cost
      given the selected size, sauce type, first topping, second topping, and 
      third topping
   Note: You should be using the functions you created to retrieve the costs
         of individual things.

7. Update function `process_choice_specialty_pizza`.
     It should use `get_specialty_cost` to return the value of a
        specialty pizza based on the user's choice.
     (Hint: I have provided the first one for you; use if-elif-else to 
      process choices. Use the else keyword to return the default value, 
      which you can find in the input() function's argument/)




TIPS FOR SUCCESS
========================================================
* You are coming up with the variable and argument names. I have provided 
  the names of the required functions only. 

* Store the values of each table in their own variables. For example, 

* How to round an integer to the nearest two decimal places:
https://stackoverflow.com/a/20457115

"""

# Create your functions starting here

# def ...

def process_choice_specialty_pizza():
  print("SPECIALTY PIZZA")
  print("=====================================================================")
  print("Select one of the specialty pizzas:")
  print("[A] The Super California      [B] The Salty Manhattan")
  print("[C] The Unkissable            [D] Meaty McMeatface")
  print("[E] The Vegetarian")
  print("---------------------------------------------------------------------")  
  
  choice = input("Selection (default A): ")
  
  if choice == ("A" or "a"):
    return get_specialty_cost("The Super California")
  # elif ...


def process_choice_custom_2topping_pizza();


def process_choice_custom_3topping_pizza():


print("Pizza Parlor Tool")
print("=======================================================================")
print("Enter the letter of your choice: ")
print("[A] Specialty Pizza")
print("[B] Custom Two Topping")
print("[C] Custom Three Topping")
choice = input("Enter Letter (default \"A\"): ")

# Process user selection
if choice == ("A" or "a"):
  process_choice_specialty_pizza()
elif choice == ("B" or "b"):
  process_choice_custom_2topping_pizza()
elif choice == ("C" or "c"):
  process_choice_custom_3topping_pizza()






