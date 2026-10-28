# Laboratory Activity No. 7
# Title: Recursion Tracing & Binary Search
# Course Code: CPEPRO8L
# Course Title: Data Structures and Algorithms
# Term: First Semester, AY 2026-2027

def recursive_binary_search(arr, low, high, target):
    """
    Search for a target value in a sorted array using recursion.

    Parameters:
        arr: Sorted list of elements.
        low: Starting index of the search range.
        high: Ending index of the search range.
        target: Value to search for.

    Returns:
        The index of the target if found; otherwise, -1.
    """

    # Base case: The target is not in the array.
    if low > high:
        return -1

    # Find the middle index.
    mid = (low + high) // 2

    # Check whether the middle element is the target.
    if arr[mid] == target:
        return mid

    # Search the left half if the target is smaller.
    elif arr[mid] > target:
        return recursive_binary_search(arr, low, mid - 1, target)

    # Search the right half if the target is larger.
    else:
        return recursive_binary_search(arr, mid + 1, high, target)


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    print("LABORATORY ACTIVITY NO. 7")
    print("Recursion Tracing & Binary Search")
    print("-" * 40)

    print("Sorted Array:", data)

    # Test 1: Search for 23.
    target_val = 23
    result = recursive_binary_search(
        data, 0, len(data) - 1, target_val
    )

    print(f"\nSearching for {target_val}:")
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found.")

    # Test 2: Search for 56.
    target_val = 56
    result = recursive_binary_search(
        data, 0, len(data) - 1, target_val
    )

    print(f"\nSearching for {target_val}:")
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found.")

    # Test 3: Search for a value that is not in the array.
    target_val = 100
    result = recursive_binary_search(
        data, 0, len(data) - 1, target_val
    )

    print(f"\nSearching for {target_val}:")
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found.")

    print("\nProgram completed successfully.")