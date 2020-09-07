# #3
 
# #a
def count_lowercase(s, low, high):
	if low == high:
		c = s[low]
		if c.islower() == True: 
			return 1
		else:
			return 0
	else: ## ELSE LOOP!!!
		sum = count_lowercase(s, low+1, high)
		c = s[low]
		if c.islower() == True: 
			newsum = sum + 1
			return newsum
		else:
			newsum = sum 
			return newsum
#b 
def is_number_of_lowercase_even(s, low, high):
	if low == high:
		c = s[low]
		if c.islower() == True:
			return False
		else: 
			return True
	else:
		mybool = is_number_of_lowercase_even(s, low+1, high)
		c = s[low]
		if mybool == True:
			if c.islower() == True:
				return False
			else: 
				return True
		if mybool == False:
			if c.islower() == False:
				return False
			else: 
				return True

# string = "NYUTandonEngineering"
# print(count_lowercase(string, 0, 19))
# print(is_number_of_lowercase_even(string, 0, 19))