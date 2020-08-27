
class Node:
	def __init__(self, name, left_child=None, right_child=None):
		self.name = name
		self.left_child = left_child
		self.right_child = right_child

	

	def print_node(self):
		print('Traversing node {}'.format(self.name))

def traverse_inorder(root):
		if root.left_child:
			traverse_inorder(root.left_child)
		root.print_node()
		if root.right_child:
			traverse_inorder(root.right_child)

def traverse_inorder_iterative_with_stack(root):
	stack = []
	current = root

	while current or len(stack) != 0:
		while current:
			stack.append(current)
			current = current.left_child

		node = stack.pop()
		node.print_node()

		current = node.right_child

	

def build_tree():

	root = Node('E', 
		Node('B', 
			Node('A'), 
			Node('D', 
				Node('C'))
			),
		Node('F', 
			None, 
			Node('I', 
				Node('G',
					None,
					Node('H')
					),
				Node('J'))
			)
		)

	return root

root = build_tree()
#traverse_inorder(root)
traverse_inorder_iterative_with_stack(root)