class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
  
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])
  
	def printArr(self, Distance):
		print("Vertex Distance")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, Distance[i]))

	def BellmanFord(self, source):
		Distance = [float("Inf")] * self.V
		Distance[source] = 0
		for _ in range(self.V - 1):
			for u, v, w in self.graph:
				if Distance[u] != float("Inf") and Distance[u] + w < Distance[v]:
						Distance[v] = Distance[u] + w
		for u, v, w in self.graph:
				if Distance[u] != float("Inf") and Distance[u] + w < Distance[v]:
						print("Graph contains negative weight cycle")
						return
		self.printArr(Distance)

g = Graph(6)
graph={'U':0,'V':1,'W':2,'X':3,'Y':4,'Z':5}
g.addEdge(graph['U'], graph['V'], 2)
g.addEdge(graph['U'], graph['W'], 5)
g.addEdge(graph['U'], graph['X'], 3)
g.addEdge(graph['V'], graph['U'], 2)
g.addEdge(graph['V'], graph['X'], 2)
g.addEdge(graph['V'], graph['W'], 3)
g.addEdge(graph['W'], graph['V'], 3)
g.addEdge(graph['W'], graph['U'], 5)
g.addEdge(graph['W'], graph['X'], 3)
g.addEdge(graph['W'], graph['Y'], 1)
g.addEdge(graph['W'], graph['Z'], 5)
g.addEdge(graph['X'], graph['U'], 1)
g.addEdge(graph['X'], graph['V'], 2)
g.addEdge(graph['X'], graph['W'], 3)
g.addEdge(graph['X'], graph['Y'], 1)
g.addEdge(graph['Y'], graph['X'], 1)
g.addEdge(graph['Y'], graph['W'], 1)
g.addEdge(graph['Y'], graph['Z'], 2)
g.addEdge(graph['Z'], graph['W'], 5)
g.addEdge(graph['Z'], graph['Y'], 2)

print('Numbers Represent Alphabets Of Graph')
print(graph)
g.BellmanFord(graph['U'])