# autograder.py MERCURY edition


import sys
import os
import os.path
import shutil
from pathlib import Path
import subprocess
from datetime import datetime

"""
class Submission:
  def __init__(self):
    student_name = ""
    # Controls for two student with similar names/filenames
    student_random_id = uuid.uuid4().hex 
"""


def banner():
  print("* * ** *** ***** *********")
  print("* AUTOGRADER (version mercury-a19)")
  print("* Written by Jesse Lawson <jesselawson@protonmail.com>")
  print("* * ** *** ***** *********")
  

def usage():
  banner()
  print("Usage: ")
  print(" python autograder.py <nameofassignment>")
  print(" (ensure <nameofassignment> is a subfolder containing a test suite and all student submissions)")
  print("* * *")
  
def die():
  print("Autograder is shutting down... ")
  # TODO: any logging or statistics here
  
  sys.exit()
  
def main():
  
  # Ensure we get an assignment 
  try:
    sys.argv[1]
  except IndexError:
    print("[ ERROR ] You must specify an assignment! See usage below.")
    usage()
    die()
    
  banner()
  
  assignment_directory = sys.argv[1]
  test_suite_filename = assignment_directory + "/assignment_test_suite.py"
  test_suite_contents = None
  
  print("Checking assignment directory for existence... ", end='')
  if not os.path.isdir(assignment_directory):
    print(f'[ FAILED ]: Directory \'{assignment_directory}\' does not exist!')
    die()
  else: 
    print("[ OK ]")

  print("Creating assignment results directory if need be... ", end='')
  os.makedirs(f"{assignment_directory}/results", exist_ok=True) 
  print("[ OK ]")
    
  print("Checking assignment directory for test suite... ", end='')
  if not os.path.isfile(test_suite_filename):
    print(f'[ FAILED ]: Could not find {test_suite_filename}!')
    die()
  else: 
    print("[ OK ]")
      
  print("Reading test suite into memory... ", end='')
  
  try:
    test_suite_contents = Path(test_suite_filename).read_text()
  except:
    print("[ FAILED ] Could not read test suite file!")
    die()
  else: 
    print("[ OK ]")
  
  # Loop through all student assignments and create a test file using the 
  # contents of the test suite file 
  print("Creating individualized test files... ")
  for filename in os.listdir(assignment_directory):
    
    # skip the assignment test suite 
    print(f"Checking filename {filename}... ", end='')
    if filename == "assignment_test_suite.py" or filename == "assignment.py" or filename == "__pycache__":
      print('[ SKIPPING ]: Reserved file ')
      continue
    
    # Create a var to hold the relpath to the student submission file 
    student_submission_filename = assignment_directory + "/" + filename
    
    
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
    student_test_filename = assignment_directory+"/results/"+filename[:-3] + "_test.py"
    
    print(f"     * Creating test file for {student_name}'s submission... ", end='')
  
    # Read contents of student submission into memory
    submission_file = open(student_submission_filename, "r")
    submission_file_contents = submission_file.read()
    submission_file.close()

    the_date = datetime.now()
    timestamp = the_date.strftime("%d-%b-%Y")
    
    # Generate the test file for the student
    test_file = open(student_test_filename, "w")
    test_file.write("import pytest\nimport sys\n")
    test_file.write(submission_file_contents)
    test_file.write(
      (
        f"\n\n\n\n\n\n\n\"\"\"\n"
        f"({timestamp} Professor Lawson) Below you will find all the test \n"
        f"functions I have used to evaluate your submission. You are free to \n"
        f"download this file and tinker around with it. In fact, \n"
        f"I encourage it!\n\n\"\"\"\n\n"
      )
    )
    test_file.write(test_suite_contents)
    test_file.write(f"\n\n\n\n")
    test_file.close()
  
    print("[ OK ]")

    # Spawn a sub process that runs pytest and saves output into a results file
    student_results_filename = f"{assignment_directory}/results/{filename}_testresults.txt"
    
    #subprocess.call(f"pytest -q --tb=line {student_test_filename}  > {student_results_filename}", shell=True)
    
    

    # Custom autograder testrunner. 
    # Collects all functions that start with "test_" from the submission file 
    # and runs those tests.
    print(f"     * Executing test runner...", end='')
    subprocess.call(f"python {student_test_filename}  > {student_results_filename}", shell=True)
    print("[ OK ]")

    # Append results to end of test file
    r = open(student_results_filename, "r")
    test_results = r.read()
    r.close()
    
    print(f"     * Adding test results to student test file... ", end='')
    f = open(student_test_filename, "a")
    f.write(f"\n\"\"\"\n")
    f.write(f"TEST RUNNER RESULTS\n======================================\n")
    f.write(f"Assignment: {assignment_directory}\nStudent: {student_name}\nCompiled: {timestamp}\n\n")	
    f.write(test_results)
    f.write(f"\n\"\"\"\n")
    f.close()
    print("[ OK ]")
    
    
    

    # pytest.main('the file')
    # if 0, tests passed
    # if 1, tests failed

if __name__ == '__main__':
  sys.exit(main())
  

  
  
  
  
  
