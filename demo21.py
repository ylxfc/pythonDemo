def add(a, b):
	print "ADDING %d + %d" %(a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" %(a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" %(a, b)
	return a * b

def divide(a, b):
	print "MULTIPLYING %d / %d" %(a, b)
	return a / b

print "let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: %d, height: %d, weight: %d, iq: %d" %(age, height, weight, iq)
print "this is a puzzle!"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print what
