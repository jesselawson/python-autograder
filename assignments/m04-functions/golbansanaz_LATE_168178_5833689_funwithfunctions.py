#name = input("What is your name? ")
def hello_world(name):
  print(f"Hello {name}, and hello world!")

#str1 = input("What is your nickname? ")
#str2 = input("What is your preferred name? ")
equal = 'true'
not_equal = 'false'
def string_compare(str1, str2):
  if str1 == str2:
    return equal
  else:
    return not_equal


#str3 = input("What is your nickname? ")
#str4 = input("What is your preferred name? ")
def string_append(str3, str4):
  str5 = str3 + str4
  return str5

str6 = input("What is the day of the week? ")
def first_five_letters(str6):
  return str6[0:5]

total_packages = 25
total_weight = 100
int1 = total_packages
int2 = total_weight
def calculate_shipping_costs(int1, int2):
  if int2 < 50:
    product = int1 * 12.50
    return product
  elif int2 >= 50:
    product = int1 * 19.75
    return product

#name = input("Is your name Jack, Michelle, Robert, Jesse, Sami or something else? ")
def favorite_color(name):
  if name == "Jack" or name == "Michelle":
    return 'Blue'
  elif name == "Robert":
    return 'Green'
  elif name == "Jesse":
    return 'Purple'
  elif name == "Sami":
    return 'Seafoam'
  else:
    return 'Black'

#subject = input("Is the subject of the email Greeting ,; Re: Fwd: Coupons; or Special Offer ! ? ")
def is_spam(subject):
  if subject == ("Greeting ,") or ("Re: Fwd: Coupons") or ("Special Offer !"):
    return 'True'  
