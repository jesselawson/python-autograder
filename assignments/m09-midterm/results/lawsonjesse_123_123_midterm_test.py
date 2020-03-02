import pytest
import sys
"""
Module 08: "Mid-Term"

OVERVIEW
================================================================================

This file contains ten programming problems that involve writing functions 
from scratch.

Remember that you have to copy and paste this assignment into a file on your
local machine, save that file as "midterm.py", then upload that file 
to the Canvas assignment. 

DIRECTIONS
================================================================================

Each of the ten problems you are expected to finish have specifications ("specs")
inside a code block, followed by a placeholder block of code where I want you 
to write the function that satisfies the specs. 

Follow the directions, paying close attention to what is being asked, the 
logical conditions, and the expected outcomes. Each Problem requires you to 
write a separate function specific to that problem. 

I have provided an example called "Problem 0".

When you are finished, upload the complete file on the Canvas assignment page.

"""

"""
Problem 0

Write a function called `say_hello`.
It should take one string argument: `name`.
It should return a string containing:
    "Hello " + `name` + " and hello world!"
"""

def say_hello(name):
    return f"Hello {name} and hello world!"

"""
Problem 1

Modify the function `get_server_details`.
It should take no arguments.
It should use a for-loop with an iterator to iterate over `server_ips`.

It should return a list where each element is a string equal to 
    the server IP followed by the server name in parentheses.
    Example1: "192.168.0.1 (App Server)"
    Example2: If x is the iterator, f"{server_ips[x]} ({server_name[x]})"

It should satisfy these tests:

details = get_server_details()

"""

server_ips = ["192.168.0.1", "192.168.11.6", "192.168.12.5", "192.168.45.0"]
server_names = ["App Server", "Database 1", "Database 2", "Node Balancer"]

def get_server_details():
    output = []
    for i, ip in enumerate(server_ips):
        str = f"{ip} ({server_names[i]})"
        output.append(str)
    return output


"""
Problem 2

OVERVIEW
================================================================================
A network administrator has given you a list of login activity for a server 
that holds classified information. You are tasked with collecting all failed 
logins from that list. 

INSTRUCTIONS
================================================================================

Modify the function `get_failed_logins`.

It should iterate over the `log_activity` list and check whether each 
   element contains the string "login_failed". 

   Any element that contains the string "login_failed" should be appended 
   to the locally declared list `output`.

It should return a list (e.g., the `output` list) that contains only those 
   elements of `log_activity` that contain the string "login_failed".

"""

log_activity = [
    '20200106|login_failed|fdf79s8d987d8fd87',
    '20200106|login_failed|a0a0a9d8dd7d6d556',
    '20200107|login_success|nbjfnfnj33k3h22kj',
    '20200107|login_failed|fkjehn4i4n5o4i4j4',
    '20200108|login_failed|cx89xc8xc98cx9c80',
    '20200109|login_success|3n3lkjn3lj3nj3333',
    '20200110|login_failed|d09s09d0sd90sd90d',
    '20200110|login_success|f8d7f8d7f98s78eey',
    '20200111|login_failed|45kjl45kj3l4kj5k4',
    '20200111|login_failed|wernelkrnr8f79879',
    '20200112|login_success|f345da4isdfdfasd',
    '20200112|login_success|f345da4i5g4545hh',
    '20200112|login_success|df897df78h3j3hnj',
    '20200113|login_failed|cv89d7f984h4k4kjh',
    '20200113|login_failed|fdffasrt434534tgf']

def get_failed_logins():
    output = []
    for line in log_activity:
        if 'login_failed' in line:
            output.append(line)
    return output


"""
Problem 3

OVERVIEW
================================================================================

Systems administrators routinely have to audit servers and network 
configurations for security purposes. 

You are a programmer assigned to a network team. Your systems administrators 
have asked you to write a function that will quickly give them the name of the 
service that lives on a particular port.

You'll be crafting a function called `get_service_on_port`. It will take one 
argument, a four-digit port number.

When they do this:

`print(get_service_on_port(3000))`

They want the following string returned:

"Service (local dev server) lives on port 3000."

To build this, you'll first want to become comfortable with how the data is 
organized. Each element in the list of services and ports have the following 
format:

":<PORT>:<SERVICE_NAME>"

<PORT> is always four digits long. Never more, never less. 

<SERVICE_NAME> can be any length, and is always a string containing the name 
of the service that lives on the port <PORT>.

The port number is completely unique; there will never be two services running 
on the same port. 

HINT
================================================================================
Use string slices to extract specific parts of the string. 

In the below example:

test = ":3000:local dev server"

The following are true:

* test[1:5] is equal to "3000"
* test[6:] is equal to "local dev server"

Interactive example: https://repl.it/@professorlawson/m08-midterm-example1

You WILL want to use string slices, and not just "<x> in <y>" because there are 
some services that have four-digit numbers in their names that may or may not 
also happen to be equal to the port numbers of different services. In other 
words, don't do this:

port = 3000
for service in service_port_list:
    if port in service:
        # This will give you false positives!

And instead, check if port is equal to service[1:5]. 

Don't forget that port will be an integer, so before you can compare its value 
to a string slice, you need to do a type conversion:

port = 3000
test = ":3000:local dev server"

if test[1:5] == port:
    print("This will never work because test[1:5] is a string and port is an integer.")

if test[1:5] == str(port):
    print("This will work because str(port) forces port to behave like a string.")


INSTRUCTIONS
================================================================================

Modify the function `get_service_on_port`.
It should take one argument: `port`.
If `service_port_list` has an element that contains `port` in the position [1:5],
    It should return a string in the following format:
        f"Service ({name}) is listening on port {port}."
Otherwise, it should return a string in the following format:
        f"No service listening on port {port}."
In each of the above returned strings, {name} is the <SERVICE_NAME> and 
    port is the <PORT>. See the Overview section for details about these fields.


Examples of expected return values:

* get_service_on_port(3000) should return:
    "Service (local dev server) is listening on port 3000."
* get_service_on_port(2500) should return:
    "Service (SMTP) is listening on port 2500."
* get_service_on_port(9999) should return:
    "No service is listening on port 9999."

You will be marked down if you fail to include:
* The period at the end of the strings
* The parentheses in the appropriate places
* All the words in the correct places

Look over your code and the instructions CAREFULLY.

"""

service_port_list = [
    ":3000:local dev server",
    ":8081:Nginx Reverse Proxy",
    ":2500:SMTP Server ID 030001",
    ":4005:Crash Scanner 3000F13",
    ":6800:Telemetry Collector P278081B",
]

def get_service_on_port(port):
    for s in service_port_list:
        if s[1:5] == str(port):
            return f"Service ({s[6:]}) is listening on port {port}."
    return f"No service is listening on port {port}."



"""
Problem 4

OVERVIEW
================================================================================

Touchlite Photography, Inc. has hired you create a streamlined way of organizing 
photos from folders. Specifically, they want you to write a function that will 
allow them to get a list of all the photos that were taken on a specific day, 
given a master list of all photos taken on any day. 

INSTRUCTIONS
================================================================================

1. Modify function `convert_jpg_to_tif`.
    It should take one argument, "filename".
    It should return `filename` with the last four characters 
       replaced with `.tif`. 
    Example: if `filename` = "something.jpg", it should return "something.tif"

2. Modify the function `get_files_from_day`.
    It should take two arguments, "month" and "day".
    It should return a list containing all elements returned from 
       get_files_from_computer() where the first three characters 
       are equal to the month argument, the next two characters 
       are equal to the day argument, and the extension ".jpg"
       is replaced with ".tif" using the `convert_jpg_to_tif` function.
    
    Example:
        I expect this:
        
        get_files_from_day("jan", "04") 
        
        to return the following list:
        
        [
            'jan04_walkinthepark.tif',
            'jan04_dogsitting.tif'
        ]

Assume the following:
* The month will always be inputted as three lower-case letters.
* The day will always be inputted as two digits.

"""

def get_files_from_computer():
    return [
    'jan04_walkinthepark.jpg',
    'jan04_dogsitting.jpg',
    'jan05_firstkiss.jpg',
    'jan05_wedding1.jpg',
    'jan05_wedding2.jpg',
    'jan05_firstkiss2.jpg',
    'jan05_bridesmaids.jpg',
    'jan05_morebridesmaids.jpg',
    'jan05_groom.jpg',
    'jan06_funny1.jpg',
    'jan06_parkschematics.jpg',
    'jan06_angryparkperson.jpg',
    'jan06_parkpersoninmud.jpg',
    'jan06_parkpersoncrying.jpg',
    'jan06_mehelpingparkperson.jpg',
    'jan06_parkpersonthankingme.jpg',
    'jan06_parkperson2.jpg',
    'jan06_funny2.jpg',
    'jan06_funny3.jpg',
    'feb25_weirdobjectinsky.jpg',
    'feb25_hugemeteorthing.jpg',
    'feb25_ufo1.jpg',
    'feb25_ufo2.jpg',
    'feb25_spaceshiplanding.jpg',
    'feb25_spaceship_exterior1.jpg',
    'feb25_spaceship_exterior2.jpg',
    'feb25_spaceshipdooropening.jpg',
    'feb25_weirdaliendude.jpg',
    'feb25_turnsoutthealientsarefemale.jpg',
    'feb25_carnage1.jpg',
    'feb25_carnage2.jpg',
    'feb25_alienpressconference_cancelingallstudentloans.jpg',
    'feb25_alienpressconference_cancelingearth.jpg',
    'feb25_alienspresentingmewithweirdobject.jpg',
    'feb25_mylastcorporealexistence.jpg',
    'feb25_goodbyecruelworld.jpg'
]

def convert_jpg_to_tif(filename):
    return filename[:-4] + '.tif'

def get_files_from_day(month, day):
    # Return a list of .tif files from month and day
    # Remember: the filenames from the master list have the following format:
    # {month}{day}_{name}{extension}
    #    * `Month` is always THREE characters long and lowercase
    #    * `Day` is always TWO digits long (so we should treat it like a string)
    #    * `Name` is a string of any length
    #    * `Extension` always starts with a dot and is four total characters
    output = []
    for e in get_files_from_computer():
        # print(f"checking {e[:3]}...")
        if e[:3] == month:
            # print(f"> checking {e[3:5]}...")
            if e[3:5] == day:
                output.append(convert_jpg_to_tif(e))
    return output

















"""
(02-Mar-2020 Professor Lawson) Below you will find all the test 
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

"""
Assignment test suite for M08 "Mid-Term"


"""

# Problem 1
problem1_target = "get_server_details()"

# Random to ensure
testsuite_asdf987_server_ips = ["192.168.0.1", "192.168.11.6", "192.168.12.5", "192.168.45.0"]
testsuite_asdf987_server_names = ["App Server", "Database 1", "Database 2", "Node Balancer"]

def test_get_server_details_0():

    details = get_server_details()
    
    # details[0]
    d0 = f"{testsuite_asdf987_server_ips[0]} ({testsuite_asdf987_server_names[0]})"
    try:
        return jel_assert(
                problem1_target, 
                details[0] == d0,
                f"return a list where element 0 == \"{d0}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_server_details_1():

    details = get_server_details()
    
    # details[1]
    d1 = f"{testsuite_asdf987_server_ips[1]} ({testsuite_asdf987_server_names[1]})"
    try:
        return jel_assert(
                problem1_target, 
                details[1] == d1,
                f"return a list where element 1 == \"{d1}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_server_details_2():

    details = get_server_details()
    
    # details[2]
    d2 = f"{testsuite_asdf987_server_ips[2]} ({testsuite_asdf987_server_names[2]})"
    try:
        return jel_assert(
                problem1_target, 
                details[2] == d2,
                f"return a list where element 2 == \"{d2}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_server_details_3():

    details = get_server_details()
    
    # details[3]
    d3 = f"{testsuite_asdf987_server_ips[3]} ({testsuite_asdf987_server_names[3]})"
    try:
        return jel_assert(
                problem1_target, 
                details[3] == d3,
                f"return a list where element 3 == \"{d3}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

# Problem 2
problem2_target = "get_failed_logins()"

def test_get_failed_logins():

    logins = get_failed_logins()
    
    should_be = [
        '20200106|login_failed|fdf79s8d987d8fd87',
        '20200106|login_failed|a0a0a9d8dd7d6d556',
        '20200107|login_failed|fkjehn4i4n5o4i4j4',
        '20200108|login_failed|cx89xc8xc98cx9c80',
        '20200110|login_failed|d09s09d0sd90sd90d',
        '20200111|login_failed|45kjl45kj3l4kj5k4',
        '20200111|login_failed|wernelkrnr8f79879',
        '20200113|login_failed|cv89d7f984h4k4kjh',
        '20200113|login_failed|fdffasrt434534tgf'
    ]
    try:
        return jel_assert(
                problem2_target, 
                logins == should_be,
                f"return a list containing all failed logins"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_sevice_on_port_3000():
    problem3_target = "get_service_on_port(3000)"
    result = get_service_on_port(3000)
    expected_output = "Service (local dev server) is listening on port 3000."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_8081():

    problem3_target = "get_service_on_port(8081)"
    result = get_service_on_port(8081)
    expected_output = "Service (Nginx Reverse Proxy) is listening on port 8081."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_2500():

    problem3_target = "get_service_on_port(2500)"
    result = get_service_on_port(2500)
    expected_output = "Service (SMTP Server ID 030001) is listening on port 2500."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_4005():

    problem3_target = "get_service_on_port(4005)"
    result = get_service_on_port(4005)
    expected_output = "Service (Crash Scanner 3000F13) is listening on port 4005."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)


def test_get_sevice_on_port_6800():

    problem3_target = "get_service_on_port(6800)"
    result = get_service_on_port(6800)
    expected_output = "Service (Telemetry Collector P278081B) is listening on port 6800."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_6800():

    problem3_target = "get_service_on_port(9999)"
    result = get_service_on_port(9999)
    expected_output = "No service is listening on port 9999."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

# PROBLEM 4

def test_convert_jpg_to_tif():
    problem4_target = "convert_jpg_to_tif(\"something.jpg\")"
    result = convert_jpg_to_tif("something.jpg")
    expected_output = "something.tif"
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return the string \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)


def test_get_files_from_day1():
    problem4_target = "get_files_from_day(\"jan\", \"04\")"
    result = get_files_from_day("jan", "04")
    expected_output = [
        'jan04_walkinthepark.tif',
        'jan04_dogsitting.tif'
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_files_from_day2():
    problem4_target = "get_files_from_day(\"jan\", \"05\")"
    result = get_files_from_day("jan", "05")
    expected_output = [
        'jan05_firstkiss.tif',
        'jan05_wedding1.tif',
        'jan05_wedding2.tif',
        'jan05_firstkiss2.tif',
        'jan05_bridesmaids.tif',
        'jan05_morebridesmaids.tif',
        'jan05_groom.tif'
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_files_from_day3():
    problem4_target = "get_files_from_day(\"jan\", \"06\")"
    result = get_files_from_day("jan", "06")
    expected_output = [
        'jan06_funny1.tif',
        'jan06_parkschematics.tif',
        'jan06_angryparkperson.tif',
        'jan06_parkpersoninmud.tif',
        'jan06_parkpersoncrying.tif',
        'jan06_mehelpingparkperson.tif',
        'jan06_parkpersonthankingme.tif',
        'jan06_parkperson2.tif',
        'jan06_funny2.tif',
        'jan06_funny3.tif',
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_files_from_day4():
    problem4_target = "get_files_from_day(\"feb\", \"25\")"
    result = get_files_from_day("feb", "25")
    expected_output = [
        'feb25_weirdobjectinsky.tif',
        'feb25_hugemeteorthing.tif',
        'feb25_ufo1.tif',
        'feb25_ufo2.tif',
        'feb25_spaceshiplanding.tif',
        'feb25_spaceship_exterior1.tif',
        'feb25_spaceship_exterior2.tif',
        'feb25_spaceshipdooropening.tif',
        'feb25_weirdaliendude.tif',
        'feb25_turnsoutthealientsarefemale.tif',
        'feb25_carnage1.tif',
        'feb25_carnage2.tif',
        'feb25_alienpressconference_cancelingallstudentloans.tif',
        'feb25_alienpressconference_cancelingearth.tif',
        'feb25_alienspresentingmewithweirdobject.tif',
        'feb25_mylastcorporealexistence.tif',
        'feb25_goodbyecruelworld.tif'
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

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
    output += "* "
    output += str(r) 
    output += "\n\n"
print(output)
        




"""
TEST RUNNER RESULTS
======================================
Assignment: m08-midterm
Student: lawsonjesse
Compiled: 02-Mar-2020

Here are the results of some automated unit tests:

* Test #1 passed: get_service_on_port(8081) should return a string == "Service (Nginx Reverse Proxy) is listening on port 8081."

* Test #2 passed: get_service_on_port(9999) should return a string == "No service is listening on port 9999."

* Test #3 passed: get_service_on_port(4005) should return a string == "Service (Crash Scanner 3000F13) is listening on port 4005."

* Test #4 passed: get_service_on_port(3000) should return a string == "Service (local dev server) is listening on port 3000."

* Test #5 passed: get_service_on_port(2500) should return a string == "Service (SMTP Server ID 030001) is listening on port 2500."

* Test #6 passed: get_server_details() should return a list where element 3 == "192.168.45.0 (Node Balancer)"

* Test #7 passed: get_server_details() should return a list where element 2 == "192.168.12.5 (Database 2)"

* Test #8 passed: get_server_details() should return a list where element 1 == "192.168.11.6 (Database 1)"

* Test #9 passed: get_server_details() should return a list where element 0 == "192.168.0.1 (App Server)"

* Test #10 passed: get_files_from_day("feb", "25") should return a list containing ['feb25_weirdobjectinsky.tif', 'feb25_hugemeteorthing.tif', 'feb25_ufo1.tif', 'feb25_ufo2.tif', 'feb25_spaceshiplanding.tif', 'feb25_spaceship_exterior1.tif', 'feb25_spaceship_exterior2.tif', 'feb25_spaceshipdooropening.tif', 'feb25_weirdaliendude.tif', 'feb25_turnsoutthealientsarefemale.tif', 'feb25_carnage1.tif', 'feb25_carnage2.tif', 'feb25_alienpressconference_cancelingallstudentloans.tif', 'feb25_alienpressconference_cancelingearth.tif', 'feb25_alienspresentingmewithweirdobject.tif', 'feb25_mylastcorporealexistence.tif', 'feb25_goodbyecruelworld.tif']

* Test #11 passed: get_files_from_day("jan", "06") should return a list containing ['jan06_funny1.tif', 'jan06_parkschematics.tif', 'jan06_angryparkperson.tif', 'jan06_parkpersoninmud.tif', 'jan06_parkpersoncrying.tif', 'jan06_mehelpingparkperson.tif', 'jan06_parkpersonthankingme.tif', 'jan06_parkperson2.tif', 'jan06_funny2.tif', 'jan06_funny3.tif']

* Test #12 passed: get_files_from_day("jan", "05") should return a list containing ['jan05_firstkiss.tif', 'jan05_wedding1.tif', 'jan05_wedding2.tif', 'jan05_firstkiss2.tif', 'jan05_bridesmaids.tif', 'jan05_morebridesmaids.tif', 'jan05_groom.tif']

* Test #13 passed: get_files_from_day("jan", "04") should return a list containing ['jan04_walkinthepark.tif', 'jan04_dogsitting.tif']

* Test #14 passed: get_failed_logins() should return a list containing all failed logins

* Test #15 passed: convert_jpg_to_tif("something.jpg") should return the string "something.tif"



"""
