import turtle
from math import pi

# 1
class Rectangle():
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def properties(self):
		print('No. of edges = 4, and the angle between two edges is 90degrees, the opposite edges are of equal length')

	def draw(self):
		turt = turtle.Turtle()
		for i in range(2):
			turt.forward(100)
			turt.right(90)
			turt.forward(70)
			turt.right(90)

		turtle.clearscreen()

	def get_area(self):
		return (self.length * self.breadth)

	def get_perimeter(self):
		return 2 * (self.length + self.breadth)

# 2
class Square():
	def __init__(self, length):
		self.length = length

	def properties(self):
		print("No. of edges = 4, and the angle between two edges is 90degrees, all the edges are of equal length")
		
	def draw(self):
		turt = turtle.Turtle()
		for i in range(4):
			turt.forward(100)
			turt.right(90)
		turtle.clearscreen()

	def get_area(self):
		return (self.length * self.length)

	def get_perimeter:
		return (self.length * 4)


# 3
class Triangle():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def properties(self):
		print("No. of edges = 3, and the angle between two edges varies between 0 and 180degrees(both not included), the edges may or may not be of equal length")

	def draw(self):
		turt = turtle.Turtle()
		for i in range(3):
			turt.forward(100)
			turt.right(120)
		turtle.clearscreen()

	def get_perimeter(self):
		return (self.a + self.b + self.c)

#4
class Pentagon():
	def __init__(self, length):
		self.length = length

	def properties(self):
		print("No. of edges = 5, and the angle between two edges varies between 0 and 180degrees(both not included), the edges may or may not be of equal length")

	def draw(self):
		turt = turtle.Turtle()
		nside = 5
		side_length = 100
		angle = 360.0 / nside

		for i in range(nside):
			turt.forward(side_length)
			turt.right(angle)
		turtle.clearscreen()

#5
class Hexagon():
	def __init__(self, length):
		self.length = length

	def properties(self):
		print("No. of edges = 6, and the angle between two edges varies between 0 and 180degrees(both not included), the edges may or may not be of equal length")

	def draw(self):
		turt = turtle.Turtle()
		nside = 6
		side_length = 100
		angle = 360.0 / nside

		for i in range(nside):
			turt.forward(side_length)
			turt.right(angle)
		turtle.clearscreen()

#6
class Circle():
	def __init__(self, radius):
		self.radius = radius

	def properties(self):
		print("There are no edges in a Circle, along a point with a radius the Circle is plotted")

	def draw(self):
		turt = turtle.Turtle()
		radius = input("Enter the radius of the circle: ")
		turt.circle(radius)
		turtle.clearscreen()

	def get_circumference(self):
		return (2 * pi * self.radius)

	def get_area(self):
		return (pi * (self.radius ** 2))

# 7
class Ellipse():
	def __init__(self, major_axis, minor_axis):
		self.major_axis = major_axis
		self.minor_axis = minor_axis

	def properties(self):
		print("Ellipse has a major and a minor axis, it is like a circle which is pressed on top and bottom")

	def get_area(self):
		return (pi * self.minor_axis * self.major_axis)

	def get_perimeter(self):
		return (2 * pi * (((self.major_axis ** 2) + (self.minor_axis ** 2)) / 2) ** 0.5)

# 8
class Hyperbola():
	def __init__(self, major_axis, minor_axis):
		self.major_axis = major_axis
		self.minor_axis = minor_axis

	def properties(self):
		print("Hyperbola also has a major and minor axis")

	def get_axis(self):
		return (self.major_axis, self.minor_axis)

# 9
class Parallelogram():
	def __init__(self, side = 0, base = 0):
		self.side = side 
		self.base = base

	def properties(self):
		print("Parallelogram has 4 edges, with the opposite edges being parallel to each other and of equal length")

	def get_perimeter(self):
		return (2 * (self.side + self.base))


# 10
class Star():
	def __init__(self):
		pass
	
	def draw(self):
		turt = turtle.Turtle()

		for i in range(5):
			turt.forward(100)
			turt.right(144)

		turtle.clearscreen()



rect = Rectangle()
rect.properties()
rect.draw()

# tr = Triangle()
# tr.properties()
# tr.draw()

# st = Star()
# st.draw()

# hexa = Hexagon()
# hexa.draw()

# pent = Pentagon()
# pent.draw()