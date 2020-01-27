"""
M02 Assignment: "Shipping Costs"

Objectives: 
1. Demonstrate how to correct basic syntax errors in Python.
2. Demonstrate how to create a variable in Python
3. Demonstrate how to do basic math with variables in Python
 
To complete this assignment, do the following:

1. Save a copy of this file onto your computer. 

2. Execute this python file, observing the errors.

3. Use the errors to correct the code. Continue fixing/writing code until
   all errors are gone.
   
4. Submit the error-free version of this file to the appropriate 
   assignment in Canvas.

"""

# Welcome to the "Shipping Costs" assignment. You will be writing code to 
# help compute the shipping costs of various packages for a shipping 
# company. 

# Go through this file line-by-line, readinge every comment. Follow any 
# instructions to fix code OR write new code. If you see syntax errors,
# correct them. 

# When you are finished, execute this file. If there are any errors, go back 
# and correct them. Continue the cycle of correcting/writing and executing until
# you are satisifed that there are no errors. 

# When you have reached the end of the file, save it, and submit it to 
# the appropriate assignment in Canvas. 

print("* * * * * * * * * *") # Hint: this line is correct
print("Shipping Costs Calculator") # Hint: this line is NOT correct
print("Based on my calculations...")


# There are 44 packages ready for delivery:
num_packages_ready = 
# Here you want to make num_packages_ready equal to 44
# so the correct answer is:
# num_packages_ready = 44


# Today, ten additional packages were added to the inventory:
additional_packages = 10

# We need the total number of packages to calculate shipping costs. 
# The total number of packages is equal to the sum of the number
# of packages ready and the number of additional packages:
total_packages = 44+10;

# Let's now calculate the total shipping costs. Our shipping and 
# receiving department has indicated that each package costs three
# dollars to ship. Here, we must multiply the total packages by the 
# per package shipping cost: 
total_costs = 3 * total_packages

# CHECK YOUR PROGRESS ###############################################################
# DO NOT modify anything in here. This is only here to help you check your 
# progress. 
message = f"It will cost ${int(total_costs)} to ship {total_packages} packages."
print(message)

if message == "It will cost $162 to ship 54 packages.":
  print("You completed Step 2 successfully!")
else: 
  print("You need to keep working on Step 2. Hang in there!")
  
# END STEP 2 CHECK ##################################################################




