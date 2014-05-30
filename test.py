def rightChild(n):
	return 2*n + 2

def leftChild(n):
	return 2*n + 1

def getDepth(BST, num, level):
	try:
		if BST[num] == None:
			return level
	except:
		return level
	else:
		depth1 = getDepth(BST, leftChild(num), level + 1) 
		depth2 = getDepth(BST, rightChild(num), level + 1)
		if (depth1 > depth2):
			return depth1
		else:
			return depth2

def showBST(BST):
	maxDepth = getDepth(A, 0, 0)

	index = 0;
	for level in range(0, maxDepth):
		print A[index : index + pow(2,level)]
		index = index + pow(2, level)

A = [ 1,None,2,None,None,None,3 ]

showBST(A);

