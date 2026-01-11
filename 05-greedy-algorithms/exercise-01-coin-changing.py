"""
Exercise 1: Coin Changing Problem
Greedy algorithm for making change with minimum coins
"""


def greedy_coin_change(coins, amount):
    """
    Greedy coin changing algorithm
    
    Note: This works optimally only for certain coin systems (like US coins).
    For arbitrary coin systems, dynamic programming is needed.
    
    Time Complexity: O(n) where n is the number of coin denominations
    Space Complexity: O(1)
    
    Args:
        coins: List of coin denominations (sorted in descending order)
        amount: Target amount to make
    
    Returns:
        Dictionary mapping coin -> count, or None if impossible
    """
    result = {}
    remaining = amount
    
    for coin in coins:
        if remaining == 0:
            break
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= count * coin
    
    if remaining > 0:
        return None  # Cannot make exact change
    
    return result


def dp_coin_change(coins, amount):
    """
    Dynamic programming solution for coin changing
    Works for any coin system
    
    Time Complexity: O(n * amount)
    Space Complexity: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[amount] == float('inf'):
        return None
    
    # Reconstruct solution
    result = {}
    remaining = amount
    while remaining > 0:
        for coin in sorted(coins, reverse=True):
            if remaining >= coin and dp[remaining] == dp[remaining - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                remaining -= coin
                break
    
    return result


def demonstrate_coin_changing():
    """Demonstrate coin changing algorithms"""
    print("=" * 70)
    print("Coin Changing Problem")
    print("=" * 70)
    
    # Example 1: US coin system (greedy works)
    print("\nExample 1: US Coin System (Greedy Optimal)")
    print("-" * 70)
    
    us_coins = [25, 10, 5, 1]  # Quarters, dimes, nickels, pennies
    amounts = [67, 99, 43, 100]
    
    for amount in amounts:
        result = greedy_coin_change(us_coins, amount)
        if result:
            total_coins = sum(result.values())
            print(f"Amount: ${amount/100:.2f}")
            print(f"  Coins used: {result}")
            print(f"  Total coins: {total_coins}")
        else:
            print(f"Amount: ${amount/100:.2f} - Cannot make change")
        print()
    
    # Example 2: Non-standard coin system (greedy may not work)
    print("\nExample 2: Non-Standard Coin System")
    print("-" * 70)
    
    weird_coins = [10, 6, 1]
    amount = 12
    
    print(f"Coins: {weird_coins}")
    print(f"Target amount: {amount}")
    
    greedy_result = greedy_coin_change(weird_coins, amount)
    dp_result = dp_coin_change(weird_coins, amount)
    
    if greedy_result:
        greedy_total = sum(greedy_result.values())
        print(f"Greedy solution: {greedy_result} (Total: {greedy_total} coins)")
    else:
        print("Greedy solution: Cannot make change")
    
    if dp_result:
        dp_total = sum(dp_result.values())
        print(f"DP solution: {dp_result} (Total: {dp_total} coins)")
        if greedy_result and greedy_total > dp_total:
            print(f"  Note: Greedy is NOT optimal! DP uses {dp_total - greedy_total} fewer coins.")
    else:
        print("DP solution: Cannot make change")
    
    # Example 3: European coin system
    print("\n\nExample 3: European Coin System")
    print("-" * 70)
    
    euro_coins = [200, 100, 50, 20, 10, 5, 2, 1]  # In cents
    amount = 347  # 3.47 euros
    
    result = greedy_coin_change(euro_coins, amount)
    if result:
        print(f"Amount: {amount/100:.2f} euros")
        print(f"Coins used: {result}")
        print(f"Total coins: {sum(result.values())}")
    
    print("\n" + "=" * 70)
    print("Key Observations:")
    print("=" * 70)
    print("1. Greedy works optimally for 'canonical' coin systems")
    print("2. US and European coin systems are canonical")
    print("3. For arbitrary systems, use dynamic programming")
    print("4. Greedy is faster but may not be optimal")


if __name__ == "__main__":
    demonstrate_coin_changing()
