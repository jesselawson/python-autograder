"""
Chatbot Autograder

A custom autograder for the m03 Chat Bot assignment.

It works the same way as the other autograder, putting results in a results 
folder.

USAGE

cd into the folder, then:
    python chatbot-autograder.py



"""

# Read in all the student files
# For each file, execute it in subprocess for each test case. 
# Keep track of and then catalog the outcomes. 
import sys
import os 
import subprocess

print("Creating assignment results directory if need be... ", end='')
os.makedirs(f"/results", exist_ok=True) 
print("[ OK ]")

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

def jel_GeneralError(target, error):
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    return m + f"FAILED: '{target}' failed to {error}"

def jel_assert(target, expr, should_msg):
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    try:
        assert expr
    except AssertionError as e:
        return m + f"FAILED: {target} failed to {should_msg}!"
    except NameError as e:
        return m + f"FAILED: '{target}' failed to {should_msg}! NameError: {e}"
    except TypeError as e:
        return m + f"FAILED: '{target}' failed to {should_msg}! TypeError: {e}"
    else:
        return m + f"passed: '{target}' should {should_msg}"

def jel_test_script_output(filename, input_text, output_text):
    # Run the file one time for every test
    print(f"Sending '{input_text}' to {filename}... '")
    res = subprocess.Popen(
        f"python {filename}", 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE, 
        shell=True)
    # Next, flush any input from the script using a input() call. We don't want 
    # to hold up the testrunner because of some input() function.
    to_input = input_text + '\n'
    res.stdin.write(to_input.encode())
    #res.stdin.flush()

    out, err = res.communicate()

    # Wait for the process end and print error in case of failure 
    if res.wait() != 0:
        
        # If we couldn't even run the test suite, shove the subprocess call error
        # into the student results file instead
        return jel_GeneralError(
                input_text, 
                "yield '" + output_text + "'. Got nothing in response."
                )
    else:
        # Do the check here
        #out, err = res.communicate()

        if err:
            return f"[ FAIL ] Subprocess error: {err}"
        if out:
            # Format script output to control for any input() prompt strings
            script_output = out.decode().rstrip().replace(
                'What is your question? ',
                ''
            )
            return jel_assert(
                    input_text, 
                    script_output == output_text,
                    "yield '" + output_text + "'. Got '"+script_output+"'")

for filename in os.listdir('.'):
    
    # skip the assignment test suite 
    print(f"Checking filename {filename}... ", end='')
    if filename == "assignment_test_suite.py" or filename == "chatbot-autograder.py" or filename == "__pycache__" or filename == "results":
      print('[ SKIPPING ]: Reserved file ')
      continue
    
    # Each `filename` is a student submission
    student_submission_filename = filename
    
    
    # also skip over any directories
    if not os.path.isfile(student_submission_filename):
      print('[ SKIPPING ]: Not a file')
      continue
    else:
      print('[ OK ]')
    
    # Create the test files. 
    
    # Find the first underscore. This assumes canvas continues to store student 
    # submissions as lastnamefirstname_1234_1234_assignmentname.py
    student_name_index = filename.find('_')
    student_name = filename[:student_name_index]
    test_results_filename = "./results/"+filename[:-3] + "_results.txt"
    
    print(f"     * Creating test file for {student_name}'s submission... ", end='')
  
    test_results = []

    test_results.append(
        jel_test_script_output(
            filename, 
            "What is your name?", 
            "My name is CHAT BOT."
        )
    )

    test_results.append(
        jel_test_script_output(
            filename,
            "What is the answer to life?",
            "Proper hydration!"
        )
    )

    test_results.append(
        jel_test_script_output(
            filename,
            "What is 56*13?",
            "That's easy: 728!"
        )
    )

    test_results.append(
        jel_test_script_output(
            filename,
            "Are you sentient?",
            "What do you think?"
        )
    )

    test_results.append(
        jel_test_script_output(
            filename,
            "Who made you?",
            "The Mad Scientist Company made me!"
        )
    )

    test_results.append(
        jel_test_script_output(
            filename,
            "What did you cost?",
            "Total funding was $53500."
        )
    )

    test_results.append(
        jel_test_script_output(
            filename,
            "literally anything else",
            "Maybe try asking a different way."
        )
    )


    # Output results to test results file
    with open(test_results_filename, "w") as f:
        for r in test_results:
            f.write(r+'\n')