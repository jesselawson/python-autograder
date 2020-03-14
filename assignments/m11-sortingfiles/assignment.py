"""
M11 Assignment: "Sorting Files"

Repl.it Link: 



OVERVIEW
================================================================================

You are a member of a Rapid Technology Response Team (RT2) at the Centers for 
Disease Control and Prevention, tasked with coming up with an automation 
solution for organizing COVID-19 samples from frontline labs. 

You must download the following zip file and extract it for this assignment:
https://coastdistrict.instructure.com/files/5913281/download

Inside that zip file is a file named "README.txt" which contains some background 
information and details about what you are doing and why. 

In this assignment, you'll be writing code that reads in files from a 
specific directory, categorizes those files into dictionaries, then moves 
those files into appropriate folders based on some rules. 

ORGANIZATION AND SETUP
--------------------------------------------------------------------------------

The zip file "m11-virus-samples.zip" that you must extract to your filesystem 
in order to complete this assignment contains the following:

```
m11-virus-samples.zip
    \inbox
        \ (many different JPG files)
    \positive
        \buccal
        \blood
    README.txt
```

The first thing you will want to do is create a file named `process.py` and 
put it in the root of the folder you extracted the zip file into. 

For example, if you extracted the zip file into a folder named `m11-virus-samples`, 
you should put `process.py` here:

```
\m11-virus-samples
    \inbox
        \ (many different JPG files)
    \positive
        \buccal
        \blood
    README.txt
    process.py <-- This is the root of the folder; put it here
```

FILE FORMAT OF VIRUS SAMPLES
--------------------------------------------------------------------------------

The `inbox` folder contains all the unsorted virus sample files that you will 
be organizing.

Each file adheres to a strict file format: "lab{lab_id}_{type}_{identifier}.jpg"

* `lab_id` is a two-character string consisting of two digits.
* `type` is a string that is either "positive" or "negative"
* `identifier` is a 10-character string consisting of ten digits.

REFERENCES
================================================================================



INSTRUCTIONS
================================================================================


TIPS
================================================================================


"""
import copy
import os

positive_samples = []
negative_samples = []

sample_data_template = {
    "filename": None,
    "type": None,
    "method": None,
}

