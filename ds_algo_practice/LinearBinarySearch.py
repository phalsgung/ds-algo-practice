def LinearSearch(list, target):
	isFound = False
	for index, i in enumerate(list):
		if target == i:
			print("Target:", target, "found at:", index)
			isFound = True
			break
		else:
			continue
	
	if not isFound:
		print("Target:", target, "is not Found in", list)

def BinarySearch(list, target):
	isFound = False
	list.sort()
	firstPos = 0
	lastPos = len(list) - 1

	while firstPos <= lastPos:
		midPos = (firstPos+lastPos)//2

		if target == list[midPos]:
			print("Target:", target, "found at:", midPos)
			isFound = True
			break
		elif target <  list[midPos]:
			lastPos = midPos - 1
			midPos = (firstPos+lastPos)//2
		elif target > list[midPos]:
			firstPos = midPos + 1
			midPos = (firstPos+lastPos)//2

	if not isFound:
		print("Target:", target, "is not Found in", list)


if __name__ == '__main__':
	print("Enter Comma Separated List:")
	list = [int(i) for i in input().split(",")]
	# print(list)
	print("Enter Target Value to search for:")
	target = int(input())
	# LinearSearch(list, target)
	BinarySearch(list, target)
