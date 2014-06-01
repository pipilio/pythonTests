def VisitChildren(nodeName, path):
	if (nodeName in path):
		#print "cycle detected when trying to add " + nodeName + " to " + str(path)
		return
	if (len(grafo[nodeName])==0):
		print path + [nodeName]
		return
	for node in grafo[nodeName]:
		VisitChildren(node, path + [nodeName])

grafo = {
		"A": ["B", "D", "F"],
		"B": ["C", "D"],
		"C": ["E", "F"],
		"D": ["E", "F"],
		"E": [],
		"F": ["B", "E", "G"],
		"G": ["C"]
		}

VisitChildren("A", [])




