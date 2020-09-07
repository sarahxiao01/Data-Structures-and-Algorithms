# -*- coding: utf-8 -*-

##1

## reverses in-place, theta(n)

def reverse_list (lst):
   """
   : lst type: list[] :
   return type: None
   """
  size = len(lst)
  for i in range(size // 2):
    lst[i] , lst[-i-1] = lst[-i-1], lst[i]

##2 (harder)
## sorted list, positive int with zeroes mixed in, move all zeroes to end while maintainting order of nonzeroes
## in-place, theta(n)
   
def move_zeros(nums):
##  : nums type: list[int] :
## return type: None 
   for i in range (len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
##3

##a
## sorted list with n numbers
## from the range 0 to n, with one of the numbers removed
## no repeat; searches through the list and returns missing number
'''
def find_missing(lst):
   for num in range(len(lst) + 1):
       if num not in lst:
           return num
'''
'''worst-case runtime:
since the list ranges from 0 to n with one number missing, so worst case is that this number is n-1. 
if n-1 is missing, we have to iterate through the list from 0 for n-1 ops to find out about this. n-1 is O(n)
hence worst-case runtime is O(n)'''

##b
##consider edge cases
       
def find_missing(lst):
    for i in range len(lst-1):
        if (lst[i+1] - lst[i]) != 1:
            return lst[i]+1
   """
   : nums type: list[int] (sorted)
   : return type: int
   """
   

##c
## list not sorted; do not reuse a or b 
def find_missing(lst):
   """
   : nums type: list[int] (unsorted)
   : return type: int
   """
   total = (len(lst) * (len(lst)+1)) / 2
   subtotal = 0 
   for i in range(len(lst)):
        subtotal += lst[i]
   result = total - subtotal 
    return result
   
##4
## new Complex created, orginal objects not changed
class Complex:
    def __init__​(self, a, b):
        self.real = a
        self.img = b
##a

    def​ __​add_​_(self, other):
        mysum = Complex()
        mysum.real = self.real + other.real
        mysum.img = self.img + other.img
        return mysum

##b
    
    def​ __​sub_​_(self, other):
        mydiff = Complex()
        mydiff.real = self.real - other.real
        mydiff.img = self.img - other.img
        return mydiff

##c
## Use the FOIL method
    def​ __​mul_​_(self, other):
        product = Complex()
        product.real = self.real * other.real - self.img * other.img
        product.img = self.real * other.img + self.img * other.real
        return product

##d
## convert the Complex object to a str object and display it as output by calling print( ).
    def​ __​repr_​_(self):
        mystr = str(self.real) + " + " + str(self.img) + "i"
        return mystr

##5
class Polynomial:
    ## define a class to represent a polynomial
    ## use a list to represent coefficients. index of each coefficient in the list will be its corresponding power of x
    ## 0x2 is included and that the coefficients in the list are in reversed order

    ##a
    ## constructor​ that takes a list as a parameter, and initiates a polynomial with coefficients as given in the list.
    ## If no list is given at construction, your polynomial should be p(x) = 0. N​ame the list member variable self.data
    ## Note​: You may assume that the last element in the list (coefficient of the highest power) is not 0
    def __init__​(self, data = [0]):
        self.data = data
       
    ##b
    ## take another polynomial object, and create a new polynomial object representing the sum of the two polynomials
    ## simply adding their coefficients, but different polynomials might have different highest powers.
    def __add__​(self, other):
        thesum = Polynomial()
        thesum.data = []
        if len(self.data) >= len(other.data):
            for i in range (len(other.data)):
                thesum.data[i] = self.data[i] + other.data[i]
            for i in range (len(other.data),len(self.data)):
                thesum.data.append(self.data[i])
        else: 
            for i in range (len(self.data)):
                thesum.data[i] = self.data[i] + other.data[i]
            for i in range (len(self.data),len(other.data)):
                thesum.data.append(other.data[i])
        return thesum

    ##c
    ## takes a number and returns the value of the polynomial for that number when evaluated.
    def __call__​(self, num):
        reuslt = 0
        for i in range(len(self.data)):
            result += self.data[i] * (num ** i)
        return result
        ##Optional
    ##d
    ## returns a str representation of a polynomial in format presented above. using caret symbol​ ^
    ## highest power first; use .join()
    def __repr__​(self):
      for i in range(len(self.data)):
        if self.data[i] != 0:
          if i = 0: 
            termstr = str(self.data[i])
          elif i = 1: 
            termstr = str(self.data[i]) + 'x'
          else: 
            termstr = str(self.data[i]) + 'x' + '^' + str(i)
          strings.insert(0, termstr)
       for i in range(len(strings)):
        displaystr = " + ".join(self.strings)
        return displaystr
    ##e
    ## create new polynomial object representing the multiplication of the two polynomials.
    ## multiply all pairs of coefficients from both lists, and group the ones of the same order
    def __mul__​(self, other):
      mydict = {}
      newpo = Polynomial()
      newpo.data = []
      for i in range(len(self.data)):
        for j in range(len(other.data)):
          product = self.data[i]*other.data[j]
          index = i + j 
          mydict[index] = product
      for i in range(len(mydict)):
        newpo.data.append(0)
      for i in range(len(newpo.data)):
        if i in mydict.keys():
          newpo.data.pop(i)
          newpo.data.insert(i, product)
      return newpo

    ##f
    ## mutates the polynomial object to its derivative.
    ## implement the power rule. modification must be in-place,not creating a new list with new values.
    ## derivative rule: multiply coefficient with power 
    ## reduce power by 1: meaning first item is dropped, and others move forward for one place 
    def​ derive(self):
    ## Test code
      self.data.pop(0)
      for i in range(len(self.data)):
        newlst = [self.data[i]*(i+1) for i in range(len(self.data))]
      return newlst

##4 
cplx1 = Complex(5, 2)
print(cplx1) #5 + 2i
cplx2 = Complex(3, 3)
print(cplx2) #3 + 3i
#addition
print(cplx1 + cplx2) #8 + 5i
#subtraction
print(cplx1 - cplx2) #2 - 1i
#multiplication
print(cplx1 * cplx2) #9 + 21i

#original objects remain unchanged 
print(cplx1) #5 + 2i 
print(cplx2) #3 + 3i


##5
#Constructor
poly1 = Polynomial([3, 7, 0, -9, 2]) ​#2x^4 - 9x^3 + 7x + 3
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3]) ​# 3x^6 + 5x^3 + 2
#add operator
poly3=poly1+poly2 ​#3x^6+2x^4-4x^3+7x+5 print(poly3.data) ​#[5, 7, 0, -4, 2, 0, 3]
#call operator
val1 = poly1(1) print(val1) ​#3
val2 = poly2(1)
print(val2) ​#10
val3 = poly3(1)
print(val3)​ #13 (same result of 3 + 10; poly1(1) + poly2(1))


#Optional
## given 2 binary numbers represented as strings. return their sum represented as binary string when called. don't use bin()
​
# def binaryconvert(n):
#   if n > 1:
#     binaryconvert(n//2)
#   yield (n % 2)  ##???Stack

def​ add_binary​(bin_​num1​,​ bin_num2​):
  num1 = 0
  num2 = 0
  for i in range(len(bin_num1)):
    if bin_num[i] == "1":
      num1 += 2**i
    else:
      if bin_num1[i] != "0":
        raise Error("invalid binary number")
  for i in range(len(bin_num2)):
    if bin_num[j] == "1":
      num2 += 2**j
    else:
      if bin_num2[j] != "0":
        raise Error("invalid binary number")
  newnum = num1 + num2
  ## ??? yield?
  newlst = []
  while n >= 1:
    newlst.insert(0, str(newnum % 2))
    n = n // 2 
  newstr = newlst.join()
  return newstr
## ??? append


   """
   bin_num1 ​-​ type​:​ str
   bin_num2 ​-​ type​:​ str
   return​ value ​-​ type​:​ str
   """
## Test code
add_binary(​"11"​, ​"1"​) ​#100