"""
Exercise 1: Understanding Time Complexity
Demonstrates different time complexities with practical examples
"""

import time
import random


def constant_time_example(arr):
    """
    O(1) - Constant Time
    Accessing an element by index takes constant time
    """
    if len(arr) > 0:
        return arr[0]
    return None


def linear_time_example(arr, target):
    """
    O(n) - Linear Time
    Searching through an array linearly
    """
    for element in arr:
        if element == target:
            return True
    return False


def quadratic_time_example(arr):
    """
    O(n²) - Quadratic Time
    Nested loops - comparing every element with every other element
    """
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
    return count


def logarithmic_time_example(arr, target):
    """
    O(log n) - Logarithmic Time
    Binary search on a sorted array
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linearithmic_time_example(arr):
    """
    O(n log n) - Linearithmic Time
    Merge sort algorithm
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = linearithmic_time_example(arr[:mid])
    right = linearithmic_time_example(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def measure_time(func, *args):
    """Measure execution time of a function"""
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, (end - start) * 1000  # Return time in milliseconds


def demonstrate_complexities():
    """Demonstrate different time complexities with various input sizes"""
    print("=" * 60)
    print("Time Complexity Demonstration")
    print("=" * 60)

    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"\nInput size: {size}")
        print("-" * 60)

        # Generate test data
        arr = list(range(size))
        random.shuffle(arr)
        sorted_arr = sorted(arr)
        target = random.choice(arr)

        # O(1) - Constant
        _, time_taken = measure_time(constant_time_example, arr)
        print(f"O(1) - Constant time:        {time_taken:.6f} ms")

        # O(log n) - Logarithmic
        _, time_taken = measure_time(
            logarithmic_time_example, sorted_arr, target)
        print(f"O(log n) - Logarithmic:      {time_taken:.6f} ms")

        # O(n) - Linear
        _, time_taken = measure_time(linear_time_example, arr, target)
        print(f"O(n) - Linear:                {time_taken:.6f} ms")

        # O(n log n) - Linearithmic
        _, time_taken = measure_time(linearithmic_time_example, arr.copy())
        print(f"O(n log n) - Linearithmic:    {time_taken:.6f} ms")

        # O(n²) - Quadratic (only for smaller sizes)
        if size <= 1000:
            _, time_taken = measure_time(quadratic_time_example, arr)
            print(f"O(n²) - Quadratic:            {time_taken:.6f} ms")


if __name__ == "__main__":
    demonstrate_complexities()
