#Esercizio 21
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 3)
height = subtract(1.90, 0.4)
weight = multiply(11, 8)
iq = divide(76, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d." % (age, height, weight, iq)

#a puzzle for extra credit
print "\nHere's a puzzle:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

###finee###
