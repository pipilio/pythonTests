import math

A = [25,42,33,17,29,54,22,13,35]
HEAP=[None for i in range(0,16)]
parentPosition = 0
positionInA = 0

def swapWithParent(array,child):
	temp = array[getParent(child)]
	array[getParent(child)] = array[child]
	array[child] = temp
	if (getParent(child) > 0 and array[getParent(child)] > array[getParent(getParent(child))]):
		swapWithParent(array,getParent(child))

def getParent(pos):
	return int(math.ceil((pos-1)/2))

def printHeap(heap):
	currentRange = heap[0:1]
	level = 0
	while(not all([x==None for x in currentRange])):
		print currentRange
		level = level + 1
		currentRange = heap[pow(2,level)-1:pow(2,level)-1+pow(2,level)]


for element in A:
	firstFreeSpot = HEAP.index(None)
	HEAP[firstFreeSpot] = element
	if (firstFreeSpot != 0):
		if HEAP[getParent(firstFreeSpot)] < element:
			swapWithParent(HEAP,firstFreeSpot)
	printHeap(HEAP)
	print "----------------------------"


