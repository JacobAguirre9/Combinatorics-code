# Here's an example of how you might write a Python function to check if a graph is Eulerian without using any packages:

def is_eulerian(graph):
    vertex_degrees = {}
    for node in graph:
        for neighbor in graph[node]:
            vertex_degrees[node] = vertex_degrees.get(node, 0) + 1
    for node in vertex_degrees:
        if vertex_degrees[node] % 2 != 0:
            return False
    return True

# sample usage
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B"],
    "D": ["B"]
}

print(is_eulerian(graph)) # True


# In this example, the function takes a graph represented by an adjacency list, where the keys are the vertices and the values are 
# lists with the edges as elements.
# It defines an empty dictionary vertex_degrees to store the degree of each vertex.
# It iterates over the keys and values of the graph, in each iteration, it counts how many edges are linked to each vertex and store it
# in the vertex_degrees dictionary.
# Then it iterates over the vertex_degrees dictionary and for each node, it checks if the degree of this node is even or not, if not, it returns false. 
# If the iteration ends, it returns true.

# Please note that this is an adjacency list representation of graph, where the edges are represented by a list.
# If you are using an adjacency matrix, the logic of the function will change, but the idea is the same.
