import random

class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos): #TODO: test default arguments
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=140, y=140)
        debug_vertex_3 = Vertex('t3', x=40, y=400)
        debug_vertex_4 = Vertex('t4', x=100, y=300)
        
        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_3)
        debug_vertex_2.edges.append(debug_edge_2)

        debug_edge_3 = Edge(debug_vertex_1)
        debug_vertex_3.edges.append(debug_edge_3)



        self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3])

    def bfs(self, start):
        print("called BFS")
        random_color = "#"+"".join([random.choice('01234556789ABCDEF') for j in range(6)])
        queue = []
        found = []

        queue.append(start)
        found.append(start)
        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
                queue.pop(0) 
        return found

    def get_connected_components(self):
        searched = []
        for vertex in self.vertexes:
            if vertex not in searched:
               searched = (self.bfs(vertex))