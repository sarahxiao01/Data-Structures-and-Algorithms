#5
def flat_list(nested_lst, low, high):
	if low == high:
		newlst = [] ##PUT THIS INSIDE BASE CASE!!!
		if isinstance(nested_lst[low], int) == True:
			newlst.append(nested_lst[low])
		else:
			newlst.extend(flat_list(nested_lst[low], 0, len(nested_lst[low])-1))
	else:  ##LINEAR, Do same thing every time! 
		newlst = flat_list(nested_lst, low, high-1) ##MAINTAIN SEQUENCE
		if isinstance(nested_lst[high], int) == True:
			newlst.append(nested_lst[high])
		else:
			newlst.extend(flat_list(nested_lst[high], 0, len(nested_lst[high])-1))
	return newlst ##RETURN NEWLST FOR EVERY CONDITION

# nested_lst = [[1, 2], 3, [4, [5, 6, [7], 8]]]

# print(flat_list(nested_lst, 0, 2))