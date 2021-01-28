#gotta separate the string into pieces of 13 and split that 13 into a products and run a loop.

#then, make a new variable so that the variable is replaced when its product is bigger. when the loop is over, print that variable

x = input("Number = ")

sections = []

for i in range(0, len(x) - 12):
	sections.append(x[i:i+13])
	
print(sections)

highest_product = 0

for j in sections:
	
	temp_product = 1
	
	for k in range(0,13):
		
		temp_product *= int(j[k])
		
	if temp_product > highest_product:
		
		highest_product = temp_product
		print(j)
		
		
print(highest_product)

#ans: 23514624000