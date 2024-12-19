class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = []

        to_visit.append(v)
        while len(to_visit) != 0:
            first_vertex = to_visit.pop(0)
            visited.append(first_vertex)
            visited_vertex_neighbors = sorted(self.graph[first_vertex])
            for neighbor in visited_vertex_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited
                    
    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result


 # - Expecting: ['Cairo', 'Kyiv', 'San Francisco']

{
    'New York': {'Cairo', 'Tokyo', 'Buenos Aires', 'London'}, 
    'London': {'Madrid', 'New York', 'Dubai'},
    'Cairo': {'New York', 'Kyiv', 'Madrid'}, 
    'Tokyo': {'Buenos Aires', 'New York'}, 
    'Dubai': {'London'}, 
    'Kyiv': {'Cairo', 'San Francisco'}, 
    'Madrid': {'Cairo', 'London'}, 
    'Buenos Aires': {'Tokyo', 'New York'}, 
    'San Francisco': {'Kyiv'}
    }

       [
            ("Los Angeles", "Istanbul"),
            ("Los Angeles", "Shanghai"),
            ("Paris", "Singapore"),
            ("Istanbul", "Rome"),
            ("Paris", "Rome"),
            ("Rome", "Seattle"),
            ("Sydney", "Los Angeles"),
            ("Shanghai", "Sydney"),
            ("Sydney", "Cairo"),
            ("Cairo", "Seattle"),
            ("Seattle", "Tokyo"),
            ("Tokyo", "Shanghai"),
            ("Istanbul", "Cairo"),
            ("Rome", "Berlin"),
            ("Berlin", "Paris"),
            ("Singapore", "Sydney"),
            ("Cairo", "Istanbul"),
            ("Berlin", "Tokyo"),
        ],
        "Los Angeles",
        "Berlin",
        ["Los Angeles", "Istanbul", "Rome", "Berlin"],