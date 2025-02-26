# sub -
# add +
# multi *
# diviion /

try:
	Num1 = float(input("Enter 1st Num: "))
	Num2 = float(input("Enter 2nd Num: "))

	# print(Num1)

	Operator = input("Enter one of these Operator + - * / : ")

	# print(Operator)

except ValueError:
	print("Please enter valid Number")


if Operator == '+':
	print(Num1 + Num2)
elif Operator == '-':
	print(Num1 - Num2)
elif Operator == '*':
	print(Num1 * Num2)
elif Operator == '/':
	print(Num1 / Num2)
else:
	print("Invalid Operator")





