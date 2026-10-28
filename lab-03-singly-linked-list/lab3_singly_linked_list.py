class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        # Create a new node and link it to the current head.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        # Create a new node.
        new_node = Node(data)

        # If the list is empty, the new node becomes the head.
        if self.head is None:
            self.head = new_node
            return

        # Traverse the list until the last node.
        current = self.head
        while current.next is not None:
            current = current.next

        # Link the last node to the new node.
        current.next = new_node

    def delete_value(self, target):
        # If the list is empty, nothing can be deleted.
        if self.head is None:
            return False

        # If the head contains the target value.
        if self.head.data == target:
            self.head = self.head.next
            return True

        # Search for the target while keeping track of the previous node.
        previous = self.head
        current = self.head.next

        while current is not None:
            if current.data == target:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        # Target was not found.
        return False

    def search(self, target):
        # Traverse the list to find the target.
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next

        return False

    def display(self):
        current = self.head
        elements = []

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("Inserting elements:")
    sll.insert_head(10)
    sll.insert_head(20)
    sll.insert_tail(30)
    sll.display()

    print("\nSearching for 30:")
    print(f"Is 30 in list? {sll.search(30)}")

    print("\nDeleting 10:")
    print(f"Successfully deleted? {sll.delete_value(10)}")
    sll.display()

    print("\nSearching for 10:")
    print(f"Is 10 in list? {sll.search(10)}")