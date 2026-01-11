"""
Exercise 1: Mergesort and Counting Inversions
Divide and conquer algorithms for sorting and inversion counting
"""


def mergesort(arr):
    """
    Mergesort algorithm
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Returns:
        Sorted array
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def count_inversions(arr):
    """
    Count inversions in an array using divide and conquer
    
    An inversion is a pair (i, j) where i < j and arr[i] > arr[j]
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Returns:
        Tuple (sorted_array, inversion_count)
    """
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    
    merged, split_inv = merge_and_count(left, right)
    
    total_inv = left_inv + right_inv + split_inv
    return merged, total_inv


def merge_and_count(left, right):
    """Merge two sorted arrays and count split inversions"""
    result = []
    i = j = 0
    inversions = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            # All remaining elements in left are inversions
            inversions += len(left) - i
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions


def brute_force_inversions(arr):
    """Brute force inversion counting for comparison"""
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions


def demonstrate_mergesort_inversions():
    """Demonstrate mergesort and inversion counting"""
    print("=" * 70)
    print("Mergesort and Counting Inversions")
    print("=" * 70)
    
    # Example 1: Mergesort
    print("\n1. Mergesort Algorithm")
    print("-" * 70)
    
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]
    
    for arr in test_arrays:
        sorted_arr = mergesort(arr.copy())
        print(f"Original: {arr}")
        print(f"Sorted:   {sorted_arr}")
        print()
    
    # Example 2: Counting Inversions
    print("\n2. Counting Inversions")
    print("-" * 70)
    
    test_cases = [
        [2, 4, 1, 3, 5],
        [1, 3, 5, 2, 4, 6],
        [6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ]
    
    for arr in test_cases:
        sorted_arr, inv_count = count_inversions(arr.copy())
        brute_count = brute_force_inversions(arr)
        
        print(f"Array: {arr}")
        print(f"  Inversions (divide & conquer): {inv_count}")
        print(f"  Inversions (brute force): {brute_count}")
        print(f"  Match: {inv_count == brute_count}")
        print()
    
    # Example 3: Application - Similarity measure
    print("\n3. Application: Ranking Similarity")
    print("-" * 70)
    
    # Two rankings of the same items
    ranking1 = ['A', 'B', 'C', 'D', 'E']
    ranking2 = ['B', 'A', 'D', 'C', 'E']
    
    # Convert to indices based on ranking1
    indices = {item: i for i, item in enumerate(ranking1)}
    ranking2_indices = [indices[item] for item in ranking2]
    
    _, inversions = count_inversions(ranking2_indices)
    
    print(f"Ranking 1: {ranking1}")
    print(f"Ranking 2: {ranking2}")
    print(f"Number of inversions: {inversions}")
    print(f"Similarity: {1 - inversions / (len(ranking1) * (len(ranking1) - 1) / 2):.2%}")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. Mergesort: Stable, O(n log n) worst-case")
    print("2. Divide: Split array in half")
    print("3. Conquer: Recursively sort both halves")
    print("4. Combine: Merge sorted halves")
    print("5. Inversion counting uses same structure with counting during merge")


if __name__ == "__main__":
    demonstrate_mergesort_inversions()
