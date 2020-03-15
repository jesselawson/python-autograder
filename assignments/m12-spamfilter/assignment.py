"""
M12 Project: "Spam Filter"

Repl.it Link: 

In this assignment, you'll be exploring more filesystem operations as you build 
a very simple spam filter for an email server. 

OVERVIEW
================================================================================





INSTRUCTIONS
================================================================================

1. Create a function named `update_username`.
    It should take three arguments, `the_records`, `old_username`, and `new_username`.
        * `the_records` should be a list of dictionaries, each dictionary containing 
          two keys: `username` and `password`
        * `old_username` is a string
        * `new_username` is a string

    It should set the value associated with the `username` key in the first dictionary 
    element of `the_records` to the value of `new_username` 
        where that element's username value is equal to `old_username`.
    It should return True if the `old_username` was found and successfully updated 
        to the `new_username`.
    Otherwise, it should return False. 

2. Create a function named `generate_password_for_user`.
    It should take two arguments: `the_records` and `the_user`.
        * `the_records` should be a list of dictionaries, each dictionary containing 
          two keys: `username` and `password`
        * `the_user` is a string.
    It should set the value associated with the `password` key in the first dictionary
        element of `the_records` to be a string in the folowing format:
            "{a}{b}{c}"
            where
                a == a random choice from the list word_salad_one
                b == a random choice from the list word_salad_two
                c == a random integer between 12345 and 98765
        where that element's `username` value is equal to `the_user`.
    It should return True if the `the_user` was found and the associated 
        `password` key value successfully updated in accordance with the above criteria.
    Otherwise, it should return False.     
    
    Example code for building a pseudo-random password from two lists and an integer:
    ```
        my_new_password = random.choice(some_list)
        my_new_password += random.choice(some_other_list)
        range_start = 1
        range_end = 10
        my_new_password += str(random.randint(range_start,range_end))
    ```

TIPS
================================================================================

* Check out the `example_records` list for what kind of list we're dealing with. 
  It contains some example records that you can use to test your functions. 

* Feel free to have your functions printing things to help verify steps if you want, 
  but please comment out all print() calls before submitting your assignment.

* Remember that we are using the `random` module, so your script will need to 
  `import` it somehow... (how do we import modules again?)

"""


# Normally you would get usernames and whatnots from a database, but for the 
# purposes of this assignment, we'll just use a static data structure here:
the_records = [
    {
        "username": "rossbo",
        "password": None
    },
    {
        "username": "picardjl",
        "password": None
    },
    {
        "username": "lawsonje",
        "password": "hunter2"
    }
]

# I am compelled by moral duty to remind you that you should NEVER store 
# passwords this way. It is incredibly insecure--but really good for learning!

# We'll use these "word salad" lists to generate pseudo-random passwords
word_salad_one = [
    'Happy', 'Excited', 'Depressed', 'Anxious', 'Nervous', 'Smelly'
]

word_salad_two = [
    'Fish', 'Goat', 'Butterfly', 'Elephant', 'Zebra', 'Cat', 'Mouse'
]




# Modify the below function to satisfy the assignment instructions.
# Example expected output:
#
# A. update_username(the_records, "rossbo", "rogersfr") == True, since 
#       the function should find "rossbo" in the available usernames
#
# B. update_username(the_records, "smithdo", "rogersfr") == False, since 
#       the function should not find "smithdo" in the available usernames
def update_username():
    return None # CHANGE THIS, obviously

# You can do this one on your own. I believe in you!
def generate_password_for_user():
    return None # CHANGE THIS, obviously 
    



# BEFORE YOU SUBMIT YOUR ASSIGNMENT:
# Did you remember to get rid of all errors?
# Did you remember to import the `random` module?
# Did you remember to drink water today?