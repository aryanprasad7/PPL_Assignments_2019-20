# Exception for length
a = [1, 2, 3]

# IndexError
try:
	print("Second element of list a is = {}".format(a[1]))
	print("Fourth element of list a is = {}".format(a[3]))

except IndexError:
	print("An error occured due to misindexing")

# ZeroDivisionError
try:
	b = 3
	if b < 4:
		c = b / (b - 3)

	print("Value of c = ", c)

except (ZeroDivisionError, NameError):
	print("Error has occured due to denominator being zero")

# To raise an exception
try:
	raise NameError("This error occured because we forced to raise an error")

except NameError:
	print("An exception")
	raise		# To determine whether the exception was raised or not
