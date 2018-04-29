import sys
try:
	userInput = input("Give me a number: ")
	value=int(userInput)
	print("{} km/hr".format(value))
	value = (float(value * 1000)/(60*60))
	print("{} m/s".format(value))
	
except ValueError:
	print("This is not a number.????????????????")	
	sys.exit
