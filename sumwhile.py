# Luisa Timothy 24-02-2018
# sum all even numbers between 1 and 100

sum = 0
i = 0

while i <= 100:
  if i % 2 == 0:
    sum = sum + 1
  i = i + 1

print("the sum of the even numbers from 1 to 100 is", sum)