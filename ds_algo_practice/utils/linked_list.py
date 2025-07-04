class LinkedListNode:
	def __init__(self, val):
		if val is None:
			raise ValueError("Cannot have None as LinkedList node value")
		self._node_value = val
		self._node_next = None

	@property
	def value(self):
		return self._node_value

	@value.setter
	def value(self, val):
		self._node_value = val

	@property
	def next(self):
		return self._node_next

	@next.setter
	def next(self, val):
		self._node_next = val


class LinkedList:
	def __init__(self):
		self._head = None
		self._length = 0
		# self._tail = None
		# self.value = None

	def __repr__(self):
		ll_str = ""
		for value in self:
			if ll_str != "":
				ll_str+=" -> "
			ll_str+=value

		return f"<LinkedList({self._length}) [{ll_str}]>"

	def __iter__(self):
		curr_node = self._head
		while(curr_node):
			yield curr_node.value
			curr_node=curr_node.next

	def __next__(self):
		ll_str = ""
		curr_node = self._head
		while(curr_node):
			if ll_str != "":
				ll_str+=" -> "
			ll_str+=curr_node.value
			curr_node=curr_node.next
			return ll_str
		raise StopIteration

	def to_list(self):
		ll_list = []
		for value in self:
			ll_list.append(value)
		return ll_list

	def add_node_at_begin(self, value):
		new_node = LinkedListNode(value)
		# empty LL
		if self._head is None:
			self._head = new_node
		else:
			new_node.next = self._head
			self._head = new_node
		# Increment LL length
		self._length += 1

	def add_node(self, value, index=None):
		if index == None:
			# add at end
			self.add_node_at_end(value)
		elif index == 0:
			self.add_node_at_begin(value)
		else:
			# add at index position
			# iterate upto index position
			cur_idx = 0
			cur_node = self._head
			while(cur_node and cur_node.next != None):
				if cur_idx+1 == index:
					# break before reaching index
					break
				cur_node = cur_node.next
				cur_idx+=1

			if cur_idx+1 != index:
				raise Exception("Given Index bigger than LinkedList Length")

			new_node = LinkedListNode(value)
			new_node.next = cur_node.next
			cur_node.next = new_node
			# Increment LL length
			self._length += 1

	def add_node_at_end(self, value):
		# empty LL
		if self._head is None:
			new_node = LinkedListNode(value)
			self._head = new_node
			return

		# iterate to end
		cur_node = self._head
		while(cur_node.next != None):
			cur_node = cur_node.next

		new_node = LinkedListNode(value)
		cur_node.next = new_node
		# Increment LL length
		self._length += 1

	def delete_node_at_begin(self):
		# empty LL
		if self._head is None:
			# nothing to delete
			return
		else:
			self._head = self._head.next
		# Decrement LL length
		self._length -= 1

	def delete_node(self, index=None):
		if index is None:
			index = self._length - 1

		if index > self._length:
			raise Exception("Given Index bigger than LinkedList Length")

		if index == self._length-1 or index == None:
			# delete last node
			self.delete_node_at_end()
		elif index == 0:
			self.delete_node_at_begin()
		else:
			# delete at index position
			# iterate upto index position
			cur_idx = 0
			cur_node = self._head
			while(cur_node and cur_node.next != None):
				if cur_idx+1 == index:
					# break before reaching index
					break
				cur_node = cur_node.next
				cur_idx+=1

			del_node = cur_node.next
			cur_node.next = del_node.next
			# Decrement LL length
			self._length -= 1

	def delete_node_at_end(self):
		# empty LL
		if self._head is None:
			# nothing to do
			return

		# 1 length LL
		if self._head.next is None:
			self._head = None

		# iterate upto end
		cur_node = self._head		
		while(cur_node.next.next != None):
			cur_node = cur_node.next
		cur_node.next = None
		# Decrement LL length
		self._length -= 1

	def get_node_at(self, index):
		pass

	@property
	def length(self):
		return self._length
