import statistics


INPUT_ARR = [3, 3, 6, 3, 9]
K = 2


def getMinimumMoves(price, k):
	moves_req = 0
	latest_med = statistics.median(price)

	if latest_med == k:
		print(moves_req)
		return
	else:
		price = sorted(price)
		if len(price)/2 == 0 :
			# even len
			pass
		else:
			# odd len
			mid_index = int(((len(price) + 1)/2)) - 1
			while latest_med != k:
				if latest_med < k:
					price[mid_index]+=1
				else:
					price[mid_index]-=1
				moves_req+=1
				price = sorted(price)
				print(price)
				latest_med = statistics.median(price)


def main():
	getMinimumMoves(INPUT_ARR, K)

if __name__ == "__main__":
	main()