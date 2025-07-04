from ds_algo_practice.utils.linked_list import LinkedList

def main():
	ll1 = LinkedList()
	ll1.add_node_at_begin("A")
	ll1.add_node("B")
	ll1.add_node("C")
	ll1.add_node("D")
	ll1.add_node_at_end("E")
	# ll1.add_node("Z", 4)
	print(ll1)

	# ll1.delete_node_at_end()
	ll1.delete_node(3)
	# ll1.delete_node_at_begin()
	# print(ll1)
	print(ll1.to_list())

if __name__ == '__main__':
	main()
