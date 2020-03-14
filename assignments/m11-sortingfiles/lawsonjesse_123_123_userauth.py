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
Update function `get_inbox_samples`.
1.  It should go through each file in the `inbox` folder and process them 
    according to the following rules:
    1.a. If 

    It should return a list of dictionaries, where each dictionary element is 
    a copy of `sample_data_template` with the `filename`, `type`, and `method` 
    keys corresponding to each file in `inbox` appropriately. 


    Example:
        # If we only had one file in the `inbox` folder:
        samples = get_inbox_samples()
        print(samples[0])
        # Prints something like "{'filename': './inbox/somefile.jpg', 'type': 'positive', 'method': 'buccal'}"
"""

def get_inbox_samples():
    samples_list = []
    
    for result in os.scandir(os.curdir+"/inbox"):
        if result.is_file():
            # Strip out type and derive method
            the_type = None
            method = None 

            type_target = result.name[6:7]
            method_target = result.name[15:16]

            the_type = "negative" if type_target == 'n' else "positive"
            method = "buccal" if method_target in ['2','4','6','8','0'] else "blood"

            # print(f"{result.name}:\n\tmethod('{method_target}')='{method}';\n\tthe_type('{type_target}')='{the_type}'")

            this_sample = dict(sample_data_template)

            this_sample['filename'] = result.name
            this_sample['type'] = the_type
            this_sample['method'] = method

            samples_list.append(this_sample)
    
    return samples_list


"""
Update function `process_samples`.
It should take one argument: `samples_list`, a list of dictionaries that are all 
   based on `sample_data_template`.
For each element in `samples_list`:
    If `type` is "negative", move the file `filename` to the /negative folder.
    If `type` is "positive":
        If the method is "buccal", move file `filename` to the /positive/buccal folder.
        If the method is "blood", move the file `filename` to the /positive/blood folder.
Hint: This function will be tested by passing `get_inbox_samples()` into it.        
"""

def process_samples(samples_list):
    for e in samples_list:
        if e['type'] == "negative":
            shutil.move("inbox/"+e['filename'], "negative/"+e['filename'])
        else: 
            if e['method'] == "buccal":
                shutil.move("inbox/"+e['filename'], "positive/buccal/"+e['filename'])
            else:
                shutil.move("inbox/"+e['filename'], "positive/blood/"+e['filename'])








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


    