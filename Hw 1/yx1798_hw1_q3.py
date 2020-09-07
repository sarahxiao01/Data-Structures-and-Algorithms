##3
## array non-empty; majority element always exists 
## array size n, appears more than n/2 times 
def findmajority(lst):
	mydict = {}
	num = 0
	for i in range(len(lst)):
		num = lst[i]
		if lst[i] not in mydict:
			mydict[num] = 1
		else: 
			mydict[num]+= 1
	max = 0
	for number, times in mydict.items():
		if times > max:
			max = times
	for number, times in mydict.items():
		if times == max:
			return number
			
# lst1 = [3, 2, 3]
# lst2 = [2, 2, 1, 1, 1, 2, 2]
# print(findmajority(lst1))
# print(findmajority(lst2))