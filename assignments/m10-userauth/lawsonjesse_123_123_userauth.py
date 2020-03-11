import random

# Normally you would get usernames and whatnots from a database, but for the 
# purposes of this assignment, we'll just use a static data structure here:
the_records = [
    {
        "username": "rossbo",
        "password": None
    },
    {
        "username": "picardjl",
        "password": None
    },
    {
        "username": "lawsonje",
        "password": "hunter2"
    }
]

# We'll use these "word salad" lists to generate pseudo-random passwords
word_salad_one = [
    'Happy', 'Excited', 'Depressed', 'Anxious', 'Nervous', 'Smelly'
]

word_salad_two = [
    'Fish', 'Goat', 'Butterfly', 'Elephant', 'Zebra', 'Cat', 'Mouse'
]

# I am compelled by moral duty to remind you that you should NEVER store 
# passwords this way. It is incredibly insecure--but really good for learning!

def update_username(the_records, old_username, new_username):
    # Get the element in records where username == old_username
    for record in the_records:
        
        if record['username'] == old_username:
            record.update({"username": new_username})
            return True
    
    return False

def generate_password_for_user(the_records, the_user):
    for record in the_records:
        if record['username'] == the_user:
            password = random.choice(word_salad_one)
            password += random.choice(word_salad_two)
            # If you don't str() the randint, you'll get this:
            # TypeError: can only concatenate str (not "int") to str
            password += str(random.randint(12345,98765))
            record.update({'password': password})
            return True
    return False
    
