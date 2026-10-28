
"""Correctness tests for all six sorting algorithms."""

import random
from sorting_algorithms import SORTS


def run_tests():
    rng = random.Random(42)

    datasets = {
        "empty": [],
        "one item": [7],
        "duplicates": [4, 2, 4, 1, 2, 1, 4],
        "already sorted": [1, 2, 3, 4, 5],
        "reverse sorted": [5, 4, 3, 2, 1],
        "random": [rng.randint(-100, 100) for _ in range(30)],
    }

    total = 0

    for algorithm_name, algorithm in SORTS.items():
        for dataset_name, data in datasets.items():
            result, comparisons, movements = algorithm(data)

            # Independent correctness reference for testing.
            expected = sorted(data)

            assert result == expected, (
                f"{algorithm_name} failed on {dataset_name}"
            )
            assert data == datasets[dataset_name], (
                f"{algorithm_name} changed the original input"
            )

            total += 1
            print(
                f"PASS: {algorithm_name} - {dataset_name} "
                f"(comparisons={comparisons}, movements={movements})"
            )

    print(f"\nAll tests passed: {total} checks.")


if __name__ == "__main__":
    run_tests()
