
class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print(
                f"Overflow warning: cannot enqueue {item}; "
                "the queue is full."
            )
            return False

        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("Underflow warning: cannot dequeue; the queue is empty.")
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def display(self):
        print(
            f"Queue array: {self.queue} | "
            f"Head: {self.head} | "
            f"Tail: {self.tail} | "
            f"Size: {self.size}"
        )


def demonstrate_ten_operations():
    print("\n=== Ten Queue Operations (capacity = 5) ===")

    cq = CircularQueue(5)

    operations = [
        ("Enqueue", 10),
        ("Enqueue", 20),
        ("Enqueue", 30),
        ("Dequeue", None),
        ("Enqueue", 40),
        ("Enqueue", 50),
        ("Enqueue", 60),
        ("Dequeue", None),
        ("Enqueue", 70),
        ("Dequeue", None),
    ]

    for step, (operation, value) in enumerate(operations, start=1):
        if operation == "Enqueue":
            print(f"\nOperation {step}: enqueue({value})")
            cq.enqueue(value)
        else:
            print(f"\nOperation {step}: dequeue()")
            print(f"Dequeued: {cq.dequeue()}")

        cq.display()


if __name__ == "__main__":
    print("=== Circular Queue Buffer Implementation ===")

    # Basic queue operations
    cq = CircularQueue(5)

    print("\nInitial queue:")
    cq.display()

    print("\nBasic operations:")
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    print(f"Dequeued: {cq.dequeue()}")

    cq.enqueue(4)
    cq.display()

    # Demonstrate overflow
    print("\nOverflow demonstration:")

    overflow_queue = CircularQueue(2)
    overflow_queue.enqueue(100)
    overflow_queue.enqueue(200)
    overflow_queue.enqueue(300)
    overflow_queue.display()

    # Demonstrate underflow
    print("\nUnderflow demonstration:")

    empty_queue = CircularQueue(2)
    empty_queue.dequeue()

    # Demonstrate ten queue operations
    demonstrate_ten_operations()
