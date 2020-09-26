from vertex import Vertex
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        print("Adding {vertex} to the railway Graph"
        .format(vertex=vertex.value))
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        print("Adding edge from {from_v} to {to_v}"
        .format(from_v=from_vertex.value, to_v=to_vertex.value))
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        print("\nSearching for path between {start} and {end}..."
        .format(start=start_vertex, end=end_vertex))
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("\nVisiting {current_v}".format(current_v=current_vertex))
            if current_vertex == end_vertex:
                # return True
                print("\nA connection exists between {start} and {end}! You have reached your destination."
                .format(start=start_vertex, end=end_vertex))
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                print("Start List: {start}".format(start=start))
                print("List of Vertex Connections: {next_vertices}"
                .format(next_vertices=next_vertices))
                start.extend(next_vertices)
        # return False
        print("\nNo connection seems to exist between {start} and {end}."
        .format(start=start_vertex, end=end_vertex))

''' Test / Debut '''
# railway = Graph()
# print(railway.graph_dict)
# grand_central = Vertex("Grand Central Station")
# railway.add_vertex(grand_central)
# print(railway.graph_dict)