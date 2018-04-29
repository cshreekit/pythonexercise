input = 10
n1 = 0  
n2 = 1
count=2 
result = 0; 
if input <= 0:
	print("enter greater then 0")   
elif input == 1:  
   print(n1)  
else:  
   print(n1)  
   print(n2)  
   while count < input:  
       n3 = n1 + n2  
       print(n3)  
       n1 = n2  
       n2 = n3
       if count >= input - 3: 
       		result += n3 
       count += 1
print("Result is:", result)
