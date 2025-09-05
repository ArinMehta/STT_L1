"""Main module for practicing pylint fixes."""

x=10
y=20

for i in range(x,y):
    print("Count:", i)

def multiply(a,b):
    """Multiply two numbers."""
    result=a*b
    return result

def add(a,b):
    """ Add two numbers."""
    result=a+b
    return result

answer = multiply(x,y)
print("Answer is:", answer)

answer2 = add(x,y)
print("Addition is: ", answer2)

if answer==answer2:
    print("True")

else:
    print("False")

def swap(a,b):
    """ Swap two numbers."""
    return b,a

first = 1
second =2
print("Before Swapping:", first, second)
first, second = swap(first, second)
print("After Swapping:", first, second)

'''  Is this a comment? '''
