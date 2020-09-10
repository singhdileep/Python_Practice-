def checkPrime(n):
	if n < 2:
		return False
	for i in range(2, round(n**0.5)+1):
		if n % i == 0:
			return False
	else:
		return True
list_of_prime_number = sum([i for i in range(2000000) if  checkPrime(i)])


print (list_of_prime_number)
