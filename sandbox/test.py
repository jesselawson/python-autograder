import subprocess


# How to handle two students with the same name? Need their student ID...

student_test_filename = "student_test.py"
student_results_filename = "lawsonjesse_funwithfunctions_results.txt"
subprocess.call(f"pytest -q --tb=line {student_test_filename}  > {student_results_filename}", shell=True)