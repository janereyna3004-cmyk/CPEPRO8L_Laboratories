# Laboratory Activity No. 1
## Python Object References and Asymptotic Complexity Profiling

**Course Code:** CPEPRO8L  
**Student Name:** MARY JANE Y. REYNA  
**Date Completed:** OCTOBER 26,2026

### 1. Objectives
- Differentiate between mutable and immutable object references using `id()`.
- Demonstrate how variable assignment copies references, not data.
- Measure execution time using Python's `time` module.
- Compare O(1), O(n), and O(n²) time complexity.

### 2. Source Code
- `task1_references.py`
- `task2_profiling.py`

### 3. Execution Results
Task 1 successfully executed. Both `list_a` and `list_b` initially had the same object ID. After appending `40` to `list_b`, both variables displayed `[10, 20, 30, 40]`.

### 4. Analysis

**Question 1: Why did the value of `list_a` change when you appended a number to `list_b`?**

**Answer:** When `list_b = list_a` is executed, both variables refer to the same list object. Therefore, appending `40` through `list_b` changes the shared list, which is also reflected in `list_a`.

**Question 2: What happens to the memory reference if you assign a new list to `list_b` using `list_b = [100, 200]`? Explain using the output of `id()`.**

**Answer:** Assigning `[100, 200]` to `list_b` makes it refer to a new list object. The ID of `list_b` will differ from the ID of `list_a`, while `list_a` retains the original list `[10, 20, 30, 40]`. The two variables no longer refer to the same object.

### Task 2: Execution Results

The `task2_profiling.py` program successfully executed and measured the execution time of O(1), O(n), and O(n²) functions using Python's `time.perf_counter()`.

The benchmark results showed that constant-time operations remained relatively stable as the input size increased. Linear-time operations generally took longer as the input size increased. Quadratic-time operations showed a significant increase in execution time, especially at N = 5000. The quadratic operation was skipped at N = 10000 to avoid excessive execution time.

| Input Size (N) | O(1) (µs) | O(n) (µs) | O(n²) (µs) |
|---:|---:|---:|---:|
| 100 | 3.90 | 8.70 | 928.00 |
| 500 | 4.30 | 21.30 | 18,461.80 |
| 1,000 | 2.20 | 24.20 | 72,045.50 |
| 5,000 | 2.40 | 125.40 | 2,025,367.70 |
| 10,000 | 3.60 | 237.30 | Skipped |
*Note: µs = microseconds.*

### Task 2: Analysis

**Question 1: Which function was the fastest, and why?**

**Answer:** The O(1) constant-time function was the fastest because it accesses only the first element of the list instead of processing every element.

**Question 2: How did the execution time of the O(n) function change as N increased?**

**Answer:** The execution time generally increased as N increased because the function processes each element in the list.

**Question 3: Why did the O(n²) function take much longer for larger input sizes?**

**Answer:** The O(n²) function uses two nested loops. As the input size increases, the number of operations grows rapidly, causing the execution time to increase significantly.

**Question 4: Why was the quadratic function skipped at N = 10000?**

**Answer:** It was skipped to avoid excessive execution time because a quadratic algorithm performs approximately N × N operations.

### 5. Conclusion

This laboratory activity demonstrated how Python variables reference mutable objects and how assigning a new list changes a variable's reference. It also showed how execution time varies with algorithmic complexity. Constant-time operations remained relatively stable, linear-time operations generally increased with input size, and quadratic-time operations became significantly slower for larger inputs.