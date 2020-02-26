b1 =9
b2 =9

def string_compare(n1,n2):
  if n1 == n2 :
#comparison
    return True
  else:
    return False


print(string_compare(b1,b2))





def string_append(Country,Great='Amazing'):
   return'{}, {}' .format(Country,Great)

print (string_append('America', Great = 'Amazing'))



def first_five_letters(string1):
  return string1[0:5]

print(first_five_letters("Amazing"))



def calculate_shipping_costs(total_packages,total_weight):
  if total_weight < 50:
   return total_packages * 12.50
  else:
     return total_packages * 19.75


print(calculate_shipping_costs(5,40))




def favorite_color(name):
    if name == "Jack":
        return "Blue"
    elif name == "Robert":
        return "Green"
    elif name == "Jesse":
        return "Purple"
    elif name == "Seafoam":
        return "Sami"
    else:
        return "Black"

print(f"Jack favorite color is {favorite_color('Jack')}")


print(f"Robert favorite color is {favorite_color('Robert')}")


print(f"Jesse favorite color is {favorite_color('Jesse')}")


print(f"Seafoam favorite color is {favorite_color('Seafoam')}")


print(f"Tony favorite color is {favorite_color('Tony')}")



def is_spam(subject):
  if "Greetings" in subject:
     return True
  elif "Re: Fwd: Coupons" in subject:
      return True
  elif "Special Offer !" in subject:
    return True
  return False

print(is_spam("Greetings Tony"))



