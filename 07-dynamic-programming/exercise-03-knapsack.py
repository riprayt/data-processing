"""
Exercise 3: Knapsack Problem
0/1 Knapsack and related problems using dynamic programming
"""


def knapsack_01(weights, values, capacity):
    """
    0/1 Knapsack Problem
    
    Given items with weights and values, maximize value without exceeding capacity.
    Each item can be taken at most once.
    
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity) or O(capacity) with optimization
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum weight capacity
    
    Returns:
        Tuple (max_value, selected_items)
    """
    n = len(weights)
    
    # DP table: dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i - 1][w]
            
            # Take item i (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
    
    # Reconstruct solution
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # Item i-1 was selected
            selected.append(i - 1)
            w -= weights[i - 1]
    
    selected.reverse()
    return dp[n][capacity], selected


def knapsack_01_optimized(weights, values, capacity):
    """Space-optimized version using only O(capacity) space"""
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Iterate backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def fractional_knapsack_greedy(weights, values, capacity):
    """
    Fractional Knapsack (greedy solution is optimal)
    
    Items can be taken fractionally.
    Greedy: Take items with highest value/weight ratio first.
    
    Time Complexity: O(n log n) for sorting
    """
    items = [(values[i] / weights[i], weights[i], values[i], i) 
             for i in range(len(weights))]
    items.sort(reverse=True)
    
    total_value = 0
    remaining = capacity
    selected = []
    
    for ratio, weight, value, idx in items:
        if remaining >= weight:
            # Take whole item
            total_value += value
            remaining -= weight
            selected.append((idx, 1.0))  # (item_index, fraction)
        elif remaining > 0:
            # Take fraction
            fraction = remaining / weight
            total_value += value * fraction
            selected.append((idx, fraction))
            break
    
    return total_value, selected


def demonstrate_knapsack():
    """Demonstrate knapsack problems"""
    print("=" * 70)
    print("Knapsack Problem")
    print("=" * 70)
    
    # Example 1: 0/1 Knapsack
    print("\n1. 0/1 Knapsack Problem")
    print("-" * 70)
    
    weights1 = [2, 3, 4, 5]
    values1 = [3, 4, 5, 6]
    capacity1 = 5
    
    print(f"Weights: {weights1}")
    print(f"Values:  {values1}")
    print(f"Capacity: {capacity1}")
    
    max_value, selected = knapsack_01(weights1, values1, capacity1)
    
    print(f"\nMaximum value: {max_value}")
    print("Selected items:")
    total_weight = 0
    for idx in selected:
        print(f"  Item {idx}: weight {weights1[idx]}, value {values1[idx]}")
        total_weight += weights1[idx]
    print(f"Total weight: {total_weight}")
    
    # Example 2: Larger knapsack
    print("\n\n2. Larger 0/1 Knapsack")
    print("-" * 70)
    
    weights2 = [10, 20, 30, 40, 50]
    values2 = [60, 100, 120, 140, 150]
    capacity2 = 100
    
    print(f"Weights: {weights2}")
    print(f"Values:  {values2}")
    print(f"Capacity: {capacity2}")
    
    max_value, selected = knapsack_01(weights2, values2, capacity2)
    max_value_opt = knapsack_01_optimized(weights2, values2, capacity2)
    
    print(f"\nMaximum value: {max_value} (optimized: {max_value_opt})")
    print("Selected items:")
    for idx in selected:
        print(f"  Item {idx}: weight {weights2[idx]}, value {values2[idx]}")
    
    # Example 3: Fractional Knapsack
    print("\n\n3. Fractional Knapsack (Greedy Optimal)")
    print("-" * 70)
    
    weights3 = [10, 20, 30]
    values3 = [60, 100, 120]
    capacity3 = 50
    
    print(f"Weights: {weights3}")
    print(f"Values:  {values3}")
    print(f"Capacity: {capacity3}")
    
    max_value, selected = fractional_knapsack_greedy(weights3, values3, capacity3)
    
    print(f"\nMaximum value: {max_value:.2f}")
    print("Selected items:")
    for idx, fraction in selected:
        print(f"  Item {idx}: {fraction*100:.1f}% (weight {weights3[idx]*fraction:.1f}, value {values3[idx]*fraction:.1f})")
    
    # Example 4: Comparison
    print("\n\n4. 0/1 vs Fractional Comparison")
    print("-" * 70)
    
    weights4 = [10, 20, 30]
    values4 = [60, 100, 120]
    capacity4 = 50
    
    value_01, _ = knapsack_01(weights4, values4, capacity4)
    value_frac, _ = fractional_knapsack_greedy(weights4, values4, capacity4)
    
    print(f"0/1 Knapsack value: {value_01}")
    print(f"Fractional value: {value_frac:.2f}")
    print(f"Difference: {value_frac - value_01:.2f} (fractional allows partial items)")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. 0/1 Knapsack: DP solution, O(n * capacity) time")
    print("2. Fractional Knapsack: Greedy is optimal, O(n log n) time")
    print("3. DP recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)")
    print("4. Space can be optimized to O(capacity)")
    print("5. Applications: Resource allocation, portfolio optimization, cutting stock")


if __name__ == "__main__":
    demonstrate_knapsack()
