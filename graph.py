from vertex import Vertex
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        print("Adding {vertex} to the railway Graph".format(vertex=vertex.value))
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        print("Adding edge from {from_v} to {to_v}".format(from_v=from_vertex.value, to_v=to_vertex.value))
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

''' Test / Debut '''
# railway = Graph()
# print(railway.graph_dict)
# grand_central = Vertex("Grand Central Station")
# railway.add_vertex(grand_central)
# print(railway.graph_dict)