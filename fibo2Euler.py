# Luisa Timothy 25-02-2018
# Fibonacci even number Project Euler  2

def fib(n):
  """This function returns the nth Fibonacci number."""
x= 1
y = 1
z = 0
result = 0

while z < 4000000:
   z = (x+y)         
   if z%2 == 0:
       result = result + z

   #next iteration

   x = y
   y = z
print("the answer is", result) 