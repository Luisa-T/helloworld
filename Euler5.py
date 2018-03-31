# Luisa Timothy 24-02-2018
# project Euler Problem 5 https://projecteuler.net/problem=5
# consulted https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution to get the result

def gcd(x,y): return y and gcd(y, x % y) or x # this returns the greatest common divisor
def lcm(x,y): return x * y // gcd(x,y)  # this returns the lowest common multiple
  
n = 1  
for i in range(1, 21): # for i including all numbers between 1 and 21
     n = lcm(n, i)  # n is the lowest common multiple of n and i
print(n) # found this on w3resource.com; tried to solve it myself for an hour and failed miserably, result is 232792560