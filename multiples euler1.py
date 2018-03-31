# Luisa Timothy 25-02-2018
# project Euler problem 1 multiples of 3 and 5 below 1000

sum = 0
i = 1

while i < 1000:
  if i % 3 == 0: # number divisible exactly by 3
    sum = sum + i
  elif i % 5 == 0: # number divisible exactly by 5
    sum = sum + i
  i = i + 1 # result is 233168 