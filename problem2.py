from collections import Counter


INPUT_ARR1  = [[7, 8], [52, 80], [34, 84], [57, 64], [74, 78]]


def countNumbers(arr):
	for range_arr in arr:
		total_nums = range_arr[1] - range_arr[0] + 1
		repeat_num = 0
		for num in range(range_arr[0], range_arr[1]):
			num_counter = Counter(str(num))
			if num_counter.most_common(1)[0][1] > 1:
				repeat_num+=1
		print(total_nums - repeat_num)




def main():
	countNumbers(INPUT_ARR1)


if __name__ == "__main__":
	main()