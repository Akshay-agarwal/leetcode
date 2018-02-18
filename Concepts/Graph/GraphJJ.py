
class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbors = list()
        self.color = 'grey'
        self.distance = 999
        self.discover = 0
        self.finish = 0

    def addNeighbor(self, nbr):
        if nbr not in self.neighbors:
            self.neighbors.append((nbr))
            self.neighbors.sort()

from collections import deque
class Graph:
    vertices = {}

    def addVertex(self, vertex):
        newVertex = Vertex(vertex)
        if vertex not in self.vertices:
            self.vertices[vertex] = newVertex
            return True
        return False

    def addEdge(self, f, t, w):
        if f not in self.vertices:
            self.addVertex(f)
        if t not  in self.vertices:
            self.addVertex(t)
        self.vertices[f].addNeighbor(t)
        self.vertices[t].addNeighbor(f)

    def bfs(self, start):
        q = deque()
        startVert = self.vertices[start]
        startVert.color = 'black'
        startVert.distance = 0
        for vertex in startVert.neighbors:
            q.append(vertex)
            self.vertices[vertex].color = 'black'
            self.vertices[vertex].distance = startVert.distance + 1
        startVert.color = 'red'

        while len(q) > 0:
            node = self.vertices[q.popleft()]
            for vertex in node.neighbors:
                if self.vertices[vertex].color == 'grey':
                    q.append(vertex)
                    self.vertices[vertex].color = 'black'
                    if self.vertices[vertex].distance > node.distance + 1:
                        self.vertices[vertex].distance = node.distance + 1
            node.color = 'red'

    def _dfs(self, vertex):
        global time
        vert = self.vertices[vertex]
        vert.color = 'black'
        vert.discover = time
        time += 1
        for v in vert.neighbors:
            if self.vertices[v].color == 'grey':
                self._dfs(v)
        vert.color = 'red'
        vert.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].discover) + "/" + str(self.vertices[key].finish))



g = Graph()
for i in range (ord('A'), ord('F')):
    g.addVertex(chr(i))
g.addEdge('A','B',1)
g.addEdge('A','D',4)
g.addEdge('B','D',6)
g.addEdge('B','C',5)
g.addEdge('C','F',2)
g.addEdge('F','E',7)
g.addEdge('C','E',8)
g.addEdge('D','E',6)
g.addEdge('E','B',2)
g.printGraph()
g.dfs('A')

g.printGraph()

