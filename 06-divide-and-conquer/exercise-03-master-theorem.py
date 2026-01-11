"""
Exercise 3: Master Theorem
Understanding and applying the Master Theorem for divide-and-conquer recurrences
"""

import math


def solve_recurrence(a, b, f_n, n):
    """
    Solve recurrence T(n) = a*T(n/b) + f(n) using Master Theorem
    
    Master Theorem cases:
    1. If f(n) = O(n^(log_b(a) - ε)) for some ε > 0: T(n) = Θ(n^(log_b(a)))
    2. If f(n) = Θ(n^(log_b(a))): T(n) = Θ(n^(log_b(a)) * log n)
    3. If f(n) = Ω(n^(log_b(a) + ε)) and af(n/b) ≤ cf(n) for some c < 1:
       T(n) = Θ(f(n))
    
    Args:
        a: Number of subproblems
        b: Factor by which problem size is reduced
        f_n: Function f(n) - work done at each level
        n: Problem size
    
    Returns:
        Tuple (case, complexity, explanation)
    """
    log_b_a = math.log(a) / math.log(b)
    
    # Determine f(n) complexity
    if callable(f_n):
        # Try to determine f(n) complexity from sample values
        f_1 = f_n(1)
        f_n_val = f_n(n)
        f_n2 = f_n(n // 2)
        
        # Estimate growth rate
        if f_n_val == 1 or f_n_val == 0:
            f_complexity = 0  # O(1)
        elif abs(math.log(f_n_val) / math.log(n) - 1) < 0.1:
            f_complexity = 1  # O(n)
        elif abs(math.log(f_n_val) / math.log(n) - 2) < 0.1:
            f_complexity = 2  # O(n²)
        else:
            f_complexity = math.log(f_n_val) / math.log(n) if n > 1 else 0
    else:
        f_complexity = f_n
    
    epsilon = 0.1
    
    if f_complexity < log_b_a - epsilon:
        # Case 1
        complexity = f"Θ(n^{log_b_a:.2f})"
        case = 1
        explanation = f"f(n) = O(n^{f_complexity:.2f}) < n^{log_b_a:.2f}"
    elif abs(f_complexity - log_b_a) < epsilon:
        # Case 2
        complexity = f"Θ(n^{log_b_a:.2f} log n)"
        case = 2
        explanation = f"f(n) = Θ(n^{log_b_a:.2f})"
    else:
        # Case 3 (simplified check)
        complexity = f"Θ(f(n)) ≈ Θ(n^{f_complexity:.2f})"
        case = 3
        explanation = f"f(n) = Ω(n^{f_complexity:.2f}) > n^{log_b_a:.2f}"
    
    return case, complexity, explanation


def demonstrate_master_theorem():
    """Demonstrate Master Theorem applications"""
    print("=" * 70)
    print("Master Theorem for Divide-and-Conquer Recurrences")
    print("=" * 70)
    print("\nMaster Theorem: T(n) = a·T(n/b) + f(n)")
    print("where a ≥ 1, b > 1, and f(n) is asymptotically positive\n")
    
    # Example 1: Mergesort
    print("Example 1: Mergesort")
    print("-" * 70)
    print("Recurrence: T(n) = 2T(n/2) + Θ(n)")
    print("a = 2, b = 2, f(n) = n")
    print("log_b(a) = log₂(2) = 1")
    
    case, complexity, explanation = solve_recurrence(2, 2, 1, 100)
    print(f"Case: {case}")
    print(f"Complexity: {complexity}")
    print(f"Explanation: {explanation}")
    print("Result: Mergesort is O(n log n) ✓")
    
    # Example 2: Binary Search
    print("\n\nExample 2: Binary Search")
    print("-" * 70)
    print("Recurrence: T(n) = T(n/2) + Θ(1)")
    print("a = 1, b = 2, f(n) = 1")
    print("log_b(a) = log₂(1) = 0")
    
    case, complexity, explanation = solve_recurrence(1, 2, 0, 100)
    print(f"Case: {case}")
    print(f"Complexity: {complexity}")
    print(f"Explanation: {explanation}")
    print("Result: Binary search is O(log n) ✓")
    
    # Example 3: Karatsuba Multiplication
    print("\n\nExample 3: Karatsuba Multiplication")
    print("-" * 70)
    print("Recurrence: T(n) = 3T(n/2) + Θ(n)")
    print("a = 3, b = 2, f(n) = n")
    print("log_b(a) = log₂(3) ≈ 1.58")
    
    case, complexity, explanation = solve_recurrence(3, 2, 1, 100)
    print(f"Case: {case}")
    print(f"Complexity: {complexity}")
    print(f"Explanation: {explanation}")
    print("Result: Karatsuba is O(n^1.58) ✓")
    
    # Example 4: Matrix Multiplication (Strassen)
    print("\n\nExample 4: Strassen's Matrix Multiplication")
    print("-" * 70)
    print("Recurrence: T(n) = 7T(n/2) + Θ(n²)")
    print("a = 7, b = 2, f(n) = n²")
    print("log_b(a) = log₂(7) ≈ 2.81")
    
    case, complexity, explanation = solve_recurrence(7, 2, 2, 100)
    print(f"Case: {case}")
    print(f"Complexity: {complexity}")
    print(f"Explanation: {explanation}")
    print("Result: Strassen is O(n^2.81) ✓")
    
    # Example 5: Quick Sort (average case)
    print("\n\nExample 5: Quick Sort (Average Case)")
    print("-" * 70)
    print("Recurrence: T(n) = 2T(n/2) + Θ(n)")
    print("a = 2, b = 2, f(n) = n")
    print("log_b(a) = log₂(2) = 1")
    
    case, complexity, explanation = solve_recurrence(2, 2, 1, 100)
    print(f"Case: {case}")
    print(f"Complexity: {complexity}")
    print(f"Explanation: {explanation}")
    print("Result: Quick sort average case is O(n log n) ✓")
    
    # Summary table
    print("\n" + "=" * 70)
    print("Common Recurrences Summary")
    print("=" * 70)
    print(f"{'Algorithm':<30} {'Recurrence':<25} {'Complexity':<20}")
    print("-" * 70)
    print(f"{'Mergesort':<30} {'T(n) = 2T(n/2) + n':<25} {'O(n log n)':<20}")
    print(f"{'Binary Search':<30} {'T(n) = T(n/2) + 1':<25} {'O(log n)':<20}")
    print(f"{'Karatsuba':<30} {'T(n) = 3T(n/2) + n':<25} {'O(n^1.58)':<20}")
    print(f"{'Strassen':<30} {'T(n) = 7T(n/2) + n²':<25} {'O(n^2.81)':<20}")
    print(f"{'Quick Sort (avg)':<30} {'T(n) = 2T(n/2) + n':<25} {'O(n log n)':<20}")
    
    print("\n" + "=" * 70)
    print("Master Theorem Cases:")
    print("=" * 70)
    print("Case 1: f(n) grows slower than n^(log_b(a))")
    print("  → T(n) = Θ(n^(log_b(a)))")
    print("\nCase 2: f(n) grows same as n^(log_b(a))")
    print("  → T(n) = Θ(n^(log_b(a)) log n)")
    print("\nCase 3: f(n) grows faster than n^(log_b(a))")
    print("  → T(n) = Θ(f(n))")


if __name__ == "__main__":
    demonstrate_master_theorem()
