"""
M12 Assignment: "Fish and Classes"

Repl.it Link: 



OVERVIEW
================================================================================

This module we're following along with the DigitalOcean Objects and Classes 
tutorials. This assignment directly come from the example Shark class, so 
don't try to complete this assignment until you have followed along with the 
tutorials.

REFERENCES
--------------------------------------------------------------------------------

How to Construct Classes and Define Objects in Python 3:
    https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3

Understanding Class and Instance Variables in Python 3:
    https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3


TIPS
--------------------------------------------------------------------------------

* Use the class Discord server to work with your classmates through any issues 
or concerns you may have. Your professor will be there also to help guide 
discussions and provide support. 

* Class variables are ones that are set outside the constructor (__init__), 
  whereas class instance variables are declared and made available by 
  setting them inside the constructor.

* When a member function takes X arguments, you will actually be declaring 
  X+1 parameters, since all member functions will have `self` as the first 
  parameter. 

INSTRUCTIONS
================================================================================


1.  Replace the class instance variable `age` with a new variable named `health`. 
    Both the parameter list in the constructor and the variables declared inside 
    the constructor must be updated. 
    The constructor should now be __init__(self, name, health)
 
2.  Create a member function of the shark class named `get_health`.
    It should return the class instance variable `health`.

3.  Create a member function of the Shark class named `bite`.
    It should take one argument: `target`, which will be another Shark object. 
    It should subtract 25 from the `target` object's health.
    It should check if the `target`'s health is now less than zero, and if so, 
        it should call target.die()

4.  Create a member function of the Shark class named `die`.
    It should set the instances' `health` to zero.
    It should use `print()` to output a string that indicates the shark is dead. 
        You may have the string say whatever you want.
        Example: "The shark named {self.name} has died :<"


"""


class Shark:

    def __init__(self, name, age):
        self.name = name
        self.age = age



# Please remove the main() function when you turn in your assignment. You can 
# keep it here while you are developing and testing, of course, but I don't 
# need it to grade your submission.
def main():

    # Create some sharks
    shark1 = Shark("Dwight", 50)
    shark2 = Shark("Jim", 50)

    # Some code to play with. How can you get these to work?
    #shark1.bite(shark2)
    #print(f"{shark2.name}'s health is now {shark2.get_health()}")



if __name__ == "__main__":
    main()