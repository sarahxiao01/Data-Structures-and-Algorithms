from array_Stack import ArrayStack


def eval_postfix(exp_str):
	str_lst = exp_str.split(" ")
	operators = "+-*/"
	mystack = ArrayStack()
	for item in str_lst: 
		if item not in operators: 
			mystack.push(int(item)) #KEY is to convert to int!!!
		else: 
			arg2 = mystack.pop()
			arg1 = mystack.pop() #ARG2 popped first!!!
			if item == '+':
				res = arg1 + arg2
			elif item == '-':
				res = arg1 - arg2
			elif item == '*':
				res = arg1 * arg2
			else: 
				res = arg1 / arg2
			mystack.push(res)
	return mystack.pop()


# exp_str = "- + * 16 5 * 8 4 20"
# mid_str = "16*5 + 8*4 - 20"
post_str =  "16 5 * 8 4 * + 20 -"
print(eval_postfix(post_str))