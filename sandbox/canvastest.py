import os

from dotenv import load_dotenv
load_dotenv()




# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://coastdistrict.instructure.com/api/v1/courses"
# Canvas API key
API_KEY = os.getenv("CANVAS_API_KEY")

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(69181)

print(course.name)

#assignments = course.get_assignments()
#for assignment in assignments:
    #print(assignment)

assignment = course.get_assignment(851849)

print(assignment)

"""
This should be a web interface. For sure. 

1. Given an assignment by "python begingrading.py 851849"
    a. Get rubric and store in DB
    b. Get all student IDs and their submission IDs and store them in DB
    c. For each student ID in the submission DB where assignment = 851849:
          i. Download the submission
         ii. Run the autograder, which will populate all fields in submission db.
    d. Instruct user to go to web client to verify rubric, provide comments, etc.

When user is finished, all entries' "status" == "ready_to_post" {"pending_verification", "ready_to_post", "posted"}.

User then must run final job, postgrades.py 851849
    a. find all ready_to_post entries in submissions db where assignment == 851849
    b. for each, post to canvas.

"""