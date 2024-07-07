class Graph:
    def __init__(self, edges):
        # Initialize the graph with edges
        self.edges = edges
        # Create an empty dictionary to store the graph structure
        self.graph_dict = {}
        # Loop through each edge in the list of edges
        for start, end in self.edges:
            # If the starting node is already in the dictionary, append the ending node
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                # If the starting node is not in the dictionary, add it with the ending node in a list
                self.graph_dict[start] = [end]
        # Print the graph structure for verification
        print(f"Graph dict: {self.graph_dict}")

    def get_paths(self, start, end, path=[]):
        # Add the starting node to the current path
        path = path + [start]

        # If the starting node is the same as the ending node, return the current path
        if start == end:
            return [path]

        # If the starting node is not in the graph, return an empty list
        if start not in self.graph_dict:
            return []

        # Initialize an empty list to store all possible paths
        paths = []
        # Loop through each node connected to the starting node
        for node in self.graph_dict[start]:
            # If the node is not already in the current path
            if node not in path:
                # Recursively find all paths from the node to the end
                new_paths = self.get_paths(node, end, path)
                # Add each new path to the list of paths
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        # Add the starting node to the current path
        path = path + [start]

        # If the starting node is the same as the ending node, return the current path
        if start == end:
            return path

        # If the starting node is not in the graph, return None
        if start not in self.graph_dict:
            return None

        # Initialize a variable to store the shortest path
        shortest_path = None
        # Loop through each node connected to the starting node
        for node in self.graph_dict[start]:
            # If the node is not already in the current path
            if node not in path:
                # Recursively find the shortest path from the node to the end
                sp = self.get_shortest_path(node, end, path)
                # If a valid path is found
                if sp:
                    # Update the shortest path if it's the first one found or if it's shorter than the current shortest path
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    # List of routes represented as edges in the graph
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    # Create a graph from the routes
    route_graph = Graph(routes)

    # Define the starting and ending points
    start = "Paris"
    end = "New York"

    # Find and print the shortest path between the start and end points
    print(f"Shortest path between {start} and {end}: \n{route_graph.get_shortest_path(start, end)}")
