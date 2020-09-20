
class Node:
	def __init__(self, name, links):
		self.name = name
		self.links = links
		self.visited = False
		
	def print_node(self):
		print('Traversing node {}'.format(self.name))
		
class Link:
	def __init__(self, cost, to_node):
		self.cost = cost
		self.to_node = to_node
		
def dept_first_traverse(start_node):
	start_node.visited = True
	stack = []
	stack.append(start_node)
	
	while stack:
		node = stack.pop()
		node.print_node()
		
		for link in node.links:
			if not link.to_node.visited:
				link.to_node.visited = True
				stack.append(link.to_node)
				

nodeA = Node('A',
			[
                                Link(10, 
                                        Node('B', [])),
                                Link(5,
                                        Node('C', []))
                        ]
             )
				
print('starting program')
dept_first_traverse(nodeA)
