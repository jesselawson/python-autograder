"""
M02 Assignment: "Shipping Costs"

DIRECTIONS 
1. Read through this file, completing the tasks as required. Pay attention 
   to the comments because that is where you will find out what to do. 

2. When you are finished, upload this file to the Canvas assignment. 

"""

### Let's begin!

"""
In this assignment, you'll be writing a very basic shipping costs calculator 
for Big Tuna's Shipping Company. This calculator will be static and 
simply calculate the shipping costs based on the code. In other words, 
there is no interactive component. 
"""

# Below you will see some print statements that output the name
# of the program. But something is wrong! Correct the Python code 
# below so that the print statements will work.

print("* * * * * * * * * *") # Hint: this line is correct
print("Shipping Costs Calculator")
print("Written by <your name>") # Put your name in the print statement!
               
# At Big Tuna's Shipping Company, there are 44 packages ready. 
# Create a variable named "num_packages_ready" to hold that value.
num_packages_ready = 44 # I did this one for you.

# Ten additional packages came in last night from a midnight flight. 
# Create a variable named "additional_packages" to hold that value:
additional_packages = 10

# We need the total number of packages to calculate shipping costs. 
# The total number of packages is equal to the sum of the number
# of packages ready and the number of additional packages. 
# Create a new variable called "total_packages", and make its value 
# equal to the sum of "num_packages_ready" and "additional_packages":
total_packages = num_packages_ready + additional_packages

# Let's now calculate the total shipping costs. Our shipping and 
# receiving department has indicated that each package costs three
# dollars to ship. 
# Create a variable called "package_cost" to hold the shipping cost
# of each individual package (hint: <variable> = 3)
package_cost = 3

# Now let's figure out the total cost of all these packages. 

# Create a variable called "total_costs" and set its value to be equal to 
# the the sum of all packages (the number of packages ready plus the 
# additional packages) multiplied by the individual package cost:
total_costs = package_cost * total_packages


# If you did everything correctly, you should be able to execute this 
# script and see the message "(You did it!)" If, instead, you see
# the message "(Uh oh!)", that means you need to go back and carefully 
# read through the comments, ensuring you followed the directions. 










################# Professor Lawson's Section ###########################
# You can ignore everything below this, or keep reading if you're curious.
# This is all stuff you'll learn about very soon. I like to 
# keep code like this in your assignments because it shows you some
# practical application of the concepts you will learn in this course.
# 
# Feel free to tinker around with this and explore--but only AFTER you have 
# completed and turned in this assignment!
########################################################################

message = f"It will cost ${int(total_costs)} to ship {total_packages} packages."

if message == "It will cost $162 to ship 54 packages.":
  print("(You did it!)")
else: 
  print("(Uh oh!)")






### BEGIN AUTOGRADER INJECTION ###

# Test helpers for shipping costs assignment

def get_num_packages_ready():
	num_packages_ready
		
def get_additional_packages():
	additional_packages
	
def get_total_packages():
	total_packages

def get_total_costs():
	total_costs



### END AUTOGRADER INJECTION ###

