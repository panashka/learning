class Node:
	def __init__(self, name):
		self.name = name
		self.links = []
		self.depends_on = []
		self.num_before_me = 0
		
	def print_node(self):
		print('node {}'.format(self.name))
	
class Link:
	def __init__(self, nodes):
		self.nodes = nodes
		

def topological_ordering(nodes):
	ordered = []
	ready = []
	
	for node in nodes:
		node.num_before_me += len(node.depends_on)
	
	for node in nodes:
		if not node.depends_on:
			ready.append(node)
			
	while ready:
		ready_node = ready.pop()
		ordered.append(ready_node)
		
		for link in ready_node.links:
			link.nodes[1].num_before_me -= 1
			if link.nodes[1].num_before_me == 0:
				ready.append(link.nodes[1])
				
	return ordered
			
# A depends on B depends on C
# D depends on C

nodeA = Node('Do homework')
nodeB = Node('Prepare working place')
nodeD = Node('Get to home')
nodeC = Node('Call friend to ask homework')

nodeA.depends_on = [nodeB, nodeC]
nodeB.depends_on = [nodeD]
nodeC.depends_on = [nodeD]

nodeD.links = [Link([nodeD, nodeC]), Link([nodeD, nodeB])]
nodeB.links = [Link([nodeB, nodeA])]
nodeC.links = [Link([nodeC, nodeA])]

nodes = [nodeA, nodeB, nodeC, nodeD]
ordered = topological_ordering(nodes)

for node in ordered:
	node.print_node()

