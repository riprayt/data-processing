"""
Exercise 3: Algorithm Comparison
Compare different approaches to the same problem and analyze their efficiency
"""

import time
import random


def find_max_naive(arr):
    """
    O(n) - Linear time, O(1) space
    Simple linear search for maximum
    """
    if not arr:
        return None

    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def find_max_builtin(arr):
    """
    O(n) - Linear time, O(1) space
    Using Python's built-in max function
    """
    return max(arr) if arr else None


def find_max_recursive(arr, index=0, max_val=None):
    """
    O(n) - Linear time, O(n) space (due to recursion stack)
    Recursive approach to find maximum
    """
    if not arr:
        return None

    if index == len(arr):
        return max_val

    if max_val is None or arr[index] > max_val:
        max_val = arr[index]

    return find_max_recursive(arr, index + 1, max_val)


def sum_array_iterative(arr):
    """
    O(n) - Linear time, O(1) space
    Iterative sum calculation
    """
    total = 0
    for num in arr:
        total += num
    return total


def sum_array_recursive(arr, index=0):
    """
    O(n) - Linear time, O(n) space (recursion stack)
    Recursive sum calculation
    """
    if index == len(arr):
        return 0
    return arr[index] + sum_array_recursive(arr, index + 1)


def contains_duplicate_naive(arr):
    """
    O(n²) - Quadratic time, O(1) space
    Naive approach: check every pair
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


def contains_duplicate_optimized(arr):
    """
    O(n) - Linear time, O(n) space
    Using a set for O(1) lookup
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


def measure_and_compare(func1, func2, name1, name2, test_data,
                        handle_errors=False):
    """Compare two functions and display results"""
    print(f"\nComparing {name1} vs {name2}")
    print("-" * 60)

    # Measure function 1
    try:
        start = time.perf_counter()
        result1 = func1(test_data)
        time1 = (time.perf_counter() - start) * 1000
        error1 = None
    except RecursionError:
        result1 = None
        time1 = None
        error1 = "RecursionError (max depth exceeded)"
    except Exception as e:
        result1 = None
        time1 = None
        error1 = f"Error: {type(e).__name__}"

    # Measure function 2
    try:
        start = time.perf_counter()
        result2 = func2(test_data)
        time2 = (time.perf_counter() - start) * 1000
        error2 = None
    except RecursionError:
        result2 = None
        time2 = None
        error2 = "RecursionError (max depth exceeded)"
    except Exception as e:
        result2 = None
        time2 = None
        error2 = f"Error: {type(e).__name__}"

    if error1:
        print(f"{name1:30s}: {error1}")
    else:
        print(f"{name1:30s}: {time1:10.6f} ms, Result: {result1}")

    if error2:
        print(f"{name2:30s}: {error2}")
    else:
        print(f"{name2:30s}: {time2:10.6f} ms, Result: {result2}")

    if error1 or error2:
        has_recursion_error = (
            "RecursionError" in (error1 or "") or
            "RecursionError" in (error2 or "")
        )
        if has_recursion_error:
            msg = "Note: Python's default recursion limit (~1000) exceeded."
            print(msg)
            print("      This demonstrates why iterative solutions are")
            print("      preferred for large inputs in Python.")
    elif result1 == result2:
        speedup = time1 / time2 if time2 > 0 else float('inf')
        print(f"Speedup: {speedup:.2f}x")
    else:
        print("WARNING: Results don't match!")


def demonstrate_algorithm_comparison():
    """Demonstrate comparing different algorithms"""
    print("=" * 60)
    print("Algorithm Comparison Demonstration")
    print("=" * 60)

    # Test data
    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"\n{'=' * 60}")
        print(f"Input size: {size}")
        print(f"{'=' * 60}")

        # Generate test data
        arr = [random.randint(1, 1000) for _ in range(size)]

        # Compare max finding algorithms
        measure_and_compare(
            find_max_naive, find_max_builtin,
            "Naive find_max", "Built-in max",
            arr
        )

        # Compare sum algorithms (only for smaller sizes due to recursion)
        # Python's default recursion limit is ~1000, so we limit to 500
        if size <= 500:
            measure_and_compare(
                sum_array_iterative, sum_array_recursive,
                "Iterative sum", "Recursive sum",
                arr, handle_errors=True
            )
        else:
            print("\nSkipping recursive sum comparison for large arrays")
            print("(Python recursion limit would be exceeded)")

        # Compare duplicate finding algorithms
        measure_and_compare(
            contains_duplicate_naive, contains_duplicate_optimized,
            "Naive duplicate check (O(n²))",
            "Optimized duplicate check (O(n))",
            arr
        )


if __name__ == "__main__":
    demonstrate_algorithm_comparison()
