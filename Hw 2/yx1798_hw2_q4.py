#4
def split_by_sign(lst, low, high):
	if low == high:
		newlst = []
		newlst.append(lst[low])
		return newlst
	else:
		sortedlst = split_by_sign(lst, low+1, high)
		if lst[low] > 0:
			sortedlst.append(lst[low]) ##APPEND DOESNT RETURN ANYTHING!!!
		else: 
			sortedlst.insert(0,lst[low])
	return sortedlst

# print(split_by_sign([-1, 5, 15, 20, -33, -57, -9, 1, 2], 0, 8))