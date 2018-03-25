#Luisa Timothy 19.03.2018
# problem 1

def sumultiply (a, b):
	if a < 0: # if a is smaller than 0 then it is a negative number
		return - sumultiply (-a, b) #the result therefore needs to be a negative integer
	elif a == 0: # if a is 0 
		return 0 # then the result is 0
	elif a == 1: # if a is 1
		return b # the result is b
	else:
		return b + sumultiply (b, a - 1)