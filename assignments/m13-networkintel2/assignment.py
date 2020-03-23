"""
M13 Assignment: "Network Intelligence Project, Part II"

Repl.it Link: https://repl.it/@professorlawson/m13-networkintel2



OVERVIEW
================================================================================

The NSA's Basic Overview Operations & Planning (BOOP) division has been 
experiencing a high-volume of suspicious network activity from inside the 
intranet. The NSA's intranet is a closed-off, firewalled internal 
communications network among workstations in and around several buildings in 
Quantico, VA, connecting them to classified servers throughout Virginia and the 
D.C. area. 

SITUATION
--------------------------------------------------------------------------------

You have been brought in to the NSA to help parse through traffic logs of 
one particularly important system to find out which computers on the internal 
net are responsible for the suspicious activity. 


MISSION
--------------------------------------------------------------------------------

Use what you've learned about object-oriented programming in Python to 
construct a log parser that will find IP addresses of workstations on the NSA's
intranet that have "login_failed" comprising > 35% of all activity for that IP.

ARCHITECTURE
--------------------------------------------------------------------------------

At the end of this course we'll have a text file named `traffic_logs.txt` which 
will contain tens of thousands of records of activity in the following format:

<timestamp> <ip> <activity> <url>

Here are some example records:

2570818943688726 192.168.55.94 500_error siprnet-gateway.nsa.gov/reports/std/batch/
2570920833467903 192.168.55.94 500_error elintportal.nsa.gov/cms/account/roles/
25710101036208735 192.168.31.13 login_success humintportal.nsa.gov/cms/builder/
25711134547409388 192.168.31.3 500_error project7.nsa.gov/account/settings/
2571257827258958 192.168.55.84 login_failed dmdnode2.nsa.gov/cms/builder/
25713178541757516 192.168.31.4 post_request elintportal.nsa.gov/adm_groups/reports/

Our system's goal is to go through each of these records and to determine 
which IP addresses are *suspicious*. To determine that, we'll define a sensitivity 
threshold to our log parser in Module 14 which will give our algorithms a point 
at which we can indicate an IP address is suspicious. We will define "suspicious" 
activity as having failed logins comprising more than a percent of total activity--
again, that cut-off being defined as the system's sensitivity. 

The sytem will have two classes:

* IPAddress, which will represent an individual IP address
* LogParser, which will represent the engine that handles all IPAddress objects

We will be constructing this log parsing system over the rest of this course. 

[CURRENTLY] Module 13: We'll build the IPAddress class.
[NEXT WEEK] Module 14: We'll build part of the LogParser class.
[LAST WEEK] Module 15: You'll finish off the LogParser class and get it turned in.

You can see an example of the log file we are going to be parsing by downloading 
a copy from the following link:

https://gist.githubusercontent.com/jesselawson/11cb1a6834973f683c306070d359a4c9/raw/f24ae600f379e10e1b1e8f12f925a3a5a42bfdc3/traffic_logs.txt


TIPS
--------------------------------------------------------------------------------

* Use the class Discord server to work with your classmates through any issues 
or concerns you may have. Your professor will be there also to help guide 
discussions and provide support. 

* Unless specified otherwise, assume member functions take no arguments (i.e., 
  they will take `self` only, as member functions must take `self` as the first 
  parameter). So if the instructions say, for example, to create a member 
  function named `get_name` and does not specify anything about arguments, 
  you will declare it with `def get_name(self)`. 

* If an instruction says to create something that has one parameter, that means 
  it will have two: `self`, and whatever else you have to make. 

* Seriously--don't forget that member functions will all have `self` as the 
  first parameter.


REFERENCES
--------------------------------------------------------------------------------

How to Construct Classes and Define Objects in Python 3:
    https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3

Understanding Class and Instance Variables in Python 3:
    https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3


INSTRUCTIONS
================================================================================

1.  Create a new class named `IPAddress`.

2.  Add a constructor to the IPAddress class that has one parameter: `ip`.

3.  Create a class instance variable named `ip` and, in the constructor, 
    assign to it the value of the constructor's `ip` parameter. 

4.  Create the following additional class instance variables:
    * activity, initialized to an empty list (e.g., `self.activity = []`)
    * activity_url, initialized to an empty list
    * total_activity, initialized to 0
    * failed_logins, initialized to 0
    * suspicious, initialized to False

5.  Create a member function of the IPAddress class called `is_suspicious`.
    It should return the class instance variable `suspicious`.

6.  Create a member function of the IPAddress class called `set_as_suspicious`.
    It should set the class instance variable `suspicious` to True.

7.  Create a member function of the IPAddress class called `get_ip`.
    It should return the class instance variable `ip`.

8.  Create a member function of the IPAddress class called `add_activity`.
    It should take two parameter: `some_activity` and `some_url`.
    It should append `some_activity` to the `activity` class instance variable.
    It should append `some_url` to the `activity_url` class instance variable.
    It should increment the `total_activity` class instance variable by 1.
    It should increment the `failed_logins` class instance variable by 1
        if `some_activity` is "login_failed". 

9.  Create a member function of the IPAddress class called `get_total_activity`.
    It should return the `total_activity` class instance variable.

10. Create a member function of the IPAddress class called `get_failed_logins`.
    It should return the `failed_logins` class instance variable. 

11. Create a member function of the IPAddress class called `get_flar`.
    It should return `get_failed_logins()` divided by `get_total_activity()` 
        rounded to the nearest two decimals.
    Hint: Use the round() function:
        return round(first_func() / second_func(), 2)

12. Ensure your script executes with no errors. 

13. Submit your error-free Python file to the appropriate Canvas assignment. 

"""

class IPAddress:
    #def __init__ ...
        

# You may add as many print() statements as you need and use a main() 
# function for testing all you want, but please remember to remove it or 
# comment it out before submitting. Thank you!