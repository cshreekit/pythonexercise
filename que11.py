i = 0
numList = []
while True: 
	try:
		userInput = input("Give me a number: ")
		if userInput == "quit":
			break
		else:
			value=int(userInput)
			numList.append(value)
	except ValueError:
		print("This is not a number.????????????????")	
print("Result: ")
print("Maximum: ",min(numList))
print("Minimum: ",max(numList))
print("Sum: ",sum(numList))
print("Average: ",float(sum(numList)/len(numList)))

