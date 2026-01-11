"""
Exercise 2: P vs NP Problem
Understanding complexity classes P, NP, NP-complete, and NP-hard
"""

import time
import random


def polynomial_time_example(n):
    """
    Example of a problem in P (Polynomial time)
    Finding maximum element in array: O(n)
    """
    arr = list(range(n))
    random.shuffle(arr)
    return max(arr)


def exponential_time_example(n):
    """
    Example of a problem that seems to require exponential time
    Generating all subsets: O(2^n)
    """
    arr = list(range(n))
    from itertools import combinations
    
    all_subsets = []
    for r in range(n + 1):
        all_subsets.extend(list(combinations(arr, r)))
    
    return len(all_subsets)


def verify_solution_problem(problem_instance, solution):
    """
    Example of polynomial-time verification
    Many NP problems have this property: hard to solve, easy to verify
    """
    # Example: Subset Sum verification
    numbers, target = problem_instance
    return sum(solution) == target


def demonstrate_complexity_classes():
    """Demonstrate P, NP, NP-complete, and NP-hard concepts"""
    print("=" * 70)
    print("P vs NP Problem and Complexity Classes")
    print("=" * 70)
    
    print("\n1. Complexity Class P (Polynomial Time)")
    print("-" * 70)
    print("Problems solvable in polynomial time by a deterministic Turing machine")
    print("\nExamples:")
    print("  - Sorting: O(n log n)")
    print("  - Shortest path: O(V + E)")
    print("  - Maximum flow: O(V * E²)")
    print("  - Linear programming: O(n³)")
    
    print("\n\n2. Complexity Class NP (Nondeterministic Polynomial)")
    print("-" * 70)
    print("Problems whose solutions can be VERIFIED in polynomial time")
    print("\nExamples:")
    print("  - Subset Sum: Given numbers and target, verify subset sums to target")
    print("  - Hamiltonian Cycle: Verify if cycle visits all vertices")
    print("  - 3-SAT: Verify if assignment satisfies formula")
    print("  - Graph Coloring: Verify if coloring uses ≤ k colors")
    
    # Demonstrate verification
    print("\nVerification example (Subset Sum):")
    numbers = [3, 34, 4, 12, 5, 2]
    target = 9
    solution = [4, 5]  # Candidate solution
    
    print(f"  Problem: Can we find subset of {numbers} that sums to {target}?")
    print(f"  Candidate solution: {solution}")
    is_valid = verify_solution_problem((numbers, target), solution)
    print(f"  Verification: {is_valid} (takes O(n) time)")
    
    print("\n\n3. NP-Complete")
    print("-" * 70)
    print("Problems that are:")
    print("  1. In NP (solutions verifiable in polynomial time)")
    print("  2. NP-hard (every problem in NP reduces to it)")
    print("\nExamples:")
    print("  - 3-SAT")
    print("  - Traveling Salesman Problem")
    print("  - Knapsack Problem")
    print("  - Graph Coloring")
    print("  - Independent Set")
    print("  - Vertex Cover")
    
    print("\n\n4. NP-Hard")
    print("-" * 70)
    print("Problems at least as hard as any problem in NP")
    print("(May or may not be in NP themselves)")
    print("\nExamples:")
    print("  - Halting Problem (undecidable, not in NP)")
    print("  - All NP-complete problems")
    print("  - Optimization versions of NP-complete problems")
    
    print("\n\n5. Relationship Diagram")
    print("-" * 70)
    print("""
    ┌─────────────────────────────────────┐
    │            All Problems              │
    └─────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
    ┌───┴────┐            ┌─────┴─────┐
    │   P   │            │    NP     │
    │       │            │            │
    │ Easy  │            │  Verifiable│
    └───┬───┘            └─────┬─────┘
        │                      │
        │              ┌───────┴───────┐
        │              │               │
        │         ┌────┴────┐     ┌────┴────┐
        │         │NP-      │     │NP-Hard  │
        │         │Complete │     │(not NP) │
        │         └─────────┘     └─────────┘
        │
    If P = NP, then P = NP = NP-complete
    """)
    
    print("\n\n6. P vs NP Question")
    print("-" * 70)
    print("The million-dollar question: Is P = NP?")
    print("\nIf P = NP:")
    print("  - All problems in NP can be solved in polynomial time")
    print("  - Would revolutionize cryptography, optimization, AI")
    print("  - Most experts believe P ≠ NP")
    print("\nIf P ≠ NP:")
    print("  - Some problems are inherently harder than others")
    print("  - Current cryptographic systems remain secure")
    print("  - Need approximation algorithms for hard problems")
    
    print("\n\n7. Practical Implications")
    print("-" * 70)
    print("Even if P = NP, the polynomial might be n^1000 (impractical)")
    print("For practical purposes:")
    print("  - Use efficient algorithms for problems in P")
    print("  - Use heuristics/approximations for NP-complete problems")
    print("  - Use exponential algorithms only for small inputs")
    
    # Performance comparison
    print("\n\n8. Performance Comparison")
    print("-" * 70)
    
    sizes = [10, 20, 30]
    
    print(f"{'Size':<10} {'Polynomial O(n)':<20} {'Exponential O(2^n)':<20}")
    print("-" * 70)
    
    for n in sizes:
        # Polynomial
        start = time.perf_counter()
        polynomial_time_example(n)
        poly_time = (time.perf_counter() - start) * 1000
        
        # Exponential (only for small n)
        if n <= 20:
            start = time.perf_counter()
            exponential_time_example(n)
            exp_time = (time.perf_counter() - start) * 1000
            print(f"{n:<10} {poly_time:>10.3f}ms      {exp_time:>10.3f}ms")
        else:
            print(f"{n:<10} {poly_time:>10.3f}ms      {'Too slow':<20}")
    
    print("\n" + "=" * 70)
    print("Key Takeaways:")
    print("=" * 70)
    print("1. P: Problems solvable efficiently")
    print("2. NP: Problems with efficiently verifiable solutions")
    print("3. NP-complete: Hardest problems in NP")
    print("4. P = NP? is the most important open problem in CS")
    print("5. In practice, use best available algorithms regardless of class")


if __name__ == "__main__":
    demonstrate_complexity_classes()
