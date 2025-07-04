if __name__ == "__main__":
	Blocks = [
		{
			"gym": False,
			"school": True,
			"store": False,
		},
		{
			"gym": True,
			"school": False,
			"store": False,
		},
		{
			"gym": True,
			"school": True,
			"store": False,
		},
		{
			"gym": False,
			"school": True,
			"store": False,
		},
		{
			"gym": False,
			"school": True,
			"store": True,
		}
	]

	Reqs = ["gym", "school", "store"]

	BlocksWeight = []

	for BlockIndex in range(0, len(Blocks)):
		BlockWeight = 0
		for Req in Reqs:
			# current Node
			if(Blocks[BlockIndex][Req] == True):
				BlockWeight+=0
				Reqs.remove(Req)
				continue
			
			BlockIndexPrev = BlockIndex
			BlockIndexNext = BlockIndex
			# Previous Nodes
			while(BlockIndexPrev != 0):
				BlockIndexPrev-=1



			# Next Nodes
		
		BlocksWeight.append(BlockWeight)
	# print(BlocksWeight)
