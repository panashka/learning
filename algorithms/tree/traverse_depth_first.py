from collections import deque

class Node:
	def __init__(self, name):
		self.name = name
		self.left_child = None
		self.right_child = None

	def traverse_depth_first(self):
		children = deque()
		children.append(self)

		while children:
			node = children.popleft()
			node.print_node()

			if node.left_child:
				children.append(node.left_child)
			if node.right_child:
				children.append(node.right_child)

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
root.traverse_depth_first()