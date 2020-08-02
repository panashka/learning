class Node:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None
		self.left_thread = None
		self.right_thread = None

	def add_node(self, value):
		if value < self.value:
			if self.left_child:
				self.left_child.add_node(value)
			else:
				node = Node(value)
				node.left_thread = self.left_thread
				node.right_thread = self
				self.left_child = node
				self.left_thread = None
		else:
			if self.right_child:
				self.right_child.add_node(value)
			else:
				node = Node(value)
				node.right_thread = self.right_thread
				node.left_thread = self
				self.right_child = node
				self.right_thread = None

	def print_node(self):
		print('Traversing node {}'.format(self.value))

	def traverse_preorder_with_threads(self):
		node = self
		via_branch = True

		while node:
			if via_branch:
				while node.left_child:
					node = node.left_child

			node.print_node()

			if node.right_child:
				node = node.right_child
				via_branch = True
			else:
				node = node.right_thread
				via_branch = False


	def traverse_postorder_with_threads(self):
		node = self
		via_branch = True

		while node:
			if via_branch:
				while node.right_child:
					node = node.right_child

			node.print_node()

			if node.left_child:
				node = node.left_child
				via_branch = True
			else:
				node = node.left_thread
				via_branch = False


def build_tree():
	root = Node(15)
	root.add_node(12)
	root.add_node(7)
	root.add_node(22)
	root.add_node(45)
	root.add_node(2)
	root.add_node(1)
	root.add_node(5)
	root.add_node(90)
	return root

root = build_tree()
print('\nPreorder traversing:')
root.traverse_preorder_with_threads()

print('\nPostorder traversing:')
root.traverse_postorder_with_threads()


