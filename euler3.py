# Luisa Timothy 25-02-2018
# Project Euler problem 3 largest prime

m = 600851475143
i = 2

while i * i <= m: # as long as the integer times the integer is smaller or equal to m
  while m % i == 0: # if m modulus i equals exactly 0
    m = m // i  # then m is m divided by i returning an integer not a floating point
  i = i + 1 # i is i plus 1

print("The largest prime of 600851475143 is", m) # prints the largest prime (The largest prime of 600851475143 is 6857)