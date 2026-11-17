# Graph Structure Implementation for TEOPIZ

class Graph:
    def __init__(self):
        self.adjacency_list = {
            'T': ['E', 'O', 'P'],
            'E': ['T', 'I'],
            'O': ['T', 'Z'],
            'P': ['T', 'Z'],
            'I': ['E'],
            'Z': ['O', 'P']
        }

    def display(self):
        print("\n--- Graph Adjacency List (TEOPIZ) ---")
        for vertex, neighbors in self.adjacency_list.items():
            print(f"Vertex {vertex} -> Connected to: {', '.join(neighbors)}")

def run():
    g = Graph()
    g.display()

if __name__ == "__main__":
    run()