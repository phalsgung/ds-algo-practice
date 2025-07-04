def fun1():
	str1 = 'GeeksforGeeks'
	 
	# lambda returns a function object
	rev_upper = lambda string: string.lower()[::2]

	print(rev_upper)
	print(rev_upper(str1))


def fun2():
	# Python 3 code to people above 18 yrs
	ages = [13, 90, 17, 59, 21, 60, 5]
	 
	adults = list(filter(lambda age: age > 18, ages))
	 
	print(adults)


if __name__=="__main__":
	fun2()