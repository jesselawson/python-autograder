
# Overview

Python Autograder

1. For each assignment, create a "assignment_test_suite.py" file. These will be 
   the unit tests that will run off of the student's test file. The way they work 
   is by being automatically injected into the bottom of each student's code file. 
3. Download all student submissions and place them into "assignments/assignmentname" folder.
4. Place the correct "assignment_test_suite.py" into the assignmentname folder. 
5. Place "autograder.py" into the assignments folder and run it: python autograder.py assignmentname

For example, if you have an assignment named "shippingcosts":

assignments/ 
	autograder.py
	test_template.py 
	shippingcosts/ 
		assignment_test_suite.py
		sub1.py
		sub2.py
		etc

You would run this like so:

`python autograder.py shippingcosts`

Find the results in the `assignments/shippingcosts/results` folder.



		
DEVLOG

- **4-Mar-2020 Jesse Lawson** 

The chatbot assignments have their own custom grader, since each assignment 
has custom stdout activity that needs to be tracked. Since a subprocess is used
to spin up each assignment's tests, there are special ways of testing the 
output of the script based on inputs. This can, of course, be customized 
further than what is already available. 

- **29-Jan-2020 Jesse Lawson** 

Decoupled the test suite file for assignments. Now the assignment test suite file 
will just be the test functions, and there will be a `test_template.py` file that 
has a special marker (`#<INJECTION_MARKER>`) to indicate where the contents from 
the `assignment_test_suite.py` file are injected. 

- **26-Jan-2020 Jesse Lawson** 

Pytest isn't very condusive to test feedback for students, so I started creating 
a special testrunner for teaching. I'd like to eventually have something like 
Rust's borrow checker. 

Future: MVP is promising, so I am decoupling student data into a data from the program 
and creating a Submission class, and integrating sqlite to store results. This 
will prep the web interface system that may come next, depending on how this 
next milestone goes. 

- **13-Jan-2020 Jesse Lawson**

I thought I could have a footer and test suite that is automatically appended 
to test files, but instead what I need to do is just 1) read the contents of 
the submission file into memory, 2) create a copy of the submission file 
that ends with _test, 3) push all original contents in there, then 4) 
push the test suite file into the bottom of the new test file. 

So get rid of assignment_footer.py nonsense, and rework the algorithm to 
push the contents of the original submission into a new _test file. 
		
Also look into @pytest.mark.parametrize to test a student's functions 

also lets forget about repl and just upload a copy of the assignment for the student in canvas