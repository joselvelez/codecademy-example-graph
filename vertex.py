class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        print("Adding edge to {vertex}".format(vertex=self.value))
        # A key in the Vertex instance’s edges dictionary represents a connection to that other vertex.
        # For now, we can just set the value to be True.
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())

''' Testing / Debug '''
# grand_central = Vertex('Grand Central Station')
# forty_second_street = Vertex('42nd Street Station')
# print(grand_central.get_edges())
# grand_central.add_edge(forty_second_street.value)
# print(grand_central.get_edges())