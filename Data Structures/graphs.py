# Adjacency Matrix
class Graph:
    def __init__(self, num_vertices):
        # Initialize a num_vertices x num_vertices matrix with False (no edge)
        self.graph = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]
        
    def add_edge(self, u, v):
        # Ensure u and v are within valid range
        if 0 <= u < len(self.graph) and 0 <= v < len(self.graph):
            # Add an edge by setting the corresponding matrix cell to True
            self.graph[u][v] = True
            # For undirected graph, also set the symmetric cell
            self.graph[v][u] = True
        else:
            raise ValueError("Invalid vertex index")

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph) or v < 0 or v >= len(self.graph):
            return False
        return self.graph[u][v]
    
    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
    
# Adjancey List
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
           self.graph[u].add(v)      
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def adjacent_nodes(self, node):
        return list(self.graph[node])
    
    # Returns vertices(nodes) that have no edges and connect to no nother vertices
    def unconnected_vertices(self):         
        unconnected = []
        for vertex, connections in self.graph.items():
            if not connections:
                unconnected.append(vertex)
        return unconnected

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False