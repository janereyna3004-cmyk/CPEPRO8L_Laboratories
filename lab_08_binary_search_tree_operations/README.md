
# Laboratory Activity No. 8
## Binary Search Tree Insertion and Traversals

**Name:** Mary Jane Y. Reyna  
**Date:** September 6, 2026  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

## 1. Objectives

1. Implement dynamic tree nodes with left and right child references.
2. Create insertion and lookup-related BST logic.
3. Implement recursive inorder, preorder, and postorder traversals.
4. Understand how a Binary Search Tree organizes numerical data.

## 2. Description

A Binary Search Tree (BST) is a hierarchical, non-linear data structure.
Each node contains a key and references to its left and right children.

In this implementation, values smaller than the current node are
inserted into the left subtree, while values greater than or equal
to the current node are inserted into the right subtree.

The program inserts the following elements:

50, 30, 70, 20, 40, 60, 80

## 3. Source Code

The Python program is saved as `lab8_bst.py`.

It contains the following components:

- `TreeNode`: Creates a node with a key, left child, and right child.
- `BST`: Manages the binary search tree.
- `insert()`: Adds a value to the tree.
- `_insert_recursive()`: Finds the correct location for a new value.
- `inorder()`: Visits the left subtree, node, and right subtree.
- `preorder()`: Visits the node, left subtree, and right subtree.
- `postorder()`: Visits the left subtree, right subtree, and node.

## 4. Execution Instructions

1. Open the project folder in Visual Studio Code.
2. Make sure Python is installed.
3. Open a new terminal in VS Code.
4. Run the following command:

   `py lab8_bst.py`

5. Observe the three traversal results in the terminal.

## 5. Expected Output

```text
Inorder Traversal:
20 30 40 50 60 70 80
Preorder Traversal:
50 30 20 40 70 60 80
Postorder Traversal:
20 40 30 60 80 70 50
```

## 6. Analysis Questions

### Question 1: Complete all traversals and write down the Preorder and Postorder outputs for the test tree.

**Answer:**

The Preorder Traversal output is:

`50 30 20 40 70 60 80`

Preorder visits the root node first, followed by the left subtree
and then the right subtree.

The Postorder Traversal output is:

`20 40 30 60 80 70 50`

Postorder visits the left subtree first, followed by the right
subtree, and then the root node.

The Inorder Traversal output is:

`20 30 40 50 60 70 80`

### Question 2: Explain why the inorder traversal of a BST outputs items in sorted order.

**Answer:**

Inorder traversal produces sorted values because it visits the
left subtree before the current node and the right subtree afterward.
In a Binary Search Tree, values in the left subtree are smaller than
the node's key, while values in the right subtree are greater than
or equal to the node's key in this implementation.

By recursively following this rule for every node, the program
displays the values in ascending order.

## 7. Conclusion

This activity demonstrates how a Binary Search Tree stores and
organizes numerical values through recursive insertion. It also
shows how inorder, preorder, and postorder traversals visit nodes
in different sequences.

The inorder traversal displays the values in ascending order,
while preorder and postorder demonstrate alternative ways of
visiting the nodes in a tree.
