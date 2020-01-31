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

2. We stored the user's question in a variable named `question`, but something
   is wrong with the way it's declared. Go fix it. 
   
3. Find the call to `input` where we store the value of the user's input into 
   the variable `question`. Just after that, we will process the value of 
   the user's input and store the results in another variable, `response`. 
   Use the if, elif, and else keywords to process `question` as follows:
   
   3.a.
   If the user asks, "What is your name?"
   Then set `response` to be: "My name is CHAT BOT."
   
   3.b.
   If the user asks, "What is the answer to life?"
   Then set `response` to be: "Proper hydration!"

   3.c.
   If the user asks, "What is 56*13?"
   Then set `response` to be: "That's easy: 728!"

   3.d.
   If the user asks, "Are you sentinent?"
   Then set `response` to be: "What do you think?"

   3.e.
   If the user asks, "Who made you?"
   Then set `response` to be: the variable `maker` 
     along with " made me!" in a single sentence. 
     (Hint: use an f-string!)

   3.f.
   If the user asks, "What did you cost?"
   Then set `response` to be: "Total funding was $" along with 
     the sum of `total_grant_funds` and `total_donations`
     in a single sentence. 
     (Hint: use an f-string!)  
     (Hint: "Total funding was $100." is an example)

   3.g.
   If the user asks anything else, 
   Then set `response` to be: "Maybe try asking a different way."

4. Add in at least TWO more questions and answers that
   use a variable (that you will have to define) and 
   an f-string to print the answer. Be creative; it can 
   be anything! 

5. Make sure this works without errors! If there are errors, you will 
   need to fix them.

6. Submit this file to the appropriate assignment in Canvas.

Helpful tips:
* This assignment requires VERY CLOSE READING of the specifications above. 
  Ensure that your grammar, punctuation, and spelling are EXACTLY as they are 
  specified in the instructions!
* You will be marked down if you do not follow the instructions PRECISELY.

"""

maker = "The Mad Scientist Company"

total_grant_funds = 50000
total_donations = 3500

# (Hint: what do you think is wrong with the variable assignment below?)
question = input("What is your question? ")

if question == "What is your name?":
    response =  "My name is CHAT BOT."
# elif question == ??
    response = "Proper hydration!"
# ??


# Finally, we'll print the response variable
print(response)
