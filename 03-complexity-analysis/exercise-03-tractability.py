"""
Exercise 3: Computational Tractability
Demonstrates the concept of tractable vs intractable problems
"""

import time
import random


def polynomial_time_algorithm(n):
    """
    Tractable: Polynomial time algorithm
    Time Complexity: O(n²)
    """
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def exponential_time_algorithm(n):
    """
    Intractable: Exponential time algorithm
    Time Complexity: O(2^n)
    """
    def recursive_count(n):
        if n <= 0:
            return 1
        return recursive_count(n - 1) + recursive_count(n - 1)
    return recursive_count(n)


def brute_force_subset_sum(numbers, target):
    """
    Intractable: Brute force subset sum problem
    Time Complexity: O(2^n) where n is the number of elements
    """
    from itertools import combinations
    
    for r in range(len(numbers) + 1):
        for combo in combinations(numbers, r):
            if sum(combo) == target:
                return combo
    return None


def efficient_subset_sum(numbers, target):
    """
    More efficient: Dynamic programming approach (pseudo-polynomial)
    Time Complexity: O(n * target)
    """
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in numbers:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    
    return dp[target]


def demonstrate_tractability():
    """Demonstrate tractable vs intractable problems"""
    print("=" * 70)
    print("Computational Tractability")
    print("=" * 70)
    print("\nTractable: Problems solvable in polynomial time O(n^k) for constant k")
    print("Intractable: Problems requiring exponential or worse time\n")
    
    # Test polynomial time
    print("1. Polynomial Time Algorithm (Tractable)")
    print("-" * 70)
    print(f"{'Input Size':<15} {'Time (ms)':<15} {'Scalable?':<15}")
    print("-" * 70)
    
    for n in [100, 500, 1000, 2000]:
        start = time.perf_counter()
        result = polynomial_time_algorithm(n)
        end = time.perf_counter()
        time_ms = (end - start) * 1000
        print(f"{n:<15} {time_ms:.3f} ms{'':<8} Yes")
    
    # Test exponential time
    print("\n2. Exponential Time Algorithm (Intractable)")
    print("-" * 70)
    print(f"{'Input Size':<15} {'Time (ms)':<15} {'Scalable?':<15}")
    print("-" * 70)
    
    for n in [10, 15, 20, 25]:
        start = time.perf_counter()
        try:
            result = exponential_time_algorithm(n)
            end = time.perf_counter()
            time_ms = (end - start) * 1000
            if time_ms > 1000:
                print(f"{n:<15} {time_ms/1000:.2f} s{'':<8} No")
            else:
                print(f"{n:<15} {time_ms:.3f} ms{'':<8} No")
        except Exception as e:
            print(f"{n:<15} {'Too slow':<15} No")
    
    # Test subset sum problem
    print("\n3. Subset Sum Problem Comparison")
    print("-" * 70)
    
    test_cases = [
        ([1, 3, 5, 7, 9], 12),
        ([2, 4, 6, 8, 10, 12], 18),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15),
    ]
    
    for numbers, target in test_cases:
        print(f"\nNumbers: {numbers}, Target: {target}")
        
        # Brute force (intractable for large inputs)
        if len(numbers) <= 10:
            start = time.perf_counter()
            result_bf = brute_force_subset_sum(numbers, target)
            end = time.perf_counter()
            time_bf = (end - start) * 1000
            print(f"  Brute Force: {time_bf:.3f} ms, Result: {result_bf}")
        
        # Efficient (pseudo-polynomial)
        start = time.perf_counter()
        result_eff = efficient_subset_sum(numbers, target)
        end = time.perf_counter()
        time_eff = (end - start) * 1000
        print(f"  Efficient DP: {time_eff:.3f} ms, Result: {result_eff}")
    
    print("\n" + "=" * 70)
    print("Key Concepts:")
    print("=" * 70)
    print("1. Polynomial time (O(n^k)): Generally considered tractable")
    print("2. Exponential time (O(2^n)): Generally intractable for large n")
    print("3. P vs NP: Whether problems with exponential brute-force solutions")
    print("   can be solved in polynomial time")
    print("4. Pseudo-polynomial: Polynomial in the numeric value, not input size")
    print("5. Practical tractability depends on input size and constraints")


if __name__ == "__main__":
    demonstrate_tractability()
