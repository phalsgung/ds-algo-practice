def isPrime(Num):
	divisibleNumbers = []
	for i in range(1, Num+1):
		if Num%i == 0:
			divisibleNumbers.append(i)
	# print(divisibleNumbers)

	if len(divisibleNumbers) == 2:
		return True
	else:
		return False



for Num in range(1, 51):
	if isPrime(Num):
		print(Num)