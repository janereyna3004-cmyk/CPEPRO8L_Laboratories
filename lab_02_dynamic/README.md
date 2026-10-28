# Laboratory Activity No. 2

## Dynamic Array Builder & Capacity Allocation

**Student Name:** MARY JANE Y. REYNA  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027  
**Date:** September 2, 2026

### Objectives

1. Implement a custom dynamic array using Python's `ctypes` module.
2. Understand capacity scaling, memory doubling, and the cost of copying elements.
3. Observe how index access works in constant time, O(1).

### Implementation

The `DynamicArray` class implements the following operations:

- `__len__()`: Returns the number of elements.
- `__getitem__(index)`: Returns an element at a valid index and raises `IndexError` for an invalid index.
- `append(element)`: Adds an element and resizes the array when necessary.
- `_resize(new_capacity)`: Allocates a new array, copies the existing elements, and updates the capacity.
- `_make_array(new_capacity)`: Creates a low-level array using `ctypes.py_object`.

### Execution and Output

The program was executed by appending the integers 0 through 9 to the dynamic array.

The initial capacity is 1. Whenever the array becomes full, its capacity doubles.

| Old Capacity | New Capacity | Size Before Append |
|---|---|---|
| 1 | 2 | 1 |
| 2 | 4 | 2 |
| 4 | 8 | 4 |
| 8 | 16 | 8 |

After inserting 10 elements, the final size is 10 and the final capacity is 16.

### Analysis Questions

**1. At what sizes does capacity resizing occur?**

Resizing occurs when the array is full, at sizes 1, 2, 4, and 8 before the next element is appended. The capacity changes from 1 to 2, 2 to 4, 4 to 8, and 8 to 16.

**2. Why does the dynamic array copy elements during resizing? What is the time complexity of a single resize operation?**

The array copies its existing elements into a newly allocated memory block because the current block does not have enough space for additional elements. Doubling the capacity provides room for future insertions.

A single resize operation has O(n) time complexity because all existing elements must be copied to the new array.

### Conclusion

This activity demonstrates how a dynamic array manages memory and grows when additional elements are inserted. By doubling its capacity when full, the array reduces the frequency of resizing. Element access by index takes O(1) time, while a single resize operation takes O(n) time.