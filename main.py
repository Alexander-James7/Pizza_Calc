MAT = int(0.5) 
TAX = int(1.13)
ADD_COST = int(1.75)

diameter = int(input("What is the diameter of your pizza"))
material = diameter * 0.5
additional = material + 1.75
tax = additional * 1.13
rounded = round(tax)
print("Your Final Price is $"+str(rounded))