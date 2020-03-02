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










