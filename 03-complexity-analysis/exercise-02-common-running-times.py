"""
Exercise 2: Common Running Times
Demonstrates algorithms with different common running times
"""

import time
import random
import math


def constant_time(n):
    """O(1) - Constant time"""
    return n % 2 == 0


def logarithmic_time(n, target):
    """O(log n) - Logarithmic time (binary search)"""
    arr = list(range(n))
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


def linear_time(n):
    """O(n) - Linear time"""
    total = 0
    for i in range(n):
        total += i
    return total


def linearithmic_time(n):
    """O(n log n) - Linearithmic time (merge sort)"""
    arr = list(range(n))
    random.shuffle(arr)
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
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
    
    return merge_sort(arr)


def quadratic_time(n):
    """O(n²) - Quadratic time"""
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i < j:
                count += 1
    return count


def cubic_time(n):
    """O(n³) - Cubic time"""
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count


def exponential_time(n):
    """O(2^n) - Exponential time (recursive Fibonacci)"""
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    return fib(n)


def factorial_time(n):
    """O(n!) - Factorial time (generating all permutations)"""
    from itertools import permutations
    perms = list(permutations(range(min(n, 8))))  # Limit to avoid overflow
    return len(perms)


def measure_time(func, *args):
    """Measure execution time of a function"""
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, (end - start) * 1000  # Return time in milliseconds


def demonstrate_running_times():
    """Demonstrate different running times with various input sizes"""
    print("=" * 70)
    print("Common Running Times Demonstration")
    print("=" * 70)
    
    test_cases = [
        ("O(1) - Constant", constant_time, [100, 1000, 10000, 100000]),
        ("O(log n) - Logarithmic", lambda n: logarithmic_time(n, n//2), [100, 1000, 10000, 100000]),
        ("O(n) - Linear", linear_time, [100, 1000, 10000, 100000]),
        ("O(n log n) - Linearithmic", linearithmic_time, [100, 1000, 10000]),
        ("O(n²) - Quadratic", quadratic_time, [100, 1000, 5000]),
        ("O(n³) - Cubic", cubic_time, [10, 50, 100]),
        ("O(2^n) - Exponential", exponential_time, [10, 20, 30]),
        ("O(n!) - Factorial", factorial_time, [5, 6, 7, 8]),
    ]
    
    for name, func, sizes in test_cases:
        print(f"\n{name}")
        print("-" * 70)
        print(f"{'Input Size':<15} {'Time (ms)':<15} {'Result':<20}")
        print("-" * 70)
        
        for size in sizes:
            try:
                result, time_taken = measure_time(func, size)
                if time_taken < 0.001:
                    time_str = f"{time_taken*1000:.3f} μs"
                else:
                    time_str = f"{time_taken:.3f} ms"
                print(f"{size:<15} {time_str:<15} {str(result)[:20]:<20}")
            except Exception as e:
                print(f"{size:<15} {'Error':<15} {str(e)[:20]:<20}")
    
    print("\n" + "=" * 70)
    print("Key Observations:")
    print("=" * 70)
    print("1. Constant time O(1) is independent of input size")
    print("2. Logarithmic time O(log n) grows very slowly")
    print("3. Linear time O(n) grows proportionally with input")
    print("4. Linearithmic O(n log n) is common in efficient sorting")
    print("5. Quadratic O(n²) becomes slow for large inputs")
    print("6. Cubic O(n³) and above are often impractical")
    print("7. Exponential O(2^n) and factorial O(n!) are intractable")


if __name__ == "__main__":
    demonstrate_running_times()
