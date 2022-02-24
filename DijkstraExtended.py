import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
        

	def printSolution(self, dist):
		print("Vertex tDistance from Source")
		for node in range(self.V):
			print("Node:",node, ",", "Minimum Distance:",dist[node])
    
	
	def minDistance(self, dist, sptSet):

		
		min = sys.maxsize

		
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	
	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			
			u = self.minDistance(dist, sptSet)

			
			sptSet[u] = True

			
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

pm25 = [37,256,28,140,89,35,150,352,97]
penalty = [0,0,0,0,0,0,0,0,0]

for x in range (len(pm25)):
     if pm25[x] <= 35:
         penalty[x] = 0
     elif pm25[x] > 35 and pm25[x] <= 75:
        penalty[x] = 1
     elif pm25[x] > 75 and pm25[x] <= 115:
        penalty[x] = 2
     elif pm25[x] > 115 and pm25[x] <= 150:
        penalty[x] = 3
     elif pm25[x] > 150 and pm25[x] <= 250:
        penalty[x] = 4
     elif pm25[x] > 250 and pm25[x] <= 350:
        penalty[x] = 5    
     else:
        penalty[x] = 6
        

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

for i in range (len(g.graph)):
    for j in range (len (g.graph)):
        if (i != j) and (g.graph[i][j]!=0):
            g.graph[i][j] = g.graph[i][j] + penalty[j]         
            
g.dijkstra(0)

