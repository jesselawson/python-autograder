DATE: 	One day ago 
TO: 	Rapid Tech Response Team (RT2), Centers for Disease Control and Prevention
FROM: 	RT2 Chief
SUBJ:   Fw: Unsorted Lab Imaging Results

Please take for action immediately. We require a single Python file that will 
organize the files in their respective folders. Here are the details:

* All samples are located in the `inbox` folder. These are unprocessed and should be 
  moved, not copied, to the appropriate folder based on the processing rules below
  
* File format is as follows:
    "lab{lab_id}_{type}_{identifier}.jpg"

    - `lab_id` is a two-character string consisting of two digits.
    - `type` is a string that is either "positive" or "negative"
    - `identifier` is a 10-character string consisting of ten digits.

* Samples coming in have a type that is either "positive" or "negative"
* There are two kinds of samples: buccal swab analyses, which are cheek swab samples, 
  and blood draw analyses.
* All negative samples should be moved to the `negative` folder, and all positive samples 
  should be moved to the `positive` folder. In the positive folder there is a folder for 
  positive buccal samples and positive blood samples.
* If `identifier` starts with an even number (zero is an even number), then it is a 
  buccal sample and should go into the `positive\buccal` folder. 
* If `identifier starts with an odd number, the it is a blood sample and should go into 
  the `positive\blood` folder.
  
We need this Python file ASAP, as lab results are already starting to pour in. The 
cure for COVID-19 is only possible if we can support the front-line scientists. You are 
one of many hands holding the fate of humanity in all this. 

Good luck,

BEVERLY CRUSHER
CDC RT2 Chief

----------------------------------------------------------------------------------------------


DATE: 	Two days ago
TO: 	Rapid Tech Response Team (RT2), Centers for Disease Control and Prevention
FROM: 	Interdepartmental Liaison Office (ILO), Centers for Disease Control and Prevention
SUBJ:   Unsorted Lab Imaging Results

The ILO is requesting immediate assistance with a rapid classification system to 
organize incoming lab results from COVID-19 samples. We have over 1,200 laboratories 
from around the world sending in data. We have included the samples from the first 
day so that you may create an effective automation system. We anticipate 450+ new sample 
results transmitted every hour starting next monday. Please have the automation 
solution delivered no later than Sunday night. 

Very respectfully,

ZEFRAM COCHRANE
CDC ILO Chief
