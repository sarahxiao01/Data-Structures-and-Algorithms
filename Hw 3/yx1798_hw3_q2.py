#2

def deep_copy(lst):
	newlst = []
	for i in range(len(lst)):
		if not isinstance(lst[i], list):
			newlst.append(lst[i])
		else: 
			newlst.append(deep_copy(lst[i]))
	return newlst
# mylst = [[1,2],3,[4,5,6,[7],8]
# print(deep_copy(mylst))