from bst import TreeNode as BST
from avl import TreeNode as AVL
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-avl", action="store_true", help="Work on AVL tree")
parser.add_argument("-bst", action="store_true", help="Work on BST tree")
args = parser.parse_args()
CURRENT_DIR = os.path.dirname(__file__)
positions = {}

def chosenTree(treeName, tree, root):
    treeName = treeName.upper()
    while True:
        command = input('command> ').lower()
        if command == 'help':
            print("--- Help ---")
            print("Commands:")
            print("Help - display this message")
            print("Exit - exit the program")
            print("Print - print the trees")
            print("Insert - insert a node into the trees")
            print("Delete - delete all nodes from the trees")
            print("Rebalance - rebalance the AVL tree")
            print("Remove - remove a node from the trees")
            print("MinMax - find the minimum and maximum values in the trees")
            print("Height- return the height of the tree")
            print("-------------")
            continue
        if command == 'exit':
            break
        if command == "print":
            print(treeName, " tree:")
            print("In-order:", end=" ")
            tree.in_order()
            print("\nPost-order:", end=" ")
            tree.post_order()
            print("\nPre-order:", end=" ")
            tree.pre_order()
            print("")
        elif command == 'insert':
            if treeName == "BST":
                num_nodes = int(input('nodes> '))
                keys = list(map(int, input('insert> ').split()))
                for key in keys: 
                    tree.insert(key)
            elif treeName == "AVL":
                num_nodes = int(input('nodes> '))
                keys = list(map(int, input('insert> ').split()))
                for key in keys:
                    root = tree.insert(keys)
        elif command == 'delete':
                tree.delete_all()
                print(f"All nodes have been deleted from the {treeName} tree.")
        elif command == 'rebalance':
            root = tree.rebalance(root)
            print(f"{treeName} tree has been balanced.")
        elif command == 'remove':
            keys = list(map(int, input('remove> ').split()))
            for key in keys:
                tree.delete(key)
        elif command == 'find':
            znajdzka = int(input('find> '))
            print(tree.find(znajdzka))
        elif command == 'minmax':
            print("Max: ",tree.largest(),"\nMin: ",tree.smallest(),"\n")  
        elif command == 'height':
            
            print("Height: ",tree.get_height())
        else:
            print("Unknown command. Please try again. Type help for more information.")

def main():
    avl_tree = AVL()
    bst_tree = BST()
    avl_root = None
    bst_root = None

    if args.avl:
        chosenTree("AVL", avl_tree, avl_root)
    if args.bst:
        chosenTree("BST", bst_tree, bst_root)
if __name__ == "__main__":
    main()
