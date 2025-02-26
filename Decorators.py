def DecUpper(func):
	
	def WrapperFunc():
		retVal = func()
		return retVal.upper()
	
	return WrapperFunc

def DecLower(func):
	
	def WrapperFunc():
		retVal = func()
		return retVal.lower()
	
	return WrapperFunc


@DecLower
def Greet():
	return "Hello World!"


if __name__ == "__main__":
	print(Greet())
	# print(var)