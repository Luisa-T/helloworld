# Luisa Timothy 25-02-2018
# project Euler problem 1

sum = 0
i = 1

while i < 1000:
  if i % 3 == 0: # if the number is divisible exactly by 3
    sum = sum + i
  elif i % 5 == 0: # if the number is divisible exactly by 5
    sum = sum + i
  i = i + 1

print("Sum of multiples of 3 and 5, less than 1000", sum)