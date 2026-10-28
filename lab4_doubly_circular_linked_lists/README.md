# Laboratory Activity No. 4
## Doubly and Circular Linked Lists

**Name:** Mary Jane Y. Reyna  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Date:** September 5, 2026  
**Term:** First Semester, AY 2026–2027

---

## 1. Introduction

A linked list is a data structure consisting of nodes that store data and references to other nodes.

A Doubly Linked List contains two pointers in each node: `next` and `prev`. The `next` pointer refers to the next node, while the `prev` pointer refers to the previous node. This allows the list to support traversal in both directions.

A Circular Singly Linked List is a linked list in which the last node points back to the first node. Unlike a regular linked list, it does not end with a `None` reference at the tail.

This activity demonstrates the implementation, insertion, and traversal of doubly linked lists and circular singly linked lists using Python.

---

## 2. Objectives

The objectives of this laboratory activity are:

1. To implement a Doubly Linked List using `next` and `prev` pointers.
2. To implement a Circular Singly Linked List and connect the last node back to the head.
3. To understand the differences between linear and circular linked lists.
4. To demonstrate correct insertion and traversal operations.
5. To prevent infinite loops when traversing a circular linked list.

---

## 3. Program Description

The program implements two types of linked lists.

### A. Doubly Linked List

The Doubly Linked List uses the following components:

- `DoubleNode`: Represents a node containing data, a next pointer, and a previous pointer.
- `DoublyLinkedList`: Manages the list and provides insertion and forward traversal methods.
- `insert_head(data)`: Inserts a new node at the beginning of the list.
- `display_forward()`: Traverses the list from the head to the tail and displays its elements.

When a new node is inserted at the head, its `next` pointer references the previous head. The previous head's `prev` pointer is updated to reference the new node.

### B. Circular Singly Linked List

The Circular Singly Linked List uses the following components:

- `CircularNode`: Represents a node containing data and a next pointer.
- `CircularSinglyLinkedList`: Manages the circular linked list.
- `insert_tail(data)`: Inserts a new node at the end of the list.
- `display()`: Displays the elements of the circular list exactly once.

When the list is empty, the first node points to itself. When additional nodes are inserted, the last node's `next` pointer is updated to point back to the head.

---

## 4. Source Code

The Python source code is saved in the following file:

`lab4_doubly_circular.py`

The program creates a Doubly Linked List containing the values `10` and `5`, followed by a Circular Singly Linked List containing the values `100`, `200`, and `300`.

Both implementations are tested in the main program.

---

## 5. Execution and Output

```bash
python lab4_doubly_circular.py
```

If the command does not work, try:

```bash
py lab4_doubly_circular.py
```

### Expected Output

```text
--- Testing Doubly Linked List ---
None <-> 10 <-> 5 <-> None

--- Testing Circular Linked List ---
100 -> 200 -> 300 -> (loops to 100)
```

### Output Explanation

The Doubly Linked List displays:

`None <-> 10 <-> 5 <-> None`

The values appear in reverse insertion order because each new value is inserted at the head. The `None` values at both ends indicate that the list has no previous node before its head and no next node after its tail.

The Circular Singly Linked List displays:

`100 -> 200 -> 300 -> (loops to 100)`

This output demonstrates that the last node, containing `300`, points back to the head node, containing `100`. This connection forms a circular structure.

---

## 6. Report Analysis Questions

### Question 1: Were the classes completed successfully, and did the program execute without compilation or runtime errors?

**Answer:**

Yes. The classes were completed successfully, and the program is designed to execute without syntax or runtime errors under normal conditions with a working Python installation.

The `DoubleNode` and `DoublyLinkedList` classes implement a doubly linked list with correctly connected `next` and `prev` pointers. The `CircularNode` and `CircularSinglyLinkedList` classes implement a circular singly linked list in which the last node points back to the head.

The program tests insertion and traversal operations for both structures. When executed correctly, it produces the expected output for the Doubly Linked List and the Circular Singly Linked List.

### Question 2: Explain the termination condition in a loop traversal of a Circular Linked List to prevent infinite loops.

**Answer:**

A Circular Linked List does not terminate at a `None` reference because the last node points back to the head. Therefore, using a condition such as `while temp is not None` would cause an infinite loop when traversing a properly formed circular list.

To prevent this, the program uses the condition `if temp == self.head: break` after moving to the next node. Traversal starts at the head and continues until the pointer returns to the head, indicating that every node has been visited exactly once.

This termination condition allows the program to display all elements without repeatedly traversing the same nodes. It is an important technique when working with circular data structures.

---

## 7. Conclusion

In conclusion, this laboratory activity demonstrated the implementation and traversal of Doubly Linked Lists and Circular Singly Linked Lists using Python.

The Doubly Linked List showed how the `next` and `prev` pointers connect nodes and allow forward traversal. Inserting values at the head also demonstrated how the order of elements changes depending on the insertion method.

The Circular Singly Linked List demonstrated how the last node connects back to the head, forming a continuous circular structure. The traversal termination condition ensured that the program displayed each element once without entering an infinite loop.

Overall, this activity improved my understanding of linked list structures, node connections, insertion operations, and traversal techniques. It also highlighted the importance of using appropriate termination conditions when working with circular data structures.

---

