# Laboratory Activity No. 4
# Title: Doubly and Circular Linked Lists
# Course Code: CPEPRO8L
# Course Title: Data Structures and Algorithms

# ------------------------------------------
# DOUBLY LINKED LIST
# ------------------------------------------

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        # Create a new node
        new_node = DoubleNode(data)

        # Link the new node to the current head
        new_node.next = self.head

        # Update the previous pointer of the old head
        if self.head is not None:
            self.head.prev = new_node

        # Make the new node the head
        self.head = new_node

    def display_forward(self):
        temp = self.head
        elements = []

        # Traverse the list from head to tail
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next

        print("None <-> " + " <-> ".join(elements) + " <-> None")


# ------------------------------------------
# CIRCULAR SINGLY LINKED LIST
# ------------------------------------------

class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, data):
        # Create a new node
        new_node = CircularNode(data)

        # Handle the empty list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        # Traverse to the last node
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        # Connect the old tail to the new node
        temp.next = new_node

        # Connect the new tail back to the head
        new_node.next = self.head

    def display(self):
        # Handle the empty list
        if self.head is None:
            print("The circular linked list is empty.")
            return

        temp = self.head
        elements = []

        # Traverse the circular list exactly once
        while True:
            elements.append(str(temp.data))
            temp = temp.next

            # Stop when traversal returns to the head
            if temp == self.head:
                break

        print(" -> ".join(elements) + " -> (loops to " +
              str(self.head.data) + ")")


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

if __name__ == "__main__":

    print("--- Testing Doubly Linked List ---")

    dll = DoublyLinkedList()
    dll.insert_head(5)
    dll.insert_head(10)
    dll.display_forward()

    print("\n--- Testing Circular Linked List ---")

    cll = CircularSinglyLinkedList()
    cll.insert_tail(100)
    cll.insert_tail(200)
    cll.insert_tail(300)
    cll.display()