"""Main module for practicing pylint fixes."""

X = 10
Y = 20

for i in range(X,Y):
    print("Count:", i)

def multiply(a,b):
    """Multiply two numbers."""
    result=a*b
    return result

def add(a,b):
    """ Add two numbers."""
    result=a+b
    return result

ANSWER = multiply(X,Y)
print("Answer is:", ANSWER)

ANSWER2 = add(X,Y)
print("Addition is: ", ANSWER2)

if ANSWER==ANSWER2:
    print("True")

else:
    print("False")

def swap(a,b):
    """ Swap two numbers."""
    return b,a

FIRST = 1
SECOND =2
print("Before Swapping:", FIRST, SECOND)
FIRST, SECOND = swap(FIRST, SECOND)
print("After Swapping:", FIRST, SECOND)

#Is this a comment?
