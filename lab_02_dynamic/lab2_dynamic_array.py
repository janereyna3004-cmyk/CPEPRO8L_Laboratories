
import ctypes

class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def append(self, element):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.array[self.size] = element
        self.size += 1

    def _resize(self, new_capacity):
        print(
            f"Resizing: Capacity {self.capacity} -> {new_capacity}"
        )

        new_array = self._make_array(new_capacity)

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == "__main__":
    arr = DynamicArray()

    for i in range(10):
        arr.append(i)
        print(
            f"Appending {i} | Size: {len(arr)} | "
            f"Capacity: {arr.capacity} | "
            f"Element at index {i}: {arr[i]}"
        )
