from bst import TreeNode as BST
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
            print("FindMinMax - find the minimum and maximum values in the trees")
            print("SortAndMedian - sort the trees and find the median")
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
            num_nodes = int(input('nodes> '))
            keys = list(map(int, input('insert> ').split()))
            for key in keys: 
                tree.insert(key)
        elif command == 'delete':
                root = None
                print(f"All nodes have been deleted from the {treeName} tree.")
        elif command == 'rebalance':
            root = tree.rebalance(root)
            print(f"{treeName} tree has been balanced.")
        elif command == 'remove':
            keys = list(map(int, input('remove> ').split()))
            for key in keys:
                root = tree.delete(root, key)
        elif command == 'findMinMax':
            minTree = tree.minValueNode(root).key
            maxTree = tree.maxValueNode(root).key
            print(f"{treeName} tree: Min = {minTree}, Max = {maxTree}")
        elif command == 'sortAndMedian':
            print(f"{treeName} tree sorted:")
            tree.inOrder(root)
            print(f"\nMedian: {tree.findMedian(root)}")
        else:
            print("Unknown command. Please try again. Type help for more information.")

def main():
    #avl_tree = avl.AVLTree()
    bst_tree = BST()
    #avl_root = None
    bst_root = None

    #if args.avl:
     #   chosenTree("AVL", avl _tree, avl_root)
    if args.bst:
        chosenTree("BST", bst_tree, bst_root)
        # elif command == 'print':
        #     if args.avl:
        #         print("AVL tree:")
        #         print("In-order:", end=" ")
        #         avl_tree.inOrder(avl_root)
        #         print("\nPost-order:", end=" ")
        #         avl_tree.postOrder(avl_root)
        #         print("\nPre-order:", end=" ")
        #         avl_tree.preOrder(avl_root)
        #     if args.bst:
        #         print("BST tree:")
        #         print("In-order:", end=" ")
        #         bst_tree.inOrder(bst_root)
        #         print("\nPost-order:", end=" ")
        #         bst_tree.postOrder(bst_root)
        #         print("\nPre-order:", end=" ")
        #         bst_tree.preOrder(bst_root)
        # elif command == "tickz":
        #     if args.avl:
        #         print("AVL tree has been saved to a txt file:")
        #         writeTikzToFile(os.path.join(CURRENT_DIR, 'tickzpictureAVL.txt'), tikz_tree(avl_root))
        #     if args.bst:
        #         print("BST tree: has been saved to a txt file:")
        #         writeTikzToFile(os.path.join(CURRENT_DIR, 'tickzpictureBST.txt'), tikz_tree(bst_root))
        # elif command == 'insert':
        #     num_nodes = int(input('nodes> '))
        #     keys = list(map(int, input('insert> ').split()))
        #     for key in keys:
        #         if args.avl:
        #             avl_root = avl_tree.insert(avl_root, key)
        #         if args.bst:
        #             bst_root = bst_tree.insert(bst_root, key)
        # elif command == 'delete':
        #     if args.avl:
        #         avl_root = None
        #     if args.bst:
        #         bst_root = None
        # elif command == 'rebalance':
        #     if args.avl:
        #         avl_root = avl_tree.rebalance(avl_root)
        #         print("AVL tree has been balanced.")
        #     if args.bst:
        #         bst_root = bst_tree.rebalance(bst_root)
        #         print("BST tree has been balanced.")
        # elif command == 'remove':
        #     keys = list(map(int, input('remove> ').split()))
        #     for key in keys:
        #         avl_root = avl_tree.delete(avl_root, key)
        #         bst_root = bst_tree.delete(bst_root, key)
        # elif command == 'findMinMax':
        #     avl_min = avl_tree.minValueNode(avl_root).key
        #     avl_max = avl_tree.maxValueNode(avl_root).key
        #     bst_min = bst_tree.minValueNode(bst_root).key
        #     bst_max = bst_tree.maxValueNode(bst_root).key
        #     print(f"AVL tree: Min = {avl_min}, Max = {avl_max}")
        #     print(f"BST tree: Min = {bst_min}, Max = {bst_max}")
        # elif command == 'sortAndMedian':
        #     print("AVL tree sorted:")
        #     avl_tree.inOrder(avl_root)
        #     print(f"\nMedian: {avl_tree.findMedian(avl_root)}")

        #     print("\nBST tree sorted:")
        #     bst_tree.inOrder(bst_root)
        #     print(f"\nMedian: {bst_tree.findMedian(bst_root)}")
        

if __name__ == "__main__":
    main()
