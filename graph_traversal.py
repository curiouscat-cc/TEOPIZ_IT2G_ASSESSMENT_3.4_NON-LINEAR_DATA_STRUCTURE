# Graph Traversal (BFS & DFS) for TEOPIZ

from collections import deque

def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal = []

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal

def dfs_graph(graph, start):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            # Push reverse order to match standard left-to-right exploration
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return traversal

def run():
    print("\n--- Graph Traversals (BFS & DFS) ---")
    graph = {
        'T': ['E', 'O', 'P'],
        'E': ['T', 'I'],
        'O': ['T', 'Z'],
        'P': ['T', 'Z'],
        'I': ['E'],
        'Z': ['O', 'P']
    }

    print("Graph BFS Traversal:", " - ".join(bfs_graph(graph, 'T')))
    print("Graph DFS Traversal:", " - ".join(dfs_graph(graph, 'T')))

if __name__ == "__main__":
    run()