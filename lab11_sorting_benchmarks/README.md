# Laboratory Activity No. 11: Sorting Algorithms and Performance Benchmarks

**Student Name:** Mary Jane Y. Reyna  
**Course:** CPEPRO8L – Data Structures and Algorithms  
**Semester:** First Semester, AY 2026–2027

## I. Objectives

1. Implement six sorting algorithms: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.
2. Test sorting correctness using empty, single-item, duplicate, sorted, reverse-sorted, and random datasets.
3. Measure and compare execution time across different input sizes and data distributions.
4. Compare the performance and complexity of the sorting algorithms.
5. Generate benchmark results and a chart to analyze sorting performance.

## II. Tools and Environment

- Python 3.11 or later
- Visual Studio Code
- Windows operating system
- Python standard library

## III. Project Files

```text
lab11_sorting_benchmarks/
│
├── sorting_algorithms.py
├── test_sorts.py
├── benchmark_sorts.py
├── README.md
│
└── results/
    ├── benchmark_results.csv
    └── sorting_runtime_chart.svg
```

### Description of Files

- **sorting_algorithms.py** – Contains the six sorting algorithm implementations and displays their sorted results.
- **test_sorts.py** – Tests the correctness of the sorting algorithms using different datasets.
- **benchmark_sorts.py** – Measures execution time and generates benchmark results and a chart.
- **README.md** – Documents the objectives, execution instructions, results, and analysis.
- **benchmark_results.csv** – Stores the measured benchmark data.
- **sorting_runtime_chart.svg** – Displays a comparison of sorting runtime.

## IV. How to Run the Program

Open the project folder in Visual Studio Code and open the integrated terminal.

### Step 1: Run the Sorting Algorithms

```bash
python sorting_algorithms.py
```

On Windows, you can also use:

```powershell
py sorting_algorithms.py
```

### Step 2: Run the Correctness Tests

```bash
py test_sorts.py
```

### Step 3: Run the Benchmarks

```bash
py benchmark_sorts.py
```

After the benchmark finishes successfully, the CSV results and chart should be saved inside the `results` folder.

**Note:** The testing and benchmark files must use the same function return format as `sorting_algorithms.py`. The current standalone sorting version returns only the sorted list, so the earlier testing and benchmark scripts must be adjusted to match before running them.

## V. Sorting Algorithms Implemented

### 1. Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order. It can stop early if no swaps occur during a pass.

### 2. Selection Sort

Selection Sort searches for the smallest remaining element and places it in its correct position.

### 3. Insertion Sort

Insertion Sort builds a sorted portion of the list by inserting each new element into its proper position.

### 4. Merge Sort

Merge Sort divides the list into smaller parts, sorts them recursively, and merges the sorted parts.

### 5. Quick Sort

Quick Sort partitions the list around a pivot. This implementation uses the last element as the pivot.

### 6. Heap Sort

Heap Sort builds a max heap and repeatedly moves the largest element to the end of the list.

## VI. Expected Sorting Output

For the input list:

```text
[64, 25, 12, 22, 11, 25, 5]
```

The expected output is:

```text
SORTING ALGORITHMS RESULTS
Original list: [64, 25, 12, 22, 11, 25, 5]

Bubble Sort: [5, 11, 12, 22, 25, 25, 64]
Selection Sort: [5, 11, 12, 22, 25, 25, 64]
Insertion Sort: [5, 11, 12, 22, 25, 25, 64]
Merge Sort: [5, 11, 12, 22, 25, 25, 64]
Quick Sort: [5, 11, 12, 22, 25, 25, 64]
Heap Sort: [5, 11, 12, 22, 25, 25, 64]
```

All six algorithms should produce the same ascending order while preserving duplicate values.

## VII. Time and Space Complexity

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |

Merge Sort requires additional memory for merging. Heap Sort uses constant auxiliary array space in this implementation. Quick Sort also requires recursion-stack memory.

## VIII. Benchmarking Methodology

The laboratory benchmark is designed to compare the algorithms using input sizes of 100, 300, and 600 elements.

The datasets include:

- Random values
- Already sorted values
- Reverse-sorted values
- Duplicate-heavy values

Each algorithm and dataset condition should be measured over three trials. The median execution time is used to reduce the effect of unusually high or low measurements.

The benchmark results should be saved in CSV format, and a chart should compare runtime growth.

## IX. Guide Questions and Answers

### 1. Which elementary algorithm benefited most from already sorted data, and why?

Insertion Sort benefits from already sorted data because each element is already in its correct position. It performs fewer comparisons and does not need to shift elements, giving it a best-case time complexity of O(n).

### 2. How did the Quick Sort pivot strategy affect sorted or duplicate-heavy data?

The implementation uses the last element as the pivot. Sorted and reverse-sorted lists can produce unbalanced partitions, causing Quick Sort to approach O(n²) time. Duplicate-heavy data can also affect partition balance.

### 3. Why is median runtime preferable to a single timing result?

Median runtime reduces the influence of unusually fast or slow trials caused by background processes and other system activity. It gives a more representative measurement.

### 4. What memory trade-off does Merge Sort make compared with in-place alternatives?

Merge Sort uses additional memory to create and merge temporary lists. In exchange, it provides predictable O(n log n) time complexity. Heap Sort uses less auxiliary array memory.

### 5. When might an O(n²) algorithm still be reasonable?

An O(n²) algorithm can be appropriate for small datasets, educational exercises, or nearly sorted data when using Insertion Sort. For small inputs, its simplicity can make it practical.

### 6. Which measured result differed most from the theoretical expectation, and what likely caused it?

This answer should be finalized after examining the actual benchmark measurements. One possible observation is that Quick Sort performs poorly on sorted data because its last-element pivot creates unbalanced partitions. The CSV results should be checked before identifying this as the actual finding.

## X. Conclusion

This laboratory activity demonstrates the implementation and comparison of six sorting algorithms. Each algorithm uses a different strategy to arrange data in ascending order.

Theoretical analysis shows that Bubble Sort, Selection Sort, and Insertion Sort can require quadratic time, while Merge Sort and Heap Sort provide O(n log n) time complexity. Quick Sort is often efficient but can be affected by its pivot selection.

Testing and benchmarking help verify correctness and show how input size and data distribution influence performance. The generated CSV file and chart provide evidence for analyzing the differences between algorithms.

