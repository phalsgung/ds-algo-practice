filePath = "LinearSearch.py"

with open(filePath, "r") as fileReader:
	LineNumber = 1
	for Line in fileReader:		
		print("LineNumber", LineNumber, end = ": ")
		print(Line, end="")
		LineNumber+=1