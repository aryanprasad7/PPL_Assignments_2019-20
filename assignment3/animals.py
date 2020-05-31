# Animals
# Super class for the animals
class Animal:
	def __init__(self, name, age, weight):
		self.__name = name
		self.__age = age
		self.__weight = weight
		# All are private variables of the class

	def get_name(self):
		return self.__name

	def get_wt(self):
		return self.__weight

	def get_age(self):
		return self.__age

# 1
class Dog(Animal):
	def speak(self):
		print("Speaking...")
		print('Bark')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 2
class Cat(Animal):
	def speak(self):
		print("Speaking...")
		print('Meow')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color
   
# 3 
class Lion(Animal):
	def speak(self):
		print("Speaking...")
		print('Roar')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 4
class Tiger(Animal):
	def speak(self):
		print("Speaking...")
		print('Roar')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 5
class Horse(Animal):
	def speak(self):
		print("Speaking...")
		print('Neigh')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 6
class Donkey(Animal):
	def speak(self):
		print("Speaking...")
		print('Hee-Haw')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 7
class Monkey(Animal):
	def speak(self):
		print("Speaking...")
		print('Whoop...Whoop')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 8
class Snake(Animal):
	def speak(self):
		print("Speaking...")
		print('Hiss')		

# 9
class Cow(Animal):
	def speak(self):
		print("Speaking...")
		print('Moo')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color

# 10
class Wolf(Animal):
	def speak(self):
		print("Speaking...")
		print('Howl')

	def set_properties(self, no_of_legs, eye_color, color):
		self.no_of_legs = no_of_legs
		self.eye_color = eye_color
		self.color = color

	def get_legs(self):
		return self.no_of_legs

	def get_eyecolor(self):
		return self.eye_color

	def get_color(self):
		return self.color


d = Dog('Rocky', 2, 20)
print("Name: " + d.get_name())
print("Age: {}".format(d.get_age()))
print("Weight: {}".format(d.get_wt()))
d.speak()