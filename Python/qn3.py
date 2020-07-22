import math
class Complex:


	def __init__(self, x, y = 0):
		self.x = x
		self.y = y

	def add(self, other):
		x = self.x + other.x  
		y = self.y + other.y
		return Complex(x,y)


	def subtract(self, other):
		x = self.x - other.x  
		y = self.y - other.y
		return Complex(x,y)


	def display(self):
		print(f"{self.x} + {self.y}i")


	def multiplication(self, other):
		x = self.x*other.x - self.y*other.y
		y = self.x*other.y + self.y*other.x
		return Complex(x,y)


	def conjugate(self):
		x = self.x
		y = -1*self.y
		return Complex(x,y)


	def modulus(self):
		return math.sqrt(self.x**2 + self.y**2)


	def inverse(self):
		x = self.x / (self.mod**2)
		y = -self.y / (self.mod**2)
		return Complex(x,y) 