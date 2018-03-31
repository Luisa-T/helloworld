# Luisa Timothy 11-03-2018
# exercise week 7 factorial

def factorial(n): # Return the factorial of n, an exact integer >= 0. 

  import math # importing the inbuilt maths function
  result = 1
  factor = 2
  while factor <= n: # while the factor is smaller or equal to the integer
    result *= factor # then calculate result times factor
    factor += 1 # and also the factor is a positive integer at least equal to 1
  return result
print(factorial(10)) # factorial of 5 is 120, of 7 5040 and of 10 3628800