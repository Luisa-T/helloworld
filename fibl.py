# Luisa Timothy 24-02-2018
# A program that displays Fibonacci numbers using people's names.

def fib(n): # line 4-8 define the variables used in the program
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0: # as long as n is bigger or equal to 0 then 11 and 12
    i, j = j, i + j
    n = n - 1
  
  return i # as long as the above applies then i is returned

name = "Timothy" #equals the name
first = name[0] #returns the first integer
last = name[-1] #returns the second integer string
firstno = ord(first) # definition for the ord() function Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string. https://www.geeksforgeeks.org/ord-function-python/
lastno = ord(last)
x = firstno + lastno

ans = fib(x) # returns the resulting fib no
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)