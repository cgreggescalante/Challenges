# Minimal Network
import networkx as nx

matrix = [
	[0,	16,	12,	21,	0,	0,	0],
	[16,0,	0,	17,	20,	0,	0],
	[12,0,	0,	28,	0,	31,	0],
	[21,17,	28,	0,	18,	19,	23],
	[0,	20,	0,	18,	0,	0,	11],
	[0,	0,	31,	19,	0,	0,	27],
	[0,	0,	0,	23,	11,	27,	0]
]

# with open("../Resources/network107.txt", "r") as file:
# 	matrix = [list(map(int, line.strip().split(","))) for line in file.readlines()]


def test_connect(edges):
	sets = [set(e) for e in edges]
	l = len(edges)
	while True:
		i = 0
		while i < len(sets):
			j = i+1
			while j < len(sets):
				if not sets[i].isdisjoint(sets[j]):
					sets[i].update(sets.pop(j))
				else:
					j += 1
			i += 1
		if len(sets) == l or len(sets) == 1:
			break
		l = len(sets)
	return len(sets[0]) == len(matrix)


def weight(matrix, edges):
	s = sum(matrix[e[0]][e[1]] for e in edges)
	if s == 11:
		print(edges)
	return s


def recursive(graph, start=0):
	weights = [graph.size(weight="weight")]

	if start < graph.size():
		for s in range(start, graph.size()):
			new_graph = graph.copy()
			new_graph.remove_edge(edges[s][0], edges[s][1])
			if nx.is_connected(new_graph):
				weights.append(recursive(new_graph, s + 1))

	return min(weights)


#
# def recursive(mask=None, start=0):
# 	if mask is None:
# 		mask = [1 for _ in range(len(edges))]
#
# 	weights = [weight(matrix, [edges[i] for i in range(len(mask)) if mask[i]])]
#
# 	if start < len(mask):
# 		for s in range(start, len(mask)):
# 			nm = mask.copy()
# 			nm[s] = 0
# 			if test_connect([edges[i] for i in range(len(nm)) if nm[i]]):
# 				weights.append(recursive(nm, s + 1))
#
# 	return min(weights)


edges = []
for i in range(len(matrix)):
	for j in range(i, len(matrix)):
		if matrix[i][j]:
			edges.append((i, j, matrix[i][j]))


graph = nx.Graph()
graph.add_nodes_from([i for i in range(len(matrix))])
graph.add_weighted_edges_from(edges)

print(graph.size(weight="weight") - recursive(graph))
