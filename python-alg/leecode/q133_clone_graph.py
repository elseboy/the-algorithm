class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None


original_graph = Node(1, [Node(2), Node(4)])
original_graph.neighbors[0].neighbors = [original_graph, Node(3)]
original_graph.neighbors[1].neighbors = [Node(1), original_graph.neighbors[0]]
original_graph.neighbors[0].neighbors[1].neighbors = [original_graph, Node(3)]

cloned_graph = cloneGraph(original_graph)


def print_graph(node):
    if not node:
        return
    visited = set()

    def dfs_print(current):
        if current in visited:
            return
        visited.add(current)
        print(
            f"Node {current.val}: {[(neighbor.val) for neighbor in current.neighbors]}"
        )
        for neighbor in current.neighbors:
            dfs_print(neighbor)

    dfs_print(node)


print("Original Graph:")
print_graph(original_graph)

print("\nCloned Graph:")
print_graph(cloned_graph)
