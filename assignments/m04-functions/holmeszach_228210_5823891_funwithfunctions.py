#Problem 1
def string_compare(str1, str2):
	if str1 == str2:
		return True
	else:
		return False

print(string_compare("Burgers", "Burgers"))

#Problem 2
def string_append(str1, str2):
	return str1+str2

print(string_append("Hello, ", "World!"))

#Problem 3
def first_five_letters(string):
	return string[:5]

print(first_five_letters("Sauce, Awesome"))

#Problem 4
def calculate_shipping_costs(total_packages, total_weight):
	if total_weight < 50:
		return total_packages*12.50
	elif total_weight >= 50:
		return total_packages*19.75

print(calculate_shipping_costs(10, 40))

#Problem 5
def favorite_color(name):

	if name == "Jack" or name == "Michelle":
		return "Blue"
	elif name == "Robert":
		return "Green"
	elif name == "Jesse":
		return "Purple"
	elif name == "Sami":
		return "Seafoam"
	else:
		return "Black"

print(favorite_color("Jesse"))

#Problem 6
def is_spam(subject):
	if  "Greeting , " in subject or "Re: Fwd: Coupons" in subject or  "Special Offer !" in subject:
		return True
	else:
		return False

print(is_spam("Re: Fwd: Coupons"))
