
class Node:
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.links = []
		
	def print_node(self):
		print('Traversing node {}'.format(self.name))
		
class Link:
	def __init__(self, cost, nodes):
		self.cost = cost
		self.nodes = nodes
		
def dept_first_traverse(start_node):
	start_node.visited = True
	stack = []
	stack.append(start_node)
	
	while stack:
		node = stack.pop()
		node.print_node()
		
		for link in node.links:
			if not link.nodes[1].visited:
				link.nodes[1].visited = True
				stack.append(link.nodes[1])
				

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')

linkAB = Link(10, [nodeA, nodeB])
linkBC = Link(5, [nodeB, nodeC])
linkCD = Link(5, [nodeC, nodeD])
linkAD = Link(6, [nodeA, nodeD])

nodeA.links.append(linkAB)
nodeA.links.append(linkAD)
nodeB.links.append(linkBC)
nodeC.links.append(linkCD)
				
dept_first_traverse(nodeA)
