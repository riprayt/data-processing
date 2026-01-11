"""
Exercise 1: Fibonacci and Counting Paths
Introduction to dynamic programming with classic examples
"""


def fibonacci_naive(n):
    """
    Naive recursive Fibonacci (exponential time)
    Time Complexity: O(2^n)
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoized(n, memo=None):
    """
    Fibonacci with memoization (top-down DP)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_bottom_up(n):
    """
    Fibonacci with bottom-up DP
    Time Complexity: O(n)
    Space Complexity: O(1) - only need last two values
    """
    if n <= 1:
        return n
    
    prev2 = 0
    prev1 = 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def count_paths_grid(m, n):
    """
    Count paths from top-left to bottom-right in m×n grid
    Can only move right or down
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n) or O(min(m, n)) with optimization
    """
    # DP table: dp[i][j] = number of paths to (i, j)
    dp = [[0] * n for _ in range(m)]
    
    # Base case: one way to reach any cell in first row/column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Fill table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]


def count_paths_optimized(m, n):
    """Optimized version using only O(min(m, n)) space"""
    if m < n:
        m, n = n, m  # Ensure n is smaller
    
    prev = [1] * n
    
    for i in range(1, m):
        curr = [1]
        for j in range(1, n):
            curr.append(curr[-1] + prev[j])
        prev = curr
    
    return prev[-1]


def demonstrate_fibonacci_paths():
    """Demonstrate Fibonacci and path counting"""
    print("=" * 70)
    print("Fibonacci and Counting Paths")
    print("=" * 70)
    
    # Example 1: Fibonacci comparison
    print("\n1. Fibonacci Sequence")
    print("-" * 70)
    
    n_values = [5, 10, 20, 30, 40]
    
    print("Comparing different approaches:")
    print(f"{'n':<5} {'Naive':<15} {'Memoized':<15} {'Bottom-up':<15}")
    print("-" * 70)
    
    import time
    
    for n in n_values:
        # Naive (only for small n)
        if n <= 30:
            start = time.perf_counter()
            fib_naive = fibonacci_naive(n)
            naive_time = (time.perf_counter() - start) * 1000
        else:
            fib_naive = "N/A"
            naive_time = float('inf')
        
        # Memoized
        start = time.perf_counter()
        fib_memo = fibonacci_memoized(n)
        memo_time = (time.perf_counter() - start) * 1000
        
        # Bottom-up
        start = time.perf_counter()
        fib_bu = fibonacci_bottom_up(n)
        bu_time = (time.perf_counter() - start) * 1000
        
        if n <= 30:
            print(f"{n:<5} {naive_time:>10.3f}ms   {memo_time:>10.3f}ms   {bu_time:>10.3f}ms")
            print(f"      Result: {fib_naive} = {fib_memo} = {fib_bu}")
        else:
            print(f"{n:<5} {'Too slow':<15} {memo_time:>10.3f}ms   {bu_time:>10.3f}ms")
            print(f"      Result: {fib_memo} = {fib_bu}")
        print()
    
    # Example 2: Grid paths
    print("\n2. Counting Paths in Grid")
    print("-" * 70)
    
    grids = [(2, 2), (3, 3), (4, 4), (5, 5), (3, 7)]
    
    for m, n in grids:
        paths = count_paths_grid(m, n)
        paths_opt = count_paths_optimized(m, n)
        print(f"Grid {m}×{n}: {paths} paths (optimized: {paths_opt})")
    
    # Example 3: Visualize small grid
    print("\n3. Visualizing 3×3 Grid")
    print("-" * 70)
    
    m, n = 3, 3
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    print("DP table:")
    for row in dp:
        print(f"  {row}")
    print(f"\nTotal paths: {dp[m - 1][n - 1]}")
    
    print("\n" + "=" * 70)
    print("Key DP Concepts:")
    print("=" * 70)
    print("1. Overlapping subproblems: Same subproblems computed multiple times")
    print("2. Optimal substructure: Optimal solution contains optimal subsolutions")
    print("3. Memoization: Top-down, cache results")
    print("4. Tabulation: Bottom-up, fill table iteratively")
    print("5. Space optimization: Often only need previous values")


if __name__ == "__main__":
    demonstrate_fibonacci_paths()
