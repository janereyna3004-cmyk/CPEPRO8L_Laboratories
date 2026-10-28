# Laboratory Activity No. 3
## Singly Linked List CRUD Operations

**Name:** Mary Jane Y. Reyna  
**Date:** September 4, 2026  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

---

## 1. Objectives

The objectives of this laboratory activity are:

1. Construct custom Node and SinglyLinkedList classes.
2. Implement insertion at the head and tail of a singly linked list.
3. Manage list nodes and pointers without losing references.
4. Implement searching and deletion operations in a singly linked list.

## 2. Introduction

A singly linked list is a linear data structure consisting of nodes stored in non-contiguous memory locations. Each node contains data and a pointer to the next node.

Unlike arrays, linked lists do not require elements to occupy consecutive memory locations. This laboratory activity demonstrates how to create, traverse, search, and delete nodes using Python.

## 3. Implementation

The program uses two classes:

- **Node:** Stores the data and a reference to the next node.
- **SinglyLinkedList:** Manages the list and provides methods for inserting, searching, deleting, and displaying elements.

The implemented methods are:

| Method | Description |
|---|---|
| `insert_head(data)` | Inserts a new node at the beginning of the list. |
| `insert_tail(data)` | Inserts a new node at the end of the list. |
| `delete_value(target)` | Deletes the first node containing the specified value. |
| `search(target)` | Searches for a value and returns True if found or False otherwise. |
| `display()` | Displays the elements in the linked list. |

## 4. Execution and Output

The program was executed to test the insertion, searching, and deletion operations of a singly linked list.

### Program Output

    Inserting elements:
    20 -> 10 -> 30 -> None

    Searching for 30:
    Is 30 in list? True

    Deleting 10:
    Successfully deleted? True
    20 -> 30 -> None

    Searching for 10:
    Is 10 in list? False

### Explanation

1. **Insertion:** The program inserts 10 at the head, inserts 20 at the head, and inserts 30 at the tail. The resulting list is 20 -> 10 -> 30 -> None.
2. **Searching:** The program searches for 30 and returns True because the value exists in the list.
3. **Deletion:** The program deletes 10 and returns True to indicate successful deletion.
4. **Verification:** After deletion, the list becomes 20 -> 30 -> None. Searching for 10 returns False because the value is no longer in the list.

### Console Screenshot

Take a screenshot of your actual terminal output and save it as `output.png`.

Upload the image to the same GitHub repository folder as this README.

![Console Output](output.png)

## 5. Report Analysis Questions

### Question 1: What happens when a new node is inserted at the head of a singly linked list?

When a new node is inserted at the head, the program creates a new node and assigns the current head to its next pointer. The head pointer is then updated to reference the new node.

For example, inserting 20 at the head of a list containing 10 produces:

    20 -> 10 -> None

This operation takes O(1) time because it does not require traversing the list.

### Question 2: How does the program insert a node at the tail?

The program first creates a new node. If the list is empty, the new node becomes the head. Otherwise, the program traverses the list until it reaches the last node, whose next pointer is None.

The last node's next pointer is then updated to reference the new node.

For example:

    Before: 20 -> 10 -> None
    After:  20 -> 10 -> 30 -> None

The operation takes O(n) time in the worst case because the program may need to traverse the list to reach the last node.

### Question 3: How does the search operation work?

The search operation starts at the head and compares each node's data with the target value. If a match is found, the method returns True. If the traversal reaches None without finding a match, it returns False.

For example, searching for 30 in the list 20 -> 10 -> 30 -> None returns True.

The time complexity is O(n) in the worst case.

### Question 4: How does the program delete a middle node? Trace the pointers step by step.

Consider the linked list:

    10 -> 20 -> 30 -> None

The target value is 20.

**Step 1:** Initialize previous to the head and current to the second node.

    previous = self.head
    current = self.head.next

Now, previous points to node 10, and current points to node 20.

**Step 2:** Compare the data in current with the target value. Since current.data equals 20, the target has been found.

**Step 3:** Update the previous node's pointer.

    previous.next = current.next

This makes node 10 point directly to node 30, bypassing node 20.

**Step 4:** Return True to indicate successful deletion.

The resulting linked list is:

    10 -> 30 -> None

Updating the previous node's next pointer removes the target node from the linked list's chain of references. The head remains unchanged because the deleted node is in the middle.

### Question 5: What is the time complexity of the deletion operation?

The time complexity of delete_value() is O(n) in the worst case because the program may need to traverse the list to locate the target node.

If the target is at the head, deletion takes O(1) time because the head pointer can be updated directly.

## 6. Conclusion

This laboratory activity demonstrates the implementation of a singly linked list using Python. The program implements insertion at the head and tail, searching, deletion, and displaying the list.

The activity also demonstrates the importance of managing node pointers correctly. In particular, deleting a middle node requires updating the previous node's next pointer so that the remaining nodes stay connected.

Through this implementation, the basic operations and pointer management of a singly linked list are demonstrated.