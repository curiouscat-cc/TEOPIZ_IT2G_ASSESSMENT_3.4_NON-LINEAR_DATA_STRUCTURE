# Main Menu Selection for Assessment 3.3 (Non-Linear Data Structures)

import binary_tree
import graph
import binary_tree_traversal
import graph_traversal


def show_menu():
    while True:
        print("\n==============================================")
        print("  ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURES")
        print("  DATASET: TEOPIZ (T, E, O, P, I, Z)")
        print("==============================================")
        print(" [1] Binary Tree Structure")
        print(" [2] Graph Structure")
        print(" [3] Binary Tree Traversals (BFS & DFS)")
        print(" [4] Graph Traversals (BFS & DFS)")
        print(" [5] Exit Program")
        print("==============================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            binary_tree.run()
        elif choice == '2':
            graph.run()
        elif choice == '3':
            binary_tree_traversal.run()
        elif choice == '4':
            graph_traversal.run()
        elif choice == '5':
            print("\nExiting program. Good luck with your submission!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    show_menu()