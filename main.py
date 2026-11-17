# Main Menu Selection for Assessment 3.3 (Non-Linear Data Structures)

import binary_tree_program
import graph_program
import binary_tree_traversal
import graph_traversal


def show_menu():
    while True:
        print("\n==============================================")
        print("           NON-LINEAR DATA STRUCTURES          ")
        print("==============================================")
        print(" 1. Binary Tree")
        print(" 2. Graph")
        print(" 3. Binary Tree Traversal Method (BFS & DFS)")
        print(" 4. Graph Traversal Method (BFS & DFS)")
        print(" 5. Exit Program")
        print("==============================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            binary_tree_program.run()
        elif choice == '2':
            graph_program.run()
        elif choice == '3':
            binary_tree_traversal.run()
        elif choice == '4':
            graph_traversal.run()
        elif choice == '5':
            print("\nExiting program. Thank you for viewing!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    show_menu()