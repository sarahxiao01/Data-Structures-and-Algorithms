from array_Stack import ArrayStack

def eval_prefix(exp_str):
	str_lst = exp_str.split(" ")
	operators = "+-*/"
	mystack = ArrayStack()
	count1 = 0
	count2 = 0
	count3 = 0
	for i in range(len(str_lst)):  # for i in range
		if count2 != 0 and count1 != 0:
			arg2 = mystack.pop()
			arg1 = mystack.pop()
			item = mystack.pop()
			if item == '+':
				res = arg1 + arg2
			elif item == '-':
				res = arg1 - arg2
			elif item == '*':
				res = arg1 * arg2
			else: 
				res = arg1 / arg2
			mystack.push(res)
			count1 = 0
			count3 = 1
		if (count1 != 0) and (str_lst[i] not in operators) and (count2 == 0):
			continue
		if (count3 != 0):
			count3 = 0
			continue
		if str_lst[i] in operators: 
			mystack.push(str_lst[i])
			count1 = 0
		else: 
			arg1 = int(str_lst[i]) ##CONVERT to int!!
			if count2 == 0 and count1 == 0:
				arg2 = int(str_lst[i+1])
				count1 += 1
				item = mystack.pop()
				if item == '+':
					res = arg1 + arg2
				elif item == '-':
					res = arg1 - arg2
				elif item == '*':
					res = arg1 * arg2
				else: 
					res = arg1 / arg2
				mystack.push(res)
				if (i+2 <= len(str_lst)-1):
					if str_lst[i+2] not in operators:
						count2 += 1
			else: 
				arg2 = arg1
				arg1 = int(mystack.pop())
				item = mystack.pop()
				if item == '+':
					res = arg1 + arg2
				elif item == '-':
					res = arg1 - arg2
				elif item == '*':
					res = arg1 * arg2
				else: 
					res = arg1 / arg2
				mystack.push(res)
	return res

pre_str = "- + * 16 5 * 8 4 20"
mid_str = "16*5 + 8*4 - 20"
post_str =  "16 5 * 8 4 * + 20 -"
# print(eval_postfix(post_str))
print(eval_prefix(pre_str))