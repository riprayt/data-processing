"""
Exercise 2: Understanding Space Complexity
Demonstrates different space complexities with practical examples
"""

import sys


def constant_space_example(n):
    """
    O(1) - Constant Space
    Uses a fixed amount of memory regardless of input size
    """
    total = 0
    for i in range(n):
        total += i
    return total


def linear_space_example(n):
    """
    O(n) - Linear Space
    Creates an array of size n
    """
    arr = [0] * n
    for i in range(n):
        arr[i] = i * 2
    return arr


def quadratic_space_example(n):
    """
    O(n²) - Quadratic Space
    Creates a 2D matrix of size n x n
    """
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = i * j
    return matrix


def recursive_space_example(n):
    """
    O(n) - Linear Space (due to recursion stack)
    Each recursive call adds to the call stack
    """
    if n <= 0:
        return 0
    return n + recursive_space_example(n - 1)


def tail_recursive_space_example(n, accumulator=0):
    """
    O(1) - Constant Space (with tail recursion optimization)
    Note: Python doesn't optimize tail recursion,
    but this demonstrates the concept
    """
    if n <= 0:
        return accumulator
    return tail_recursive_space_example(n - 1, accumulator + n)


def get_size(obj):
    """Get approximate size of an object in bytes"""
    return sys.getsizeof(obj)


def demonstrate_space_complexities():
    """Demonstrate different space complexities"""
    print("=" * 60)
    print("Space Complexity Demonstration")
    print("=" * 60)

    sizes = [10, 100, 1000]

    for size in sizes:
        print(f"\nInput size: {size}")
        print("-" * 60)

        # O(1) - Constant
        result = constant_space_example(size)
        mem_size = get_size(result)
        print(f"O(1) - Constant space:        "
              f"Result = {result}, Memory = {mem_size} bytes")

        # O(n) - Linear
        result = linear_space_example(size)
        mem_size = get_size(result)
        print(f"O(n) - Linear space:          "
              f"Array size = {len(result)}, Memory ≈ {mem_size} bytes")

        # O(n) - Recursive (stack space)
        result = recursive_space_example(size)
        print(f"O(n) - Recursive (stack):      Result = {result}")

        # O(n²) - Quadratic (only for smaller sizes)
        if size <= 100:
            result = quadratic_space_example(size)
            mem_size = get_size(result)
            matrix_size = f"{len(result)}x{len(result[0])}"
            print(f"O(n²) - Quadratic space:       "
                  f"Matrix size = {matrix_size}, Memory ≈ {mem_size} bytes")


if __name__ == "__main__":
    demonstrate_space_complexities()
