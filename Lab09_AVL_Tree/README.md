
# Laboratory Activity No. 9: Height Balancing in AVL Trees

**Name:** Mary Jane Y. Reyna  
**Course:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

## 1. Introduction

An AVL Tree is a self-balancing Binary Search Tree (BST). It maintains a balance factor between -1 and 1 for every node. When an insertion makes the tree unbalanced, the AVL Tree automatically performs rotations to restore balance.

This activity demonstrates AVL tree insertion, height calculation, balance factor computation, and automatic tree rotations.

## 2. Objectives

1. Calculate node heights and balance factors dynamically.
2. Implement single and double rotations, including LL, RR, LR, and RL cases.
3. Demonstrate self-balancing tree insertions.
4. Understand how rotations maintain efficient tree operations.

## 3. Files Included

- `lab9_avl.py` - Python implementation of the AVL Tree.
- `README.md` - Documentation, execution output, and analysis.

## 4. How to Run the Program

1. Open the project folder in Visual Studio Code.
2. Make sure Python is installed.
3. Open the VS Code terminal.
4. Run the following command:

```bash
py lab9_avl.py
```

Alternatively, use:

```bash
python lab9_avl.py
```

## 5. Expected Output

```text
AVL TREE HEIGHT BALANCING
===================================
Keys to insert: [10, 20, 30]

Inserting 10...
Current tree:
Root: 10 (Height=1, Balance=0)

Inserting 20...
Current tree:
Root: 10 (Height=2, Balance=-1)
    R--- 20 (Height=1, Balance=0)

Inserting 30...
RR imbalance at node 10
Left rotation performed at node 10
Current tree:
Root: 20 (Height=2, Balance=0)
    L--- 10 (Height=1, Balance=0)
    R--- 30 (Height=1, Balance=0)

===================================
FINAL AVL TREE
===================================
Inorder traversal:
10 20 30

Final tree structure:
Root: 20 (Height=2, Balance=0)
    L--- 10 (Height=1, Balance=0)
    R--- 30 (Height=1, Balance=0)

Root node: 20
Tree height: 2
Root balance factor: 0
```

## 6. Report Analysis Questions

### 1. Implement the AVL insertion and rotation routines. Show a sequence diagram of a right rotation.

The AVL insertion routine first performs a standard Binary Search Tree insertion. It then updates the node height and calculates its balance factor. If a node becomes unbalanced, the program identifies the appropriate case and performs the necessary rotation.

A right rotation is used to correct an LL imbalance.

**Before rotation:**

```text
        30
       /
      20
     /
    10
```

**Right rotation at node 30:**

```text
        30                 20
       /                  /  \
      20       --->      10   30
     /
    10
```

**Sequence diagram:**

```text
Insert Operation     AVL Tree           Rotation
      |                  |                  |
      | Insert 10        |                  |
      |----------------->|                  |
      | Insert 20        |                  |
      |----------------->|                  |
      | Insert 30        |                  |
      |----------------->|                  |
      |                  | Detect LL case   |
      |                  |----------------->|
      |                  |   Rotate right   |
      |                  |<-----------------|
      |                  | Root becomes 20  |
      |<-----------------|                  |
      |   Balanced Tree                     |
```

The rotation changes the structure of the tree without changing the order of its keys. After rotation, the program updates the affected node heights.

### 2. Insert keys [10, 20, 30] sequentially into a tree and trace the automatic left rotation balancing step.

**Step 1: Insert 10**

Node 10 becomes the root. Its height is 1 and its balance factor is 0.

```text
10
```

**Step 2: Insert 20**

Node 20 is inserted as the right child of node 10. The balance factor of node 10 becomes -1, so the tree remains balanced.

```text
10
  \
   20
```

**Step 3: Insert 30**

Node 30 is inserted as the right child of node 20. Node 10 now has a balance factor of -2, causing an RR imbalance.

Before rotation:

```text
10
  \
   20
     \
      30
```

The AVL Tree performs a left rotation at node 10.

After rotation:

```text
     20
    /  \
   10   30
```

The final root is 20, the height is 2, and the root balance factor is 0. The tree is now balanced.

## 7. Results and Discussion

The program successfully implements AVL tree insertion and automatic balancing. It calculates node heights and balance factors and supports all four rotation cases: LL, RR, LR, and RL.

The insertion sequence [10, 20, 30] demonstrates how an RR imbalance is detected and corrected using a left rotation. The resulting tree maintains its sorted order and satisfies the AVL balance condition.

AVL trees provide O(log n) search, insertion, and deletion time in the general case because their height remains logarithmic in the number of nodes.

## 8. Conclusion

This laboratory activity demonstrates the importance of height balancing in AVL trees. By updating node heights, checking balance factors, and applying rotations, the program prevents a Binary Search Tree from becoming excessively unbalanced. The experiment confirms that automatic rotations maintain an efficient tree structure while preserving the correct ordering of the keys.
