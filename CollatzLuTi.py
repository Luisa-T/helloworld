# Luisa Timothy 10-02-2018
# Collaz conjecture 

n = 1984

while n !=1: # as long as n is not 1
    if n % 2 == 0: # if n modulus 2 exactly equals 0, meaning if n is an even number, divide by two
        n = n // 2 # then n is n divided by two returning an integer, not a floating point
        print (n) # output result
    else: # if n is not even then multiply by three and add 1
        n = n * 3 + 1 # n is n times 3 plus 1
        print (n) # output result

print ("the final value of n is", n) # final result will always be 1