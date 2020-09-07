##4 
## yield first n elements in fibonacci sequence
def fibs(n):
	lst = []
	count = 0
	a = 1
	b = 1
	sum = a + b
	while count < n:
		if count <= 1:
			yield 1
		elif count == 2:
			yield 2
		else:
			a = b
			b = sum 
			sum = a + b
			yield sum
		count += 1
	    

# ##test code 
# for curr in fibs(8):
# 	print(curr)
