"""
Exercise 2: Weighted Interval Scheduling
Dynamic programming solution for scheduling with weights
"""


def weighted_interval_scheduling(intervals):
    """
    Weighted interval scheduling using dynamic programming
    
    Each interval has (start, end, weight)
    Goal: Select non-overlapping intervals with maximum total weight
    
    Time Complexity: O(n²) or O(n log n) with binary search
    Space Complexity: O(n)
    
    Args:
        intervals: List of tuples (start, end, weight)
    
    Returns:
        Tuple (max_weight, selected_intervals)
    """
    # Sort by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    n = len(sorted_intervals)
    
    # DP: dp[i] = maximum weight using first i intervals
    dp = [0] * (n + 1)
    
    # For each interval, find last compatible interval
    for i in range(1, n + 1):
        start, end, weight = sorted_intervals[i - 1]
        
        # Find last interval that ends before this one starts
        last_compatible = 0
        for j in range(i - 1, 0, -1):
            if sorted_intervals[j - 1][1] <= start:
                last_compatible = j
                break
        
        # Two choices: include or exclude current interval
        dp[i] = max(
            dp[i - 1],  # Don't include current
            dp[last_compatible] + weight  # Include current
        )
    
    # Reconstruct solution
    selected = []
    i = n
    while i > 0:
        if dp[i] == dp[i - 1]:
            # Current interval not selected
            i -= 1
        else:
            # Current interval selected
            selected.append(sorted_intervals[i - 1])
            # Find last compatible
            start = sorted_intervals[i - 1][0]
            while i > 0 and sorted_intervals[i - 1][1] > start:
                i -= 1
    
    selected.reverse()
    return dp[n], selected


def demonstrate_weighted_intervals():
    """Demonstrate weighted interval scheduling"""
    print("=" * 70)
    print("Weighted Interval Scheduling")
    print("=" * 70)
    
    # Example 1: Simple case
    print("\nExample 1: Simple Weighted Intervals")
    print("-" * 70)
    
    intervals1 = [
        (1, 4, 2),
        (3, 5, 1),
        (0, 6, 4),
        (5, 7, 3),
        (3, 8, 5),
        (5, 9, 2),
        (6, 10, 4),
        (8, 11, 1),
    ]
    
    print("Intervals (start, end, weight):")
    for i, (s, e, w) in enumerate(intervals1):
        print(f"  Interval {i}: [{s}, {e}] weight {w}")
    
    max_weight, selected = weighted_interval_scheduling(intervals1)
    
    print(f"\nMaximum weight: {max_weight}")
    print("Selected intervals:")
    for s, e, w in selected:
        print(f"  [{s}, {e}] weight {w}")
    
    # Example 2: Job scheduling
    print("\n\nExample 2: Job Scheduling Application")
    print("-" * 70)
    
    jobs = [
        ("Job1", 0, 3, 5),
        ("Job2", 2, 5, 6),
        ("Job3", 4, 7, 5),
        ("Job4", 6, 9, 4),
        ("Job5", 8, 10, 2),
        ("Job6", 1, 4, 8),
    ]
    
    # Convert to (start, end, weight) format
    intervals2 = [(start, end, weight) for _, start, end, weight in jobs]
    job_names = {intervals2[i]: name for i, (name, _, _, _) in enumerate(jobs)}
    
    print("Jobs:")
    for name, start, end, weight in jobs:
        print(f"  {name}: [{start}, {end}] profit {weight}")
    
    max_weight, selected = weighted_interval_scheduling(intervals2)
    
    print(f"\nMaximum profit: {max_weight}")
    print("Selected jobs:")
    for interval in selected:
        name = job_names[interval]
        s, e, w = interval
        print(f"  {name}: [{s}, {e}] profit {w}")
    
    # Example 3: Resource allocation
    print("\n\nExample 3: Resource Allocation")
    print("-" * 70)
    
    tasks = [
        (1, 3, 10),
        (2, 5, 15),
        (4, 6, 10),
        (6, 8, 20),
        (7, 9, 5),
        (9, 10, 15),
    ]
    
    print("Tasks (start, end, value):")
    for s, e, v in tasks:
        print(f"  [{s}, {e}] value {v}")
    
    max_value, selected = weighted_interval_scheduling(tasks)
    
    print(f"\nMaximum total value: {max_value}")
    print("Selected tasks:")
    total_time = 0
    for s, e, v in selected:
        duration = e - s
        total_time += duration
        print(f"  [{s}, {e}] value {v}, duration {duration}")
    print(f"Total time used: {total_time}")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. Optimal substructure: Optimal solution contains optimal subsolutions")
    print("2. DP recurrence: dp[i] = max(dp[i-1], dp[p(i)] + weight[i])")
    print("3. p(i) = last interval compatible with interval i")
    print("4. Can be optimized to O(n log n) with binary search for p(i)")
    print("5. Applications: Job scheduling, resource allocation, activity selection")


if __name__ == "__main__":
    demonstrate_weighted_intervals()
