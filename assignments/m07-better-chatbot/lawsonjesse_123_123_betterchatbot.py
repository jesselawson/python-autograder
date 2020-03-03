"""
M07 Assignment: "Better Chat Bot"

Repl.it Link: https://repl.it/@professorlawson/m07-better-chatbot

Way back in Module 3, we created the first iteration of our Chat Bot. 
While we learned a lot while doing it, let's face it: that chat bot script 
was boring. You had to execute the script every time you wanted to ask it 
a question! 

So for this assignment, we are creating a new version of the chat bot script--
complete with a whole different set of business requirements. 

OVERVIEW
==================================================================================

You are a programmer working at a community college. Your Financial Aid 
department recently asked you to come up with an easy and extendable way to 
quickly check on student balances and pay them down by a certain amount. After 
a strange consulting job with a mad scientist a few weeks ago, you welcomed the 
task to work on something with practical application. 

The chatbot we are writing is operated as follows:

The user executes the script. The script greets the user. The user can then 
enter one of several COMMANDS. 

Here are the commands the user can enter:

show            This will show the balance of all students
show <id>       This will show the balance of student <id>
pay <id> <amt>  This will reduce student <id>'s balance by <amt>

Only the show command and its options have been implemented so far. For this 
project to be greenlit by Financial Aid, we need the pay command to be 
implemented.

INSTRUCTIONS
================================================================================

Implement the `pay` command.

Usage: 
        pay <id> <amount>

Example: 
        pay 122345 10.00

Explanation:
        The example command above will pay down by $10.00 the balance of 
        the student where student ID == 122345.

Demonstrations:

The following Example Commands are explained with their Desired Outcomes. These 
are not tests; these are here to help explain what the pay command should do 
in certain cases. 

| Example Command  | Desired Outcome                               |
+------------------+-----------------------------------------------|
| pay 122345 0.50  | Subtract 0.50 from balance of student         | 
|                  |   with id == 122345                           | 
| pay 122999 1.99  | Print error; 122999 is not a valid student ID |
| pay 5.00         | Print error; 5.00 is not a valid student ID   | 
+------------------+-----------------------------------------------+

Requirements:

These MUST be followed. Please read carefully. 

Implement the `pay` command. 

1. It should require three parts: <pay>, <id>, and <amount>.
  * <pay> is the word "pay"
  * <id> is a 6-digit numeric student ID
  * <amount> is a number in the form of xx.xx (e.g., 3.50 or 19.95)

2. If <id> does not exist or <id> is not in the list of student IDs:
   2.1. Print this error: "<id> is not a valid student ID!"
        where <id> is the student ID entered by the user.
   
3. If <amount> is empty or <amount> is not a number:
   3.1. Print this error: "<amount> is not a valid pay amount!"
        where <amount> is the amount entered by the user.

4. If <amount> is greater than the student's current balance:
   4.1. Print this error: "Payment too high for balance of student #<id>!"
        where <id> is the student's ID.

5. If <amount> is less than or equal to student's balance:
   5.1. Subtract <amount> from student's balance.
   5.2. Print this: "Payment posted. Balance for student #<id>: $<balance>."
        where <id> is the student's ID
        and <balance> is the student's final balance.


TIPS FOR A GOOD GRADE
================================================================================

* If an instruction is to print a string, then you must make sure 
  you are including ALL punctuation and grammar. For example, you will be
  marked down if the specification includes a period and your solution does 
  not include one. 


"""

# Data for our script
student_ids = [    122345, 122356, 122367, 122389, 122401]
student_balances = [11.50,  41.90,  35.15,  77.10, 144.98]

chatbot_name = "CHATBOT" # Please don't change this

def say(msg):
    print(f"{chatbot_name}: {msg}")

# Helper function. Look familiar?
def get_index(the_list, the_selection):
    for n in range(len(the_list)):
        if the_list[n] == the_selection:
            return n 
    return -1

def get_balance(student_id):
    i = get_index(student_ids, student_id)
    if i != -1:
        return student_balances[i]
    else:
        return "ERROR: unable to retrieve student balance!"

def show_help():
    print(f"==================================")
    print(f"FinAid BOT")
    print(f"Written by <your name>") # You should change this to your name!
    print(f"==================================")
    print(f"Available commands:")
    print(f"\tshow               Show balances for all students")
    print(f"\tshow <id>          Show balance for student")
    print(f"\tpay <id> <amt>     Subtract <amt> from student's balance")

def process_input(msg):

    # First, split the argument into a list of individual words
    words = msg.split()

    if words[0] == "show":
        if len(words) > 1: # If there's something after "show"
            if words[1].isdigit(): # If that something is a number
                # Make sure it's a valid student id
                if int(words[1]) not in student_ids:
                    say(f"{words[1]} is not a valid student ID!")
                    return # stop processing the function
                else: 
                    say(f"Student #{words[1]} has a balance of ${get_balance(int(words[1])):.2f}.")
            else:
                say(f"\"{words[1]}\" is not a valid student ID!") 
        else:
            print(f"+------------+--------")
            print(f"| Student ID | Balance")
            print(f"+------------+--------")
            for i,student in enumerate(student_ids):
                print(f"|    {student}  | ${round(student_balances[i],2):.2f}")
            print(f"+------------+--------")
    elif words[0] == "help":
        show_help()
    elif words[0] == "pay":

        # First check if we even have the appropriate amount of arguments. 
        # We should have 3: pay <id> <amount>, so len(words) must be == 3
        if len(words) == 3:
            id = int(words[1])
            amount = float(words[2]) # This will fail is anything other than 
                                         # an int or float is entered

            # Check if words[1] is a valid student ID
            if id in student_ids:
                # Student found!
                
                index = get_index(student_ids, id)
                if amount <= student_balances[index]:
                    # Okay to proceed
                    student_balances[index] -= amount
                    print(f"Payment posted. New balance for student #{id}: ${student_balances[index]}.")
                else:
                    print(f"Payment too high for balance of student #{id}!")
            else:
                print(f"{id} is not a valid student ID!")

        
        else:
            print(f"USAGE: pay <id> <amount>")
    else:
        say("I did not understand that request :<")
        say("Try \"help\" for a list of commands.")
        say("Type \"quit\" (without quotes) to exit.")
    

def do_chatbot():
    
    print(f"{chatbot_name}: How can I help today?")

    print(f"> ", end='') 
    c = input()

    if c == "quit":
        return False
    else:
        process_input(c)
        return True


def main():
    # TODO: Replace this with a comment section that the student has to fill
    # in based on the tutorial I will write on my site.
    is_running = True

    while(is_running):
        is_running = do_chatbot()

    say("Goodbye!")


if __name__ == '__main__':
    main()