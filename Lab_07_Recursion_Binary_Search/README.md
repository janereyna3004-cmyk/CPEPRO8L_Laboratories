# Laboratory Activity No. 7
## Recursion Tracing & Binary Search

**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

---

## 1. Introduction

Recursion is a programming technique in which a function calls itself to solve a problem by breaking it down into smaller subproblems. Each recursive call creates a new stack frame that stores the function's arguments and local execution information.

Binary Search is an efficient searching algorithm that finds a target element in a sorted array by repeatedly dividing the search range into two halves.

In this laboratory activity, a recursive Binary Search algorithm is implemented in Python. The program demonstrates recursive function calls, base cases, call nesting, and the differences between iterative and recursive approaches in terms of space complexity.

## 2. Objectives

The objectives of this laboratory activity are:

1. To understand recursive execution, base cases, and nested function calls.
2. To implement and test Recursive Binary Search using Python.
3. To trace the execution stack when searching for a target value.
4. To understand why base cases are necessary to prevent infinite recursion and stack overflow errors.
5. To compare the space complexity of iterative and recursive Binary Search.

## 3. Requirements

- Python 3
- Visual Studio Code (VS Code)
- A computer capable of running Python programs

## 4. Source Code

The Python source code is saved as:

`lab7_recursive_search.py`

The program implements the `recursive_binary_search()` function, which accepts a sorted array, a lower index, an upper index, and a target value.

The function follows these steps:

1. Checks whether `low > high`. If true, the target does not exist in the current search range, so the function returns `-1`.
2. Calculates the middle index using `(low + high) // 2`.
3. Compares the middle element with the target.
4. If the middle element equals the target, returns its index.
5. If the target is smaller, recursively searches the left half.
6. If the target is larger, recursively searches the right half.

The program tests three target values: `23`, `56`, and `100`.

## 5. Execution and Output

### How to Run the Program

1. Open Visual Studio Code.
2. Create a Python file named `lab7_recursive_search.py`.
3. Paste the complete Python source code into the file.
4. Save the file.
5. Open the VS Code terminal by selecting **Terminal → New Terminal**.
6. Run the following command:

```bash
python lab7_recursive_search.py
```

If the command does not work on Windows, try:

```bash
py lab7_recursive_search.py
```

### Expected Output

```text
LABORATORY ACTIVITY NO. 7
Recursion Tracing & Binary Search
----------------------------------------
Sorted Array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

Searching for 23:
Element found at index: 5

Searching for 56:
Element found at index: 7

Searching for 100:
Element not found.

Program completed successfully.
```

### Output Analysis

The program successfully searches for three different target values.

- **Target 23:** The algorithm finds the element at index `5`.
- **Target 56:** The algorithm finds the element at index `7`.
- **Target 100:** The algorithm returns `-1` because the target is not present in the array.

The results demonstrate that Recursive Binary Search can locate an existing element and correctly report when an element is absent.

**Note:** Python list indexing starts at zero, so the element at index `5` is the sixth element in the list.

## 6. Report Analysis Questions

### Question 1: Draw the execution stack trace diagram showing the arguments passed to each call when searching for 56.

The sorted array is:

```text
[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
```

The target value is `56`.

The recursive Binary Search begins with the following arguments:

```python
recursive_binary_search(data, 0, 9, 56)
```

**Step 1: First Function Call**

Arguments:

```text
low = 0
high = 9
target = 56
```

Calculate the middle index:

```text
mid = (0 + 9) // 2
mid = 4
```

The element at index `4` is `16`.

Since `56 > 16`, the algorithm searches the right half of the array.

The next recursive call is:

```python
recursive_binary_search(data, 5, 9, 56)
```

**Step 2: Second Function Call**

Arguments:

```text
low = 5
high = 9
target = 56
```

Calculate the middle index:

```text
mid = (5 + 9) // 2
mid = 7
```

The element at index `7` is `56`.

Since the middle element equals the target, the function returns index `7`.

**Execution Stack Trace Diagram**

```text
             RECURSIVE CALL STACK

       ┌───────────────────────────────┐
       │ Call 1                        │
       │ recursive_binary_search      │
       │ low = 0                       │
       │ high = 9                      │
       │ target = 56                  │
       │ mid = 4                       │
       │ arr[4] = 16                   │
       │ Search the right half         │
       └──────────────┬────────────────┘
                      │
                      ▼
       ┌───────────────────────────────┐
       │ Call 2                        │
       │ recursive_binary_search      │
       │ low = 5                       │
       │ high = 9                      │
       │ target = 56                  │
       │ mid = 7                       │
       │ arr[7] = 56                   │
       │ Target found!                 │
       │ Return index 7                │
       └──────────────┬────────────────┘
                      │
                      ▼
       ┌───────────────────────────────┐
       │ Return 7 to Call 1            │
       │ Return 7 to the main program  │
       └───────────────────────────────┘
```

**Explanation:**

The first function call examines the middle element, `16`. Because the target value `56` is greater than `16`, the algorithm eliminates the left half of the search range and recursively searches indices `5` through `9`.

The second function call examines index `7`, where the value is `56`. The target is found, so the function returns `7`. The result is passed back through the recursive calls to the main program.

This example demonstrates how recursive Binary Search reduces the search range with each function call.

### Question 2: Discuss why missing base cases lead to stack overflow errors.

A base case is a condition that stops a recursive function from calling itself again. It is essential because it provides a termination condition for recursion.

In Recursive Binary Search, the base case is:

```python
if low > high:
    return -1
```

This condition means that the search range is empty and the target cannot be found. The function returns `-1` instead of making another recursive call.

Without a proper base case, a recursive function may continue calling itself indefinitely. Each call adds another stack frame to the program's call stack. As the number of calls increases, the program consumes more memory.

Eventually, Python may raise a `RecursionError` when the maximum recursion depth is exceeded. In other programming environments, excessive recursion may result in a stack overflow.

For example, if Recursive Binary Search does not check whether `low > high`, it may continue making recursive calls even when the search range is empty.

Therefore, a correct base case is necessary to ensure that recursion terminates properly, prevents unnecessary function calls, and allows the program to handle unsuccessful searches safely.

## 7. Comparison of Iterative and Recursive Binary Search

| Feature | Iterative Binary Search | Recursive Binary Search |
|---|---|---|
| Implementation | Uses a loop. | Uses a function that calls itself. |
| Search method | Repeatedly divides the search range. | Repeatedly divides the search range through recursive calls. |
| Time complexity, best case | O(1) | O(1) |
| Time complexity, average case | O(log n) | O(log n) |
| Time complexity, worst case | O(log n) | O(log n) |
| Auxiliary space complexity | O(1) | O(log n) |
| Memory usage | Generally lower because it does not create recursive call frames. | Uses additional memory for recursive call frames. |
| Termination | Controlled by the loop condition. | Controlled by the base case. |

### Discussion

Both iterative and recursive Binary Search use the sorted order of the array to eliminate approximately half of the remaining search range at each step. Consequently, both have a worst-case time complexity of O(log n).

However, they differ in auxiliary space complexity.

Iterative Binary Search uses O(1) auxiliary space because it maintains a fixed number of variables while searching.

Recursive Binary Search uses O(log n) auxiliary space in the worst case because each recursive call creates a stack frame. The number of recursive calls grows logarithmically with the size of the search array.

Although recursive Binary Search can be easier to understand when studying recursion, the iterative approach generally uses less additional memory.

## 8. Conclusion

In this laboratory activity, Recursive Binary Search was successfully implemented and tested using Python. The program demonstrated how recursion can be used to search for a target value in a sorted array by repeatedly dividing the search range into smaller portions.

The tests confirmed that the program correctly found `23` at index `5` and `56` at index `7`, while returning `-1` when searching for `100`, which is not present in the array.

The execution stack trace for searching for `56` showed how the recursive function narrowed the search range from indices `0–9` to indices `5–9` before locating the target at index `7`. This illustrated how recursive calls are created and how their return values are passed back to the calling functions.

The activity also demonstrated the importance of base cases in recursive algorithms. Without a proper termination condition, recursive calls may continue until Python raises a `RecursionError`.

Finally, comparing iterative and recursive Binary Search showed that both methods have O(log n) worst-case time complexity, but their auxiliary space complexities differ. Iterative Binary Search requires O(1) auxiliary space, whereas Recursive Binary Search requires O(log n) auxiliary space.

Overall, this activity improved my understanding of recursive function calls, call stack execution, base cases, binary searching, and algorithmic complexity. These concepts are important for developing efficient and reliable programs using data structures and algorithms.