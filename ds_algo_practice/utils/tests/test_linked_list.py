from ds_algo_practice.utils.linked_list import LinkedList

class TestLinkedList:

	def test_create_linked_list(self):
		sample_ll = LinkedList()
		sample_ll.add_node("A")
		sample_ll.add_node("B")
		sample_ll.add_node("C")
		sample_ll.add_node("Z")

		assert sample_ll.to_list() == ["A", "B", "C", "Z"]

	def test_delete_linked_list(self):
		sample_ll = LinkedList()
		sample_ll.add_node("A")
		sample_ll.add_node("B")
		sample_ll.add_node("C")
		sample_ll.add_node("Z")
		sample_ll.delete_node(index=1)

		assert sample_ll.to_list() == ["A", "C", "Z"]

	def test_add_at_pos(self):
		pass

	def test_delete_at_pos(self):
		pass

	def test_empty_ll_add_at_pos(self):
		pass

	def test_empty_ll_delete_at_pos(self):
		pass

	def test_repr(self):
		pass

	def test_length(self):
		pass
