"""
Exercise 1: Asymptotic Notation
Demonstrates Big-O, Big-Omega, and Big-Theta notation with examples
"""

import time
import random
import math


def demonstrate_big_o():
    """
    Demonstrates O-notation (upper bound)
    f(n) = O(g(n)) means f(n) grows at most as fast as g(n)
    """
    print("=" * 60)
    print("Big-O Notation (Upper Bound)")
    print("=" * 60)
    print("f(n) = O(g(n)) means: f(n) ≤ c·g(n) for some constant c > 0")
    print("f(n) grows at most as fast as g(n)\n")
    
    examples = [
        ("3n + 5", lambda n: 3*n + 5, "O(n)", lambda n: n),
        ("n² + 2n + 1", lambda n: n**2 + 2*n + 1, "O(n²)", lambda n: n**2),
        ("log(n) + 10", lambda n: math.log(n) + 10, "O(log n)", lambda n: math.log(n)),
        ("2^n + n²", lambda n: 2**n + n**2, "O(2^n)", lambda n: 2**n),
    ]
    
    for desc, func, big_o, g_func in examples:
        print(f"{desc} = {big_o}")
        print(f"  Verifying for n = 10, 100, 1000:")
        for n in [10, 100, 1000]:
            if n > 50 and "2^n" in desc:
                print(f"    n={n}: Skipped (too large)")
                continue
            f_val = func(n)
            g_val = g_func(n)
            ratio = f_val / g_val if g_val > 0 else float('inf')
            print(f"    n={n}: f(n)={f_val:.2f}, g(n)={g_val:.2f}, ratio={ratio:.2f}")
        print()


def demonstrate_big_omega():
    """
    Demonstrates Ω-notation (lower bound)
    f(n) = Ω(g(n)) means f(n) grows at least as fast as g(n)
    """
    print("=" * 60)
    print("Big-Omega Notation (Lower Bound)")
    print("=" * 60)
    print("f(n) = Ω(g(n)) means: f(n) ≥ c·g(n) for some constant c > 0")
    print("f(n) grows at least as fast as g(n)\n")
    
    examples = [
        ("3n + 5", lambda n: 3*n + 5, "Ω(n)", lambda n: n),
        ("n² + 2n + 1", lambda n: n**2 + 2*n + 1, "Ω(n²)", lambda n: n**2),
        ("log(n) + 10", lambda n: math.log(n) + 10, "Ω(log n)", lambda n: math.log(n)),
        ("n log n + n", lambda n: n * math.log(n) + n, "Ω(n log n)", lambda n: n * math.log(n)),
    ]
    
    for desc, func, big_omega, g_func in examples:
        print(f"{desc} = {big_omega}")
        print(f"  Verifying for n = 10, 100, 1000:")
        for n in [10, 100, 1000]:
            f_val = func(n)
            g_val = g_func(n)
            ratio = f_val / g_val if g_val > 0 else float('inf')
            print(f"    n={n}: f(n)={f_val:.2f}, g(n)={g_val:.2f}, ratio={ratio:.2f}")
        print()


def demonstrate_big_theta():
    """
    Demonstrates Θ-notation (tight bound)
    f(n) = Θ(g(n)) means f(n) grows exactly as fast as g(n)
    """
    print("=" * 60)
    print("Big-Theta Notation (Tight Bound)")
    print("=" * 60)
    print("f(n) = Θ(g(n)) means: c₁·g(n) ≤ f(n) ≤ c₂·g(n) for constants c₁, c₂ > 0")
    print("f(n) grows exactly as fast as g(n)\n")
    
    examples = [
        ("3n + 5", lambda n: 3*n + 5, "Θ(n)", lambda n: n),
        ("n² + 2n + 1", lambda n: n**2 + 2*n + 1, "Θ(n²)", lambda n: n**2),
        ("n log n + n", lambda n: n * math.log(n) + n, "Θ(n log n)", lambda n: n * math.log(n)),
    ]
    
    for desc, func, big_theta, g_func in examples:
        print(f"{desc} = {big_theta}")
        print(f"  Verifying for n = 10, 100, 1000:")
        for n in [10, 100, 1000]:
            f_val = func(n)
            g_val = g_func(n)
            ratio = f_val / g_val if g_val > 0 else float('inf')
            print(f"    n={n}: f(n)={f_val:.2f}, g(n)={g_val:.2f}, ratio={ratio:.2f}")
        print()


def compare_functions():
    """Compare growth rates of common functions"""
    print("=" * 60)
    print("Comparing Growth Rates")
    print("=" * 60)
    print("Order from slowest to fastest growth:\n")
    
    functions = [
        ("1", lambda n: 1),
        ("log n", lambda n: math.log(n) if n > 0 else 0),
        ("√n", lambda n: math.sqrt(n)),
        ("n", lambda n: n),
        ("n log n", lambda n: n * math.log(n) if n > 0 else 0),
        ("n²", lambda n: n**2),
        ("n³", lambda n: n**3),
        ("2^n", lambda n: 2**n),
    ]
    
    n_values = [10, 100, 1000]
    
    print(f"{'Function':<15}", end="")
    for n in n_values:
        print(f"n={n:<10}", end="")
    print()
    print("-" * 60)
    
    for name, func in functions:
        print(f"{name:<15}", end="")
        for n in n_values:
            if "2^n" in name and n > 50:
                print(f"{'N/A':<10}", end="")
            else:
                try:
                    val = func(n)
                    if val > 1e10:
                        print(f"{val:.2e}", end="  ")
                    else:
                        print(f"{val:<10.2f}", end="")
                except:
                    print(f"{'N/A':<10}", end="")
        print()


if __name__ == "__main__":
    demonstrate_big_o()
    print("\n")
    demonstrate_big_omega()
    print("\n")
    demonstrate_big_theta()
    print("\n")
    compare_functions()
