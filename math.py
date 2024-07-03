from numpy.random import randint
import numpy as np
from math import gcd # greatest common divisor

a = 2
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print( a%b)

f = int(3)    # f will be 3
q = float(3)  # q will be 3.0
print(f)
print(q)


print(type(a))



n = 10
print(n//3);
print(n%3);



np.random.seed(1) # This is to make sure we get reproduceable results
a = randint(2, 15)
print(a)

#Find the Greatest Common Divisor of the Two Integers
print(gcd(24, 36))



print(10/3)
print(10//3)
print(10%3)

print("======================")
print(max(1,2,3))

