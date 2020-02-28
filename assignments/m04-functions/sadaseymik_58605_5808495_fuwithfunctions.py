#Fun with functions

#Problem 1 - Compare strings
#firstString = input("Make your first statement. ")
#secondString = input("Make your second statement. ")
def string_compare(firstString, secondString):
    if firstString == secondString:
        print("True")
    else:
        print("False")
#string_compare(firstString, secondString)

#Problem 2 - String Append
#firstArgument = input("State your first argument. ")
#secondArgument = input("State your second argument. ")
def string_append(firstArgument, secondArgument):
    print(f"{firstArgument} {secondArgument}")
#string_append(firstArgument, secondArgument)

#Problem 3 - First Five Letters
#yourWord = input("Make a statement and I'll tell you the first five letters: ")
def first_five_letters(yourWord):
  first_five = yourWord[:5]
  print(first_five)
#first_five_letters(yourWord)

#Problem 4 - Calculate Shipping Costs
#total_packages = int(input("Input total packages: "))
#total_weight = int(input("Input total weight: "))
def calculate_shipping_costs(total_packages, total_weight):
    if total_weight < 50:
        shipping_cost = total_packages * float(12.50)
        print(f"The cost of shipping is {shipping_cost}. ")
    elif total_weight >= 50:
        shipping_cost = total_packages * float(19.75)
        print(f"The cost of shipping is {shipping_cost}. ")
#calculate_shipping_costs(total_packages, total_weight)

#Problem 5 - Favorite Color
#name = input("State your name: ")
def favorite_color(name):
    if name == "Jack":
        print("Blue")
    elif name == "Michelle":
        print("Blue")
    elif name == "Robert":
        print("Green")
    elif name == "Jesse":
        print("Purple")
    elif name == "Sami":
        print("Seafoam")
    else:
        print("Black")
#favorite_color(name)

#Problem 6 - Spam Filter
#subject = input("Subject Is: ")
def is_spam(subject):
    if subject == "Greeting , ":
        print("True")
    elif subject == "Re: Fwd: Coupons":
        print("True")
    elif subject == "Special Offer !":
        print("True")
    else:
        print("False")
#is_spam(subject)
