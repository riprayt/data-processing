"""
Exercise 1: Gale-Shapley Algorithm Implementation
Implements the Gale-Shapley algorithm for the Stable Matching Problem
"""


def gale_shapley(men_preferences, women_preferences):
    """
    Implements the Gale-Shapley algorithm for stable matching.
    
    The algorithm finds a stable matching between two sets of equal size.
    A matching is stable if there is no pair (m, w) such that:
    - m prefers w over his current partner, AND
    - w prefers m over her current partner
    
    Time Complexity: O(n²) where n is the number of men/women
    Space Complexity: O(n²) for storing preferences
    
    Args:
        men_preferences: Dictionary mapping man -> list of women in order of preference
        women_preferences: Dictionary mapping woman -> list of men in order of preference
    
    Returns:
        Dictionary mapping woman -> man (the stable matching)
    """
    # Initialize: all men and women are free
    free_men = list(men_preferences.keys())
    engaged = {}  # woman -> man
    proposals = {man: 0 for man in free_men}  # Track how many proposals each man made
    
    # Create inverse preference lists for O(1) lookup
    # women_rankings[woman][man] = rank (lower is better)
    women_rankings = {}
    for woman, prefs in women_preferences.items():
        women_rankings[woman] = {man: rank for rank, man in enumerate(prefs)}
    
    # While there are free men who haven't proposed to all women
    while free_men:
        man = free_men[0]  # Get the first free man
        
        # If man has proposed to all women, skip (shouldn't happen in valid input)
        if proposals[man] >= len(men_preferences[man]):
            free_men.pop(0)
            continue
        
        # Get the next woman on man's preference list
        woman = men_preferences[man][proposals[man]]
        proposals[man] += 1
        
        if woman not in engaged:
            # Woman is free, engage them
            engaged[woman] = man
            free_men.pop(0)
        else:
            # Woman is engaged, check if she prefers this man
            current_man = engaged[woman]
            
            # Compare ranks (lower rank = higher preference)
            if women_rankings[woman][man] < women_rankings[woman][current_man]:
                # Woman prefers new man, break engagement and re-engage
                engaged[woman] = man
                free_men.pop(0)
                free_men.append(current_man)  # Previous man becomes free
            # Else: woman prefers current man, new man remains free and continues proposing
    
    return engaged


def is_stable_matching(matching, men_preferences, women_preferences):
    """
    Verifies if a given matching is stable.
    
    Args:
        matching: Dictionary mapping woman -> man
        men_preferences: Dictionary mapping man -> list of women in order of preference
        women_preferences: Dictionary mapping woman -> list of men in order of preference
    
    Returns:
        Tuple (is_stable, blocking_pairs)
        is_stable: Boolean indicating if matching is stable
        blocking_pairs: List of blocking pairs if not stable
    """
    # Create inverse matching (man -> woman)
    man_to_woman = {man: woman for woman, man in matching.items()}
    
    # Create inverse preference lists for efficient lookup
    women_rankings = {}
    for woman, prefs in women_preferences.items():
        women_rankings[woman] = {man: rank for rank, man in enumerate(prefs)}
    
    blocking_pairs = []
    
    # Check all possible pairs (man, woman)
    for man in men_preferences:
        current_woman = man_to_woman[man]
        man_rank_current = men_preferences[man].index(current_woman)
        
        for woman in women_preferences:
            if woman == current_woman:
                continue
            
            # Check if man prefers this woman over his current partner
            try:
                man_rank_woman = men_preferences[man].index(woman)
            except ValueError:
                continue  # Woman not in man's preference list
            
            if man_rank_woman < man_rank_current:
                # Man prefers woman over current partner
                current_man = matching[woman]
                
                # Check if woman prefers this man over her current partner
                if women_rankings[woman][man] < women_rankings[woman][current_man]:
                    # This is a blocking pair!
                    blocking_pairs.append((man, woman))
    
    return len(blocking_pairs) == 0, blocking_pairs


def print_matching(matching):
    """Pretty print a matching"""
    print("Stable Matching:")
    print("-" * 40)
    for woman, man in sorted(matching.items()):
        print(f"{woman} is matched with {man}")
    print()


def demonstrate_gale_shapley():
    """Demonstrate the Gale-Shapley algorithm with examples"""
    print("=" * 60)
    print("Gale-Shapley Algorithm Demonstration")
    print("=" * 60)
    
    # Example 1: Simple 2x2 case
    print("\nExample 1: Simple 2x2 Matching")
    print("-" * 60)
    
    men_prefs_1 = {
        'A': ['X', 'Y'],
        'B': ['Y', 'X']
    }
    
    women_prefs_1 = {
        'X': ['B', 'A'],
        'Y': ['A', 'B']
    }
    
    matching_1 = gale_shapley(men_prefs_1, women_prefs_1)
    print_matching(matching_1)
    
    is_stable, blocking = is_stable_matching(matching_1, men_prefs_1, women_prefs_1)
    print(f"Stability check: {'STABLE ✓' if is_stable else 'UNSTABLE ✗'}")
    if blocking:
        print(f"Blocking pairs: {blocking}")
    print()
    
    # Example 2: Classic 3x3 case
    print("\nExample 2: 3x3 Matching")
    print("-" * 60)
    
    men_prefs_2 = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'X', 'Z'],
        'C': ['X', 'Y', 'Z']
    }
    
    women_prefs_2 = {
        'X': ['B', 'A', 'C'],
        'Y': ['A', 'B', 'C'],
        'Z': ['A', 'B', 'C']
    }
    
    matching_2 = gale_shapley(men_prefs_2, women_prefs_2)
    print_matching(matching_2)
    
    is_stable, blocking = is_stable_matching(matching_2, men_prefs_2, women_prefs_2)
    print(f"Stability check: {'STABLE ✓' if is_stable else 'UNSTABLE ✗'}")
    if blocking:
        print(f"Blocking pairs: {blocking}")
    print()
    
    # Example 3: Larger 4x4 case
    print("\nExample 3: 4x4 Matching")
    print("-" * 60)
    
    men_prefs_3 = {
        'A': ['W', 'X', 'Y', 'Z'],
        'B': ['X', 'W', 'Z', 'Y'],
        'C': ['W', 'X', 'Y', 'Z'],
        'D': ['Y', 'Z', 'X', 'W']
    }
    
    women_prefs_3 = {
        'W': ['B', 'A', 'D', 'C'],
        'X': ['A', 'B', 'C', 'D'],
        'Y': ['A', 'B', 'C', 'D'],
        'Z': ['C', 'D', 'A', 'B']
    }
    
    matching_3 = gale_shapley(men_prefs_3, women_prefs_3)
    print_matching(matching_3)
    
    is_stable, blocking = is_stable_matching(matching_3, men_prefs_3, women_prefs_3)
    print(f"Stability check: {'STABLE ✓' if is_stable else 'UNSTABLE ✗'}")
    if blocking:
        print(f"Blocking pairs: {blocking}")
    print()


if __name__ == "__main__":
    demonstrate_gale_shapley()
