#2
def list_min(lst, low, high):
	mini = lst[low]
	if low == high:
		return lst[low]
	else: 
		minisum = list_min(lst, low+1, high)
		if mini < minisum:
			minisum = mini
		return minisum

# print(list_min([2,3,4,10], 1, 3))