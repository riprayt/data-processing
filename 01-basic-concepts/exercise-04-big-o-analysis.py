"""
Exercise 4: Big-O Analysis Practice
Analyze code snippets and determine their time/space complexity
"""


def example_1(n):
    """
    Analyze this function's time and space complexity
    """
    total = 0
    for i in range(n):
        total += i
    return total
# Answer: Time O(n), Space O(1)


def example_2(n):
    """
    Analyze this function's time and space complexity
    """
    result = []
    for i in range(n):
        result.append(i * 2)
    return result
# Answer: Time O(n), Space O(n)


def example_3(n):
    """
    Analyze this function's time and space complexity
    """
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total
# Answer: Time O(n²), Space O(1)


def example_4(n):
    """
    Analyze this function's time and space complexity
    """
    if n <= 1:
        return n
    return example_4(n - 1) + example_4(n - 2)
# Answer: Time O(2^n), Space O(n) - This is naive Fibonacci


def example_5(arr, target):
    """
    Analyze this function's time and space complexity
    Assumes arr is sorted
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
# Answer: Time O(log n), Space O(1)


def example_6(n):
    """
    Analyze this function's time and space complexity
    """
    if n <= 0:
        return 0
    return n + example_6(n - 1)
# Answer: Time O(n), Space O(n) - due to recursion stack


def example_7(arr):
    """
    Analyze this function's time and space complexity
    """
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(i, n):
            result.append(arr[i:j+1])
    return result
# Answer: Time O(n³), Space O(n³) - generates all subarrays


def demonstrate_analysis():
    """Demonstrate Big-O analysis with examples"""
    print("=" * 60)
    print("Big-O Analysis Practice")
    print("=" * 60)

    examples = [
        ("example_1", "Single loop", "O(n) time, O(1) space"),
        ("example_2", "Single loop with list", "O(n) time, O(n) space"),
        ("example_3", "Nested loops", "O(n²) time, O(1) space"),
        ("example_4", "Recursive (naive Fibonacci)", "O(2^n) time, O(n) space"),
        ("example_5", "Binary search", "O(log n) time, O(1) space"),
        ("example_6", "Linear recursion", "O(n) time, O(n) space"),
        ("example_7", "Nested loops with slicing", "O(n³) time, O(n³) space"),
    ]

    print("\nComplexity Analysis Summary:")
    print("-" * 60)
    for func_name, description, complexity in examples:
        print(f"{func_name:20s} - {description:30s}: {complexity}")


if __name__ == "__main__":
    demonstrate_analysis()
