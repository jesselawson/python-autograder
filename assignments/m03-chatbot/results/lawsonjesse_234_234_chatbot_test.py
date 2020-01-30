import pytest
import sys
"""
M03 Assignment: "Chat Bot"

Repl.it Link: https://repl.it/@professorlawson/chat-bot

A mad scientist has asked you to help her write a program to convince 
investors that she has created a sentient chat bot.

This chat bot comes to life when you execute the script. You can ask it 
one question, it will attempt to answer that question, then the program 
will finish. 

You will have to run the program each time you want to ask it a 
question. 

To complete this assignment, do the following:
 
1. Correct any variable name inconsistencies, lack of declaration, 
   or typos first.

2. Find the function `process_input`, where we are checking the user's 
   question (we stored the question in a variable named `question`), and use 
   the if, elif, and else keywords to process `question` as follows:
   
   2.a.
   If the user asks, "What is your name?"
   Then set `response` variable to "My name is CHAT BOT."
   
   2.b.
   If the user asks, "What is the answer to life?"
   Then set `response` variable to "Proper hydration!"

   2.c.
   If the user asks, "What is 56*13?"
   Then set `response` variable to "That's easy: 728!"

   2.d.
   If the user asks, "Are you sentinent?"
   Then set `response` variable to "What do you think?"

   2.e.
   If the user asks, "Who made you?"
   Then set `response` variable to the variable `maker` 
     along with " made me!" in a single sentence. 
     (Hint: use an f-string!)

   2.f.
   If the user asks, "What did you cost?"
   Then set `response` variable to "Total funding was $" along with 
     the sum of `total_grant_funds` and `total_donations`
     in a single sentence. 
     (Hint: use an f-string!)  
     (Hint: "Total funding was $100." is an example)

   2.g.
   If the user asks anything else, 
   Then set `response` variable to "Maybe try asking a different way."

3. Add in at least TWO more questions and answers that
   use a variable (that you will have to define) and 
   an f-string to print the answer. Be creative; it can 
   be anything! 

4. Make sure this works without errors! If there are errors, you will 
   need to fix them.

5. Submit this file to the appropriate assignment in Canvas.

"""

maker = "The Mad Scientist Company"

total_grant_funds = 50000
total_donations = 3500

print("I am alive!")

# (Hint: what do you think is wrong with the variable assignment below?)
kwestion = input("What is your question? ")

# Create a function called `process_input` that takes one string variable 
# argument called `question` and 
def process_input(question):
  if question == "What is your name?":
    response = "My name is CHAT BOT."
  # ??



# Finally, we'll print the response variable

print(response)

print("Goodbye!")






"""
(29-Jan-2020 Professor Lawson) Below you will find all the test 
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


# Testing injection 

def test_this_is_a_test():
  jel_assert("the injector", 
    test_qwertyuioplkjhgfdsa_number != None,
    "injects the code correctly"
  )

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
Assignment: m03-chatbot
Student: lawsonjesse
Compiled: 29-Jan-2020

Traceback (most recent call last):
  File "m03-chatbot/results/lawsonjesse_234_234_chatbot_test.py", line 94, in <module>
    print(response)
NameError: name 'response' is not defined

"""
