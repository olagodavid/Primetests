
# A user should be able to put a number of choice.
number = input("please enter a number")

# a variable that confirms that a number is prime using a boolean value
is_prime = True

# cheking if a number has more factors apart from one and its self. [2, number**0.5]
for factor in range (2, int(number ** 0.5)):
#to disprove if number is prime;
	if number % factor == 0:
		is_prime = False
#for efficiency because we know a number is not  prime
		break

# forloop to check if prime number is real.

if is_prime = True:
	print "%d is a prime number!" % number
else:
	print "%d is NOT a prime number!" % number



