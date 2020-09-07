def split_by_sign(lst, low, high):
	if low == high: 
		return [lst[low]]
	else: 
		res = split_by_sign(lst, low+1, high)
		print(res)
		res.append(lst[low]) 
		if lst[low] < 0:
			res[0], res[-1] = res[-1], res[0]
		if res[0] < 0:
			res[0], res[-2] = res[-2], res[0]
		print(res)
	return res
	
mylst = [-1, 1, 2, 3, -7, 5, 4]
print(split_by_sign(mylst, 0, 6))