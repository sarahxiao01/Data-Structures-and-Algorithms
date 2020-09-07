##1
##a 
## in-place; circular reorder to the left, don't create new list
def shift (lst, k):
	count = k 
	while (count != 0):
		lst.append(lst.pop(0))
		count -= 1
	return lst


##b 
## shift either to left or right, 3 parameters
## use default parameters; default to left
def shift(lst, k, direction = "left"):
	if direction == "right": 
		count = len(lst) - k
	elif direction == "left":
		count = k 
	else:
		raise ValueError("invalid direction")
	while (count != 0):
		lst.append(lst.pop(0))
		count -= 1
	return lst
		
# lst = [1, 2, 3, 4, 5, 6] 
# print(shift(lst, 2, "right"))
# # [3, 4, 5, 6, 1, 2]