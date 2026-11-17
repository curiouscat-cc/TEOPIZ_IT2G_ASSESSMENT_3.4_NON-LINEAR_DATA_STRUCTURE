# Binary Tree Structure Implementation for TEOPIZ

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def run():
    print("\n--- Binary Tree Structure (TEOPIZ) ---")
    # Building the tree
    root = TreeNode('T')
    root.left = TreeNode('E')
    root.right = TreeNode('O')
    root.left.left = TreeNode('P')
    root.left.right = TreeNode('I')
    root.right.left = TreeNode('Z')

    print("Level 0 (Root):", root.data)
    print("Level 1 (Children of T):", root.left.data, ",", root.right.data)
    print("Level 2 (Children of E & O):", root.left.left.data, ",", root.left.right.data, ",", root.right.left.data)
    print("\nBinary Tree Structure successfully displayed.")

if __name__ == "__main__":
    run()