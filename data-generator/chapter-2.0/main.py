import random
import string

# Very simple csv creation function
def make_csv(filename: str):
	file = open(filename, "wt")
	lines = []

	for i in range(50):
		row = []

		for o in range(5):
			row.append("".join(random.choices(string.ascii_letters, k=5)))
			
		lines.append(", ".join(row) + "\n")
	
	file.writelines(lines)
		

make_csv("test.csv")
