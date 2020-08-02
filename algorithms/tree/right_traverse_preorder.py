class Node:
	def __init__(self, name):
		self.name = name
		self.left_child = None
		self.right_child = None

	def right_traverse_preorder(self):
		self.print_node()
		if self.right_child:
			self.right_child.right_traverse_preorder()
		if self.left_child:
			self.left_child.right_traverse_preorder()

	def print_node(self):
		print('Traversing node {}'.format(self.name))


def build_tree():
	root = Node('E')
	root.left_child = Node('B')
	root.right_child = Node('F')
	root.left_child.left_child = Node('A')
	root.left_child.right_child = Node('D')
	root.left_child.right_child.left_child = Node('C')
	root.right_child.right_child = Node('I')
	root.right_child.right_child.left_child = Node('G')
	root.right_child.right_child.left_child.right_child = Node('H')
	root.right_child.right_child.right_child = Node('J')
	return root

root = build_tree()
root.right_traverse_preorder()
