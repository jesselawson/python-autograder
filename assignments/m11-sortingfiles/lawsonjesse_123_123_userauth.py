import copy
import os

positive_samples = []
negative_samples = []

sample_data_template = {
    "filename": None,
    "type": None,
    "method": None,
}

"""
Update function `get_inbox_samples`.
1. It should go through each file in the `inbox` folder and process them 
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

#def get_next_file(directory):


    