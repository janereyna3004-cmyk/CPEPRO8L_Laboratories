
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def rotate_right(self, y):
        # Right rotation for LL imbalance
        x = y.left
        subtree = x.right

        x.right = y
        y.left = subtree

        self.update_height(y)
        self.update_height(x)

        print(f"Right rotation performed at node {y.key}")
        return x

    def rotate_left(self, x):
        # Left rotation for RR imbalance
        y = x.right
        subtree = y.left

        y.left = x
        x.right = subtree

        self.update_height(x)
        self.update_height(y)

        print(f"Left rotation performed at node {x.key}")
        return y

    def insert(self, root, key):
        # Standard BST insertion
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Ignore duplicate keys
            return root

        # Update height
        self.update_height(root)

        # Calculate balance factor
        balance = self.get_balance(root)

        # LL Case
        if balance > 1 and key < root.left.key:
            print(f"LL imbalance at node {root.key}")
            return self.rotate_right(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            print(f"RR imbalance at node {root.key}")
            return self.rotate_left(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            print(f"LR imbalance at node {root.key}")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            print(f"RL imbalance at node {root.key}")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def print_tree(self, root, level=0, label="Root: "):
        if root:
            print(" " * (level * 4) + label + str(root.key)
                  + f" (Height={root.height}, Balance={self.get_balance(root)})")
            self.print_tree(root.left, level + 1, "L--- ")
            self.print_tree(root.right, level + 1, "R--- ")


def main():
    avl = AVLTree()
    root = None

    # Required sequence from the laboratory activity
    keys = [10, 20, 30]

    print("AVL TREE HEIGHT BALANCING")
    print("=" * 35)
    print("Keys to insert:", keys)

    for key in keys:
        print(f"\nInserting {key}...")
        root = avl.insert(root, key)
        print("Current tree:")
        avl.print_tree(root)

    print("\n" + "=" * 35)
    print("FINAL AVL TREE")
    print("=" * 35)

    print("Inorder traversal:")
    avl.inorder(root)
    print()

    print("\nFinal tree structure:")
    avl.print_tree(root)

    print("\nRoot node:", root.key)
    print("Tree height:", avl.get_height(root))
    print("Root balance factor:", avl.get_balance(root))


if __name__ == "__main__":
    main()
