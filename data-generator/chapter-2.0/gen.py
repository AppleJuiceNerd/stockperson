from objects import *
import random
import string

# Combine the list of all letters, lowercase and uppercase, with the list of digits
alphanumeric_chars = string.ascii_letters + string.digits

# Generates a list of Products
def generate_product_list(num: int):
	out = []
	for i in range(num):
		out.append(
			Product(
				random.choices(alphanumeric_chars, k=random.randint(1, 7)),
				random.uniform(0.1, 100000)
			)
		)
	
	return out
