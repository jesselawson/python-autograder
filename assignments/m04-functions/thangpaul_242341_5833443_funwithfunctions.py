def compare_string(str1,str2):
    str1 = 200
    str2 = 100
    if str1 == str2:
        return True
    elif str1 != str2:
        return false
def string_append(str1,str2):
    str1 = "Hello beautiful"
    str2 = "World"
    return (str1+str2)
def first_five_letters (s):
    print("I love u, I hate u")
    return s[0:5]
def calculate_shipping_costs(total_packages,total_weight):
    total_weight = [20,60]
    if total_weight < 50: 
        return "total_packages * 12.50"
    elif total_weight > 50: 
        return "total_packages *19.75"
def favorite_color(name):
    if name == ["Jack","Michelle"]:
        return "Blue"
    elif name == "Robert":
        return "Green"
    elif name == "Jesse":
        return "Purple"
    elif name == "Sami":
        return "Seaform"
    else:
        return "Black"
def is_spam(subject):
    if subject == "Greetings, ":
         return "True"
    elif subject == "Re: Fwd: Coups":
        return "True"
    elif subject == "Special Offer!":
        return "True"
    
