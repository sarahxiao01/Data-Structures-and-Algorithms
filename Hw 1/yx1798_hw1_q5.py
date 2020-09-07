##5 
class Vector:
	def __init__(self, d): 
		self.coords = [0]*d 
	def __len__(self): 
		return len(self.coords) 
	def __getitem__(self, j):
		return self.coords[j] 
	def __setitem__(self, j, val): 
		self.coords[j] = val 
	def __add__(self, other): 
		if (len(self) != len(other)):
			raise ValueError("dimensions must agree")
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result
	def __eq__(self, other): 
		return self.coords == other.coords
	def __ne__(self, other): 
		return not (self == other)
	def __str__(self): 
		return '<'+ str(self.coords)[1:−1] + '>'
	def __repr__(self):  
		return str(self)

##a
##input single integer: produces vector of that dimension with all zeros; input sequence of numbers, produces a vector with coordinates based on that sequence
##use run-time type checking (the isinstance function) to support both syntaxes.
	def __init__(self, d): 
		var = isinstance(d, int)
		if var: 
			self.coords = [0]*d 
		else: 
			##list comprehension?
			self.coords = []
			for i in range(len(d)):
				self.coords.append(d[i]) ##?

	##b
	def __sub__(self, other): 
		if (len(self) != len(other)):
			raise ValueError(”dimensions must agree”)
		result = Vector(len(self)) 
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		# have to use coords if no getters and setters
		return result
	##c
	def __neg__(self): 
		result = Vector(len(self)) 
		for i in range(len(self)):
			result[i] = -self[i]
		return result

	##d
	def __mul__(self, num): 
		result = Vector(len(self)) 
		for i in range(len(self)):
			result[i] = self[i] * num
		return result

	##e ## not sure???
	def __rmul__(nom, self): 
		result = Vector(len(self)) 
		for i in range(len(self)):
			result[i] = self[i] * nom
		return result

	##f
	##both dot product and scalar product supported (a number or another vector)
	def __mul__(self, input): 
		var = isinstance(input, int)
		if var: ## == true?
			result = Vector(len(self)) 
			for i in range(len(self)):
				result[i] = self[i] * num
			return result
		else if len(input) != len(self):
			raise ValueError(”dimensions must agree”)
		else:
			result = 0 
			for i in range(len(self)):
				result += self.coords[i] * input.coords[i]
			return result 

##test code

# v1 = Vector(5) 
# v1[1] = 10 
# v1[−1] = 10 
# print(v1)
# <0, 10, 0, 0, 10>
# v2 = Vector([2, 4, 6, 8, 10]) 
# print(v2)
# <2, 4, 6, 8, 10>
# u1 = v1 + v2 
# print(u1)
# <2, 14, 6, 8, 20> 
# u2 = -v2
# print(u2)
# <-2, -4, -6, -8, -10>
# u3 = 3 * v2
# print(u3)
# <6, 12, 18, 24, 30>
# u4 = v2 * 3
# print(u4)
# <6, 12, 18, 24, 30> 
# u5 = v1 * v2 
# print(u5)
# 140
