import math
import random

# function in integral
def f():
    math.exp(-i*i/2)

# range
a=0
b=4

# values of n to test
N=[20,200,2000,20^10]

for n in N:
    rand=[random.uniform(a,b) for i in range(n)]
    total=0
    for i in rand:
        total+=f(i)
    print(total*(b-a)/n)
