def deep_copy(lst):
	newlst = []
	for i in range(len(lst)):
		if isinstance(lst[i], list) == False:
			newlst.append(lst[i])
			print newlst
		else: 
			newlst.append(deep_copy(lst[i]))
	return newlst
mylst = [[1,2],3,[4,5,6,[7],8]
print(deep_copy(mylst))