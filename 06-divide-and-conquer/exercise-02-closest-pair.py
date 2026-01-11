"""
Exercise 2: Closest Pair of Points
Divide and conquer algorithm to find the closest pair of points
"""

import math


def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force_closest_pair(points):
    """
    Brute force approach: Check all pairs
    Time Complexity: O(n²)
    """
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_dist


def closest_pair(points):
    """
    Divide and conquer algorithm for closest pair
    
    Time Complexity: O(n log² n)
    Can be optimized to O(n log n) with better strip processing
    
    Args:
        points: List of (x, y) tuples
    
    Returns:
        Tuple ((p1, p2), distance)
    """
    if len(points) <= 3:
        return brute_force_closest_pair(points)
    
    # Sort by x-coordinate
    points_sorted = sorted(points, key=lambda p: p[0])
    
    mid = len(points_sorted) // 2
    left_points = points_sorted[:mid]
    right_points = points_sorted[mid:]
    
    # Recursively find closest pair in left and right halves
    left_pair, left_dist = closest_pair(left_points)
    right_pair, right_dist = closest_pair(right_points)
    
    # Find minimum of left and right
    if left_dist < right_dist:
        min_dist = left_dist
        closest = left_pair
    else:
        min_dist = right_dist
        closest = right_pair
    
    # Check strip around the dividing line
    mid_x = points_sorted[mid][0]
    strip = [p for p in points_sorted if abs(p[0] - mid_x) < min_dist]
    
    # Sort strip by y-coordinate
    strip_sorted = sorted(strip, key=lambda p: p[1])
    
    # Check points in strip (only need to check next 7 points)
    for i in range(len(strip_sorted)):
        for j in range(i + 1, min(i + 8, len(strip_sorted))):
            dist = euclidean_distance(strip_sorted[i], strip_sorted[j])
            if dist < min_dist:
                min_dist = dist
                closest = (strip_sorted[i], strip_sorted[j])
    
    return closest, min_dist


def demonstrate_closest_pair():
    """Demonstrate closest pair algorithm"""
    print("=" * 70)
    print("Closest Pair of Points")
    print("=" * 70)
    
    # Example 1: Small set
    print("\nExample 1: Small Point Set")
    print("-" * 70)
    
    points1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    
    print("Points:", points1)
    closest, dist = closest_pair(points1)
    print(f"Closest pair: {closest}")
    print(f"Distance: {dist:.4f}")
    
    # Verify with brute force
    brute_closest, brute_dist = brute_force_closest_pair(points1)
    print(f"Brute force: {brute_closest}, distance: {brute_dist:.4f}")
    print(f"Match: {abs(dist - brute_dist) < 1e-9}")
    
    # Example 2: Points on a line
    print("\n\nExample 2: Points on a Line")
    print("-" * 70)
    
    points2 = [(1, 1), (2, 1), (3, 1), (5, 1), (8, 1), (13, 1)]
    print("Points:", points2)
    closest, dist = closest_pair(points2)
    print(f"Closest pair: {closest}")
    print(f"Distance: {dist:.4f}")
    
    # Example 3: Random points
    print("\n\nExample 3: Random Points")
    print("-" * 70)
    
    import random
    random.seed(42)
    points3 = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(20)]
    
    print(f"Generated {len(points3)} random points")
    closest, dist = closest_pair(points3)
    print(f"Closest pair: {closest}")
    print(f"Distance: {dist:.4f}")
    
    # Example 4: Performance comparison
    print("\n\nExample 4: Performance Comparison")
    print("-" * 70)
    
    import time
    
    sizes = [10, 50, 100]
    
    for size in sizes:
        test_points = [(random.randint(0, 1000), random.randint(0, 1000)) 
                       for _ in range(size)]
        
        # Divide and conquer
        start = time.perf_counter()
        closest, _ = closest_pair(test_points)
        dc_time = (time.perf_counter() - start) * 1000
        
        # Brute force (only for small sizes)
        if size <= 50:
            start = time.perf_counter()
            brute_closest, _ = brute_force_closest_pair(test_points)
            bf_time = (time.perf_counter() - start) * 1000
            print(f"n={size}: DC={dc_time:.3f}ms, BF={bf_time:.3f}ms")
        else:
            print(f"n={size}: DC={dc_time:.3f}ms, BF=skipped (too slow)")
    
    print("\n" + "=" * 70)
    print("Algorithm Steps:")
    print("=" * 70)
    print("1. Divide: Split points by x-coordinate")
    print("2. Conquer: Recursively find closest in left and right")
    print("3. Combine: Check strip around dividing line")
    print("4. Key insight: Only need to check 7 points in strip")
    print("5. Time complexity: O(n log² n) or O(n log n) with optimization")


if __name__ == "__main__":
    demonstrate_closest_pair()
