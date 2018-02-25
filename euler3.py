# Luisa Timothy 25-02-2018
# Project Euler problem 3 largest prime

m = 600851475143
i = 2

while i * i <= m:
  while m % i == 0:
    m = m // i 
  i = i + 1

print("The largest prime of 600851475143 is", m)