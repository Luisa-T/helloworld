# Luisa Timothy 10-02-2018
# Collaz conjecture 

n = 1984

while n !=1:
    if n % 2 == 0:
        n = n / 2
        print (n)
    else:
        n = n * 3 + 1
        print (n)

print ("the final value of n is", n)