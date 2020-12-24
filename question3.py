'''Question 4:Write a python function to the number of maximum consecutive  one’s present in the array. '''
def get_max_consecutive(arr, n): 

	# intitialize count 
	count = 0
	
	# initialize max 
	result = 0

	for i in range(0, n): 
	
		# Reset count when 0 is found 
		if (arr[i] == 0): 
			count = 0

		# If 1 is found, increment count and update result. 
		else: 
			
			count+= 1
			result = max(result, count) 
		
	return result 

arr = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1] 
n = len(arr) 

print(f"output for the above array would be: {get_max_consecutive(arr, n)}") 


