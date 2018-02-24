# Luisa Timothy 24-02-2018
# project Euler Problem 5 https://projecteuler.net/problem=5

def gcd(x,y): return y and gcd(y, x % y) or x  
def lcm(x,y): return x * y // gcd(x,y)  
  
n = 1  
for i in range(1, 21):  
     n = lcm(n, i)  
print(n) # found this on w3resource.com; tried to solve it myself for an hour and failed miserably, result is 232792560