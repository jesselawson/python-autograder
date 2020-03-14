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

The first thing you will want to do is create a file named `sortphotos.py` and 
put it in the root of the folder you extracted the zip file into. 

For example, if you extracted the zip file into a folder named `m11-virus-samples`, 
you should put `sortphotos.py` here:

```
\m11-virus-samples
    \inbox
        \ (many different JPG files)
    \positive
        \buccal
        \blood
    README.txt
    sortphotos.py <-- This is the root of the folder; put it here
```

FILE FORMAT OF VIRUS SAMPLES
--------------------------------------------------------------------------------

The `inbox` folder contains all the unsorted virus sample files that you will 
be organizing.

Each file adheres to a strict file format: 

    "lab{lab_id}_{type}_{identifier}.jpg"

* `lab_id` is a two-character string consisting of two digits.
* `type` is a string that is either "positive" or "negative"
* `identifier` is a 10-character string consisting of ten digits.



INSTRUCTIONS
================================================================================


1. Update function `get_inbox_samples`.

    For every .jpg file in the `inbox` folder, create a copy of `sample_data_template`
    and populate the `filename`, `type`, and `method` values of the copy as follows:

    1.a. `filename` should be the name of the file (i.e. "lab24_positive_1234598765.jpg")
    1.b. `type` should be either "positive" or "negative", based on whether the 
         `filename` has the word "positive" or "negative" in it
    1.c. `method` should be "buccal" if the identifier starts with an even number (2,4,6,8,0), 
         and "blood" if the identifier starts with an odd number. 

    Each dictionary element should be appended to an array that is ultimately 
    returned by the function.
    
    get_inbox_samples() should return a list of dictionaries, where each 
    dictionary element is a copy of `sample_data_template` with the `filename`, 
    `type`, and `method` values set according to 1.a., 1.b., and 1.c.


    Example:
        # If we only had one file in the `inbox` folder:
        samples = get_inbox_samples()
        print(samples[0])
        # Prints something like "{'filename': './inbox/somefile.jpg', 'type': 'positive', 'method': 'buccal'}"
        
    Hint:   
        The position of the `p` in positive and `n` in negative is the same in any 
        sample, so you can just check whether the 6th character is 'n' or 'p'.
        The same is true for the first digit character of the identifier.
          
            lab06_positive_1183744839.jpg
            lab06_negative_1451916068.jpg
                  ^        ^
                  |        |
                  [6:7]    [15:16]


2. Update function `process_samples`.
    It should take one argument: `samples_list`, a list of dictionaries that are all 
        based on `sample_data_template`.
    For each element in `samples_list`:
        If `type` is "negative", move the file `filename` to the /negative folder.
        If `type` is "positive":
            If the method is "buccal", move file `filename` to the /positive/buccal folder.
            If the method is "blood", move the file `filename` to the /positive/blood folder.
    
    Hint: This function will be tested by passing `get_inbox_samples()` into it. 
    Hint: Use shutil.move() to move files.

3. Locate the section at the bottom of this file called "THINKING ABOUT REFACTORING." 
   Provide a written answer to the question.

4. Ensure there are no errors when you execute your script. Additionally, you can 
   verify that your script is working correctly by counting the sample files in 
   each folder. There are 100 negative, 53 positive blood, and 39 positive buccal 
   samples. 

5. Upload this file to the appropriate assignment in Canvas. 

TIPS
================================================================================


"""
import copy
import os
import shutil

positive_samples = []
negative_samples = []

sample_data_template = {
    "filename": None,
    "type": None,
    "method": None,
}






"""
THINKING ABOUT REFACTORING

In the space below, describe how and where we could use recursion to refactor this 
assignment. You do not need to include any code, but pseudocode is fine if you 
want to include that. Your answer should be at least a paragraph (i.e. at least 
three complete, non-trivial sentences).
--------------------------------------------------------------------------------
Your answer: 





--------------------------------------------------------------------------------
"""
