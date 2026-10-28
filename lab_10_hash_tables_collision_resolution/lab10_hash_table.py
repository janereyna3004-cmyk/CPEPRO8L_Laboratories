
class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return sum(ord(char) for char in key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)

        if self.buckets[index] is None:
            self.buckets[index] = HashNode(key, value)
            self.size += 1
            return

        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return

            if current.next is None:
                break

            current = current.next

        current.next = HashNode(key, value)
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def load_factor(self):
        return self.size / self.capacity

    def display(self):
        for index in range(self.capacity):
            chain = []
            current = self.buckets[index]

            while current is not None:
                chain.append(f"[{current.key}: {current.value}]")
                current = current.next

            print(f"Bucket {index}: " + " -> ".join(chain))


if __name__ == "__main__":
    ht = HashTable(5)

    ht.put("Alice", 25)
    ht.put("Bob", 30)
    ht.put("Charlie", 35)
    ht.put("Eve", 28)

    print("HASH TABLE: CHAINING")
    ht.display()

    print("\nSEARCH RESULTS")
    print("Alice:", ht.get("Alice"))
    print("Bob:", ht.get("Bob"))
    print("Charlie:", ht.get("Charlie"))
    print("David:", ht.get("David"))

    print("\nLOAD FACTOR")
    print(f"Entries: {ht.size}")
    print(f"Capacity: {ht.capacity}")
    print(f"Load factor: {ht.load_factor():.2f}")

