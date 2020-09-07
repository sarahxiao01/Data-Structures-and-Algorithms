#QUESTION 1
'''
the idea for this question is to store all left (opening) parentheses in the stack
if we encounter a right (closing) parentheses, see if the left most (top of the stack) matches the current right
if so, simply remove it from the stack and continue as that pair has been checked
else: return false because we have a mismatch

You also want to check in the event that there is an excess of right parentheses or excess of left parentheses.

#other edge cases aside from a mismatch
If the stack still contains values after you finish traversing the string, that means you have excess left parentheses
ex) "(((" is not balanced
If the stack is empty while your current character is a right parentheses, you have no left parentheses to compare to so that means you have excess right parentheses
ex) ")))"
'''


#1A
def is_balanced(input_str):

    stack = ArrayStack()
    left = "({[" #left parentheses
    right = ")}]" #right parenthese

    for char in input_str:
        if char in right: #right parentheses
            if stack.is_empty(): #stack is empty, no left match --> excess right parentheses
                return False
            
            else:
                top = stack.pop() 
                if left.index(top) != right.index(char): #do they not match?
                    return False #they do not match? then there's a mismatch so return false
        
        else: #left parentheses
            stack.push(char) #just place it on the stack
    
    return stack.is_empty() #if stack is empty, no excess left parentheses --> True. not empty --> False (excess left parentheses)


print("\nTESTING Q3A:")
print(is_balanced("{{([])}}([])")) #will return True
print(is_balanced("{{[(])}}"))     #will return False (non matching)
print(is_balanced("([]{{[]}())}")) #will return False (leftover character)
print(is_balanced("(([]{{[]}})"))  #will return False (leftover character)
print(is_balanced("([]{{[]}()})")) #will return True

#QUESTION 3
'''
the idea is to use the stack to store operators and the left arguments

ex) 

    exp_str is  " - + * 16 5 * 8 4 20" 
    exp_lst = exp.split(" ") → ["-", "+", "*", "16", "5", "*", "8", "4", "20"]
    stack = [-]
    stack = [- +]
    stack = [- + *]
    stack = [- + * 16] since the top of the stack is an op, we don't have enough arguments to calculate
    stack = [- +] char = 5 at this point, so we pop two elements, left arg, and the top and evaluate * 16 5 = 80
    stack = [- + 80] check to see if we need to do more operations, since top is +, we can just push that result into the stack
    stack = [- + 80 *]
    stack = [- + 80 * 8]
    stack = [- + 80] char = 4 at this point, so we pop two elements, left arg, and the top and evaluate 8 * 4 = 16
    stack = [- + 80] before we push 16 in the stack, we check to see if we need to do more operations. 
    stack = [-] since the top is another number, we pop two elements, 80 + 32 = 112
    stack = [-, 112]
    stack = [] char = 20, 112 - 20 = 92
    stack = [92]
    return stack.pop() --> 92

'''
def eval_prefix(exp_str):
    
    operators = "+-/*"
    exp_lst = exp_str.split( )

    stack = ArrayStack()

    for char in exp_lst:
        if char in operators: #is the character an operator?
            stack.push(char) #yes? push it into the stack
        
        if char.isdigit(): #is the character a number?
            arg2 = int(char) #yes? convert it to int

            while not stack.is_empty() and isinstance(stack.top(), int): #Is the stack empty? if not, do we have another number to perform operations on?
                arg1 = stack.pop() #left arg
                op = stack.pop() #operation

                #check what type of operation it is and evaluate. 
                if op == '+':
                    result = arg1 + arg2
                elif op == '-':
                    result = arg1 - arg2
                elif op == '*':
                    result = arg1 * arg2
                elif op == '/':
                    result = arg1 / arg2
                
                arg2 = result
            
        else: #no other argument, this is the first (left arg) so store this int into the stack
                stack.push(arg2)
    
    return stack.pop( ) #top number, based on our program, the remaining value in the stack is always the final evaluted value


print("\nTESTING Q2:")
print(eval_prefix("1134")) #edge case, just num
print(eval_prefix(" - + * 16 5 * 8 4 20" ))
print(eval_prefix("+ * 5 5 / 10 2"))
print(eval_prefix("+ / - 10 2 4 8"))
print(eval_prefix("+ * 6 3 * 8 4"))
print(eval_prefix("- + * 8 2 4 +  3 6"))
print(eval_prefix("+ + + + 1 2 3 4 5 ")) #edge case, all ops in front, all nums in back

