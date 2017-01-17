
# A user should be able to put a number of choice.
number = input("please enter a number")

# a variable that confirms that a number is prime using a boolean value
is_prime = True

# cheking if a number has more factors apart from one and its self. [2, number-1]
for factor in range (2, number):
#to disprove if number is prime;
	if number % factor == 0:
		is_prime = False

# forloop to check if prime number is real.


