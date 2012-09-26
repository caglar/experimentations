class Node:
	left = None
	right = None
	parent = None
	key = -1
	
def insert(node, x):
	if node is None or x is None:
		return None
	if x.key > node.key:
		if node.right is None:
			node.right = x
			x.parent = node
			return x
		else:
			insert(node.right, x)
	elif x.key < node.key:
		if node.left is None:
			node.left = x
			x.parent = node
		else:
			insert(node.left, x)

def search(node, key):
	if node is None:
		return None
	if node.key > key:
		return search(node.left, key)
	if node.key < key:
		return search(node.right, key)
	if node.key == key:
		return node

LeafCount = 0 

def countLeaves(node):
	if node is None:
		return 0
	if node.left is None and node.right is None:
		return 1
	return countLeaves(node.left) + countLeaves(node.right)

def countInternalNodes(node):
	if node is None:
		return 0
	if node.left is None and node.right is None:
		return 0
	else:
		return 1 + countInternalNodes(node.left) + countInternalNodes(node.right)

LeafCount = 0

def countLeaves2(node, leafCount):
	global LeafCount
	if node is None:
		return 0

	countLeaves2(node.left, leafCount)
	countLeaves2(node.right, leafCount)

	if node.left is None and node.right is None:
		LeafCount += 1

def compute_size(node):
	if node is None:
		return 0
	return 1 + compute_size(node.left) + compute_size(node.right)


if __name__=="__main__":
	root = Node()
	node1 = Node()
	node2 = Node()
	node3 = Node()
	node4 = Node()
	node5 = Node()

	node1.key = 1
	node2.key = 2
	node3.key = 3
	node4.key = 4
	node5.key = 8

	insert(root, node2)
	insert(root, node4)
	insert(root, node3)
	insert(root, node5)
	insert(root, node1)

	print countLeaves(root)
	countLeaves2(root, 0)
	print LeafCount
	print search(root, 2).right.key
	print compute_size(root)
	print "Internal Nodes:", countInternalNodes(root)
