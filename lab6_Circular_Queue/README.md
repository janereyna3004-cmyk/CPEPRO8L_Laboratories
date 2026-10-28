# Laboratory Activity No. 6
## Circular Queue Buffer Implementation

**Name:** Mary Jane Y. Reyna  
**Date:** September 5, 2026  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

---

## 1. Introduction

A queue is a linear data structure that follows the First-In, First-Out (FIFO) principle. This means that the first element inserted into the queue is the first element removed.

A circular queue is an improved queue implementation that uses a fixed-size array. Unlike a regular queue, it allows the end of the array to wrap around to the beginning. This is accomplished using the modulo (%) operator, which helps reuse empty positions and manage the available storage efficiently.

## 2. Objectives

1. Implement a fixed-capacity circular queue using Python.
2. Understand circular index wrapping using the modulo operator.
3. Implement enqueue and dequeue operations.
4. Handle overflow when the queue is full.
5. Handle underflow when the queue is empty.
6. Observe queue states during a series of 10 enqueue and dequeue operations.

## 3. Methodology

The activity was completed using Python in Visual Studio Code. A `CircularQueue` class was created with a fixed capacity, an array, a head index, a tail index, and a size counter.

The following methods were implemented:

- `__init__()` initializes the circular queue.
- `is_full()` checks whether the queue has reached its maximum capacity.
- `is_empty()` checks whether the queue contains no elements.
- `enqueue()` inserts a new element at the tail of the queue.
- `dequeue()` removes the element at the head of the queue.
- `display()` displays the queue array, head, tail, and size.

The modulo operator is used to update the head and tail positions circularly.

## 4. Source Code

The Python source code is saved in the file:

`lab6_circular_queue.py`

The program demonstrates basic queue operations, overflow and underflow conditions, and a series of 10 enqueue and dequeue operations.

## 5. How to Execute the Program

Follow these steps to run the program in Visual Studio Code:

1. Open Visual Studio Code.
2. Open the folder containing `lab6_circular_queue.py`.
3. Select **Terminal > New Terminal**.
4. Type the following command:

   ```bash
   python lab6_circular_queue.py
   ```

5. Press Enter to execute the program.

If the command does not work, try:

```bash
py lab6_circular_queue.py
```

The terminal will display the queue operations and their corresponding results.

## 6. Execution and Output

The program begins by displaying the initial queue and demonstrating the basic operations.

### Sample Output

```text
=== Circular Queue Buffer Implementation ===

Initial queue:
Queue array: [None, None, None, None, None] | Head: 0 | Tail: 0 | Size: 0

Basic operations:
Dequeued: 1
Queue array: [None, 2, 3, 4, None] | Head: 1 | Tail: 4 | Size: 3
```

The program also demonstrates overflow and underflow warnings and displays the queue state after each of the 10 operations.

### Screenshot of Program Output

After running the program, take a screenshot of the actual terminal output in Visual Studio Code.

Save the screenshot in the project folder using the filename `output.png`.

If the screenshot is saved in the same folder as this README file, you can display it here using the following Markdown:

```markdown
![Circular Queue Program Output](output.png)
```

## 7. Report Analysis Questions

### Question 1: Record the queue states during a series of 10 enqueues and dequeues.

The following table shows the queue states after each operation. The queue has a capacity of five elements.

The head points to the next element to be removed, while the tail points to the next available insertion position. The value `None` indicates an empty array position.

| Step | Operation | Result | Queue Array | Head | Tail | Size |
|---:|---|---|---|---:|---:|---:|
| 1 | Enqueue 10 | Inserted 10 | `[10, None, None, None, None]` | 0 | 1 | 1 |
| 2 | Enqueue 20 | Inserted 20 | `[10, 20, None, None, None]` | 0 | 2 | 2 |
| 3 | Enqueue 30 | Inserted 30 | `[10, 20, 30, None, None]` | 0 | 3 | 3 |
| 4 | Dequeue | Removed 10 | `[None, 20, 30, None, None]` | 1 | 3 | 2 |
| 5 | Enqueue 40 | Inserted 40 | `[None, 20, 30, 40, None]` | 1 | 4 | 3 |
| 6 | Enqueue 50 | Inserted 50 | `[None, 20, 30, 40, 50]` | 1 | 0 | 4 |
| 7 | Enqueue 60 | Inserted 60 | `[60, 20, 30, 40, 50]` | 1 | 1 | 5 |
| 8 | Dequeue | Removed 20 | `[60, None, 30, 40, 50]` | 2 | 1 | 4 |
| 9 | Enqueue 70 | Inserted 70 | `[60, 70, 30, 40, 50]` | 2 | 2 | 5 |
| 10 | Dequeue | Removed 30 | `[60, 70, None, 40, 50]` | 3 | 2 | 4 |

### Analysis

The results show that the circular queue successfully inserts and removes elements while maintaining the FIFO principle.

When the tail reaches the last array position, it wraps around to index zero. The program also reuses empty positions after dequeue operations. These operations demonstrate how a circular queue manages a fixed-size array efficiently.

### Question 2: Explain the purpose of using the modulo (%) operator in index calculations.

The modulo (%) operator calculates the remainder after division. In a circular queue, it is used to move the head and tail indices forward while keeping them within the array boundaries.

For example, if the queue capacity is five:

- `(0 + 1) % 5 = 1`
- `(3 + 1) % 5 = 4`
- `(4 + 1) % 5 = 0`

When the index reaches the last position, the modulo operation returns it to index zero.

The expression used in the program is:

`(self.tail + 1) % self.capacity`

A similar expression is used to update the head after removing an element.

Without modulo arithmetic, the indices could move beyond the valid array positions. Therefore, the modulo operator allows the queue to wrap around and reuse available positions.

## 8. Conclusion

In this laboratory activity, I successfully implemented a circular queue buffer using Python. I learned how to perform enqueue and dequeue operations while following the First-In, First-Out (FIFO) principle.

I also learned how to handle overflow and underflow conditions and how the modulo operator keeps the head and tail indices within the valid array boundaries. The 10-operation trace demonstrated how a circular queue wraps around and reuses empty positions in a fixed-size array.

Overall, this activity improved my understanding of circular queue implementation, index management, and efficient memory utilization in data structures.