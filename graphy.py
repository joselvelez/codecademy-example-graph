from vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        print("Adding {vertex} to the railway Graph".format(vertex=vertex.value))
        self.graph_dict[vertex.value] = vertex

''' Test / Debut '''
# railway = Graph()
# print(railway.graph_dict)
# grand_central = Vertex("Grand Central Station")
# railway.add_vertex(grand_central)
# print(railway.graph_dict)