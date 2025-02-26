MainArr = [20, -7, -3, 9, -4, 6, -9, 10]



if __name__=="__main__" :
	MinSum = float('inf')
	MinSumArr = [0]*len(MainArr) # Memoization Array

	for MainIndex in range(0, len(MainArr)):
		# print("MainArr[MainIndex]: ", MainArr[MainIndex])
		if MainIndex > 0 and MainArr[MainIndex] > (MainArr[MainIndex] + MinSumArr[MainIndex-1]):
			MinSumArr[MainIndex] = MainArr[MainIndex] + MinSumArr[MainIndex-1]
			# print("in IF: MinSumArr[MainIndex]", MinSumArr[MainIndex])
		else :
			MinSumArr[MainIndex] = MainArr[MainIndex]
			# print("in ELSE: MinSumArr[MainIndex]", MinSumArr[MainIndex])

		if MinSum > MinSumArr[MainIndex] :
			MinSum = MinSumArr[MainIndex]

	print(MinSum)