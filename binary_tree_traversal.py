# Binary Tree Traversal (BFS & DFS) for TEOPIZ

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def dfs_preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.data)
        dfs_preorder(node.left, result)
        dfs_preorder(node.right, result)
    return result

def run():
    print("\n--- Binary Tree Traversals (BFS & DFS) ---")
    root = TreeNode('T')
    root.left = TreeNode('E')
    root.right = TreeNode('O')
    root.left.left = TreeNode('P')
    root.left.right = TreeNode('I')
    root.right.left = TreeNode('Z')

    print("BFS Traversal:", " - ".join(bfs(root)))
    print("DFS (Preorder) Traversal:", " - ".join(dfs_preorder(root)))

if __name__ == "__main__":
    run()