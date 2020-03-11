"""
M10 Assignment: "User Authentication"

Repl.it Link: 

In this assignment, you'll be using the "random" module to generate a random 
password for a user. You'll also use dictionaries as a data structure to store 
usernames and passwords, and write functions that will retrive passwords, 
generate new passwords, and verify passwords. 

OVERVIEW
================================================================================

You are a programmer working at a job where you are respected and loved. A 
tier 1 tech support person has reached out to you for help: everytime they 
have to reset a user's account, they need to think up a new password for that 
user. The password is just temporary, but it still needs to be a strong 
password. 

They are Python-savvy, so if you can write them some functions to plug into 
their existing automation framework, they sure would appreciate it! 

Your task this module is to write a Python script for the tech support folks 
that contains several password-related functions involving dictionary element 
retrieval and storage. 


REFERENCES
================================================================================

* Understanding Dictionaries in Python 3
  https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3

* How to Import Modules in Python 3
  https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3

* Python Docs, Dictionary data structure: 
  https://docs.python.org/3/tutorial/datastructures.html#dictionaries

INSTRUCTIONS
================================================================================

1. Create a function named `update_username`.
    It should take three arguments, `the_records`, `old_username`, and `new_username`.
        * `the_records` should be a list of dictionaries, each dictionary containing 
          two keys: `username` and `password`
        * `old_username` is a string
        * `new_username` is a string

    It should set the value of the `username` key in the first dictionary 
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


TIPS
================================================================================

* Check out the `example_records` list for what kind of list we're dealing with. 
  It contains some example records that you can use to test your functions. 

* Feel free to have your functions printing things to help verify steps if you want, 
  but please comment out all print() calls before submitting your assignment.

"""


"""
Update the function `generate_password_for_user`.
    It should take two arguments: `the_records` and `the_user`.
        * `the_records`
"""

def generate_password_for_user(the_records, the_user):
    for record in the_records:
        if record['username'] == the_user:
            password = random.choice(word_salad_one)
            password += random.choice(word_salad_two)
            # If you don't str() the randint, you'll get this:
            # TypeError: can only concatenate str (not "int") to str
            password += str(random.randint(12345,98765))
            record.update({'password': password})
            return True
    return False
    


# Normally you would get usernames and whatnots from a database, but for the 
# purposes of this assignment, we'll just use a static data structure here:
the_records = [
        {
            username: "rossbo",
            password: None
        },
        {
            username: "picardjl",
            password: None
        },
        {
            username: ""
        }
    ]

# I am compelled by moral duty to remind you that you should NEVER store 
# passwords this way. It is incredibly insecure--but really good for learning!



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

def generate_password_for_user():
    return None # CHANGE THIS, obviously 
    
