
"""Benchmark sorting algorithms and save CSV results and an SVG chart."""

import copy
import csv
import random
import statistics
import time
from pathlib import Path

from sorting_algorithms import SORTS


OUTPUT_DIR = Path("results")
SIZES = [100, 300, 600]
TRIALS = 3
RANDOM_SEED = 42


def make_datasets(size, seed):
    rng = random.Random(seed)
    random_data = [rng.randint(0, size * 10) for _ in range(size)]

    return {
        "random": random_data,
        "sorted": sorted(random_data),
        "reverse": sorted(random_data, reverse=True),
        "duplicate-heavy": [rng.randint(0, 9) for _ in range(size)],
    }


def create_svg_chart(rows, filename):
    """Create a simple SVG line chart using Python's standard library."""
    algorithms = list(SORTS.keys())
    sizes = sorted({int(row["size"]) for row in rows})
    if not sizes:
        return

    width, height = 900, 520
    left, right, top, bottom = 100, 30, 55, 90
    plot_w = width - left - right
    plot_h = height - top - bottom

    # Use random-input median runtimes for the comparison chart.
    values = {}
    for row in rows:
        if row["distribution"] == "random":
            values[(row["algorithm"], int(row["size"]))] = float(
                row["median_seconds"]
            )

    max_time = max(values.values(), default=0.000001) or 0.000001
    max_time *= 1.10

    palette = [
        "#2563eb", "#dc2626", "#16a34a",
        "#9333ea", "#ea580c", "#0891b2"
    ]

    def x_pos(index):
        if len(sizes) == 1:
            return left + plot_w / 2
        return left + index * plot_w / (len(sizes) - 1)

    def y_pos(value):
        return top + plot_h - (value / max_time) * plot_h

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="450" y="28" text-anchor="middle" '
        'font-size="20" font-family="Arial">Sorting Runtime Comparison '
        '(Random Data)</text>',
    ]

    # Horizontal grid lines and labels.
    for i in range(6):
        value = max_time * i / 5
        y = y_pos(value)
        svg.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" '
            f'y2="{y:.1f}" stroke="#dddddd"/>'
        )
        svg.append(
            f'<text x="{left-10}" y="{y+4:.1f}" text-anchor="end" '
            f'font-size="11" font-family="Arial">{value:.5f}</text>'
        )

    for i, size in enumerate(sizes):
        x = x_pos(i)
        svg.append(
            f'<text x="{x:.1f}" y="{height-bottom+25}" '
            f'text-anchor="middle" font-size="12" '
            f'font-family="Arial">{size}</text>'
        )

    svg.append(
        f'<text x="{left + plot_w/2}" y="{height-20}" '
        'text-anchor="middle" font-size="13" font-family="Arial">'
        'Input size</text>'
    )
    svg.append(
        f'<text x="22" y="{top + plot_h/2}" '
        'transform="rotate(-90 22 '
        f'{top + plot_h/2})" text-anchor="middle" '
        'font-size="13" font-family="Arial">Median runtime (seconds)</text>'
    )

    for alg_index, algorithm in enumerate(algorithms):
        points = []
        for i, size in enumerate(sizes):
            value = values.get((algorithm, size), 0)
            points.append((x_pos(i), y_pos(value)))

        coords = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        color = palette[alg_index % len(palette)]
        svg.append(
            f'<polyline points="{coords}" fill="none" stroke="{color}" '
            'stroke-width="2.5"/>'
        )

        for x, y in points:
            svg.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{color}"/>'
            )

        legend_x = left + (alg_index % 3) * 245
        legend_y = height - 55 + (alg_index // 3) * 22
        svg.append(
            f'<line x1="{legend_x}" y1="{legend_y}" '
            f'x2="{legend_x+22}" y2="{legend_y}" '
            f'stroke="{color}" stroke-width="3"/>'
        )
        svg.append(
            f'<text x="{legend_x+28}" y="{legend_y+4}" '
            f'font-size="12" font-family="Arial">{algorithm}</text>'
        )

    svg.append("</svg>")
    filename.write_text("\n".join(svg), encoding="utf-8")


def run_benchmarks():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    print("SORTING ALGORITHM BENCHMARK")
    print(f"Input sizes: {SIZES} | Trials per condition: {TRIALS}\n")

    for size in SIZES:
        datasets = make_datasets(size, RANDOM_SEED + size)

        for distribution, source_data in datasets.items():
            for algorithm_name, algorithm in SORTS.items():
                timings = []
                final_comparisons = 0
                final_movements = 0

                for _ in range(TRIALS):
                    # Copy before starting the timer to exclude setup work.
                    working_data = copy.copy(source_data)

                    start = time.perf_counter()
                    result, comparisons, movements = algorithm(working_data)
                    elapsed = time.perf_counter() - start

                    assert result == sorted(source_data), (
                        f"Incorrect output from {algorithm_name}"
                    )

                    timings.append(elapsed)
                    final_comparisons = comparisons
                    final_movements = movements

                median_time = statistics.median(timings)
                row = {
                    "algorithm": algorithm_name,
                    "size": size,
                    "distribution": distribution,
                    "trials": TRIALS,
                    "median_seconds": f"{median_time:.8f}",
                    "comparisons": final_comparisons,
                    "movements": final_movements,
                }
                results.append(row)

                print(
                    f"{algorithm_name:16} | n={size:4} | "
                    f"{distribution:15} | median={median_time:.8f}s"
                )

    csv_path = OUTPUT_DIR / "benchmark_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    chart_path = OUTPUT_DIR / "sorting_runtime_chart.svg"
    create_svg_chart(results, chart_path)

    print(f"\nCSV saved to: {csv_path}")
    print(f"Chart saved to: {chart_path}")
    print(f"Total benchmark conditions: {len(results)}")


if __name__ == "__main__":
    run_benchmarks()
