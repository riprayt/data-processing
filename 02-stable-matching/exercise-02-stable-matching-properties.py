"""
Exercise 2: Stable Matching Properties
Demonstrates key properties of stable matchings and the Gale-Shapley algorithm
"""


def find_all_stable_matchings(men_preferences, women_preferences):
    """
    Finds all possible stable matchings (brute force approach).
    
    Note: This is computationally expensive and only practical for small inputs.
    For n men and n women, there are n! possible matchings to check.
    
    Time Complexity: O(n! * n²) - exponential!
    
    Args:
        men_preferences: Dictionary mapping man -> list of women in order of preference
        women_preferences: Dictionary mapping woman -> list of men in order of preference
    
    Returns:
        List of all stable matchings (each is a dict: woman -> man)
    """
    from itertools import permutations
    
    men = list(men_preferences.keys())
    women = list(women_preferences.keys())
    
    if len(men) != len(women):
        return []
    
    stable_matchings = []
    
    # Generate all possible matchings
    # Permute men and assign each woman to a different man
    for perm in permutations(men):
        matching = {women[i]: perm[i] for i in range(len(women))}
        
        # Check if this matching is stable
        is_stable, _ = is_stable_matching(matching, men_preferences, women_preferences)
        if is_stable:
            stable_matchings.append(matching)
    
    return stable_matchings


def is_stable_matching(matching, men_preferences, women_preferences):
    """Helper function to check if a matching is stable"""
    man_to_woman = {man: woman for woman, man in matching.items()}
    
    women_rankings = {}
    for woman, prefs in women_preferences.items():
        women_rankings[woman] = {man: rank for rank, man in enumerate(prefs)}
    
    for man in men_preferences:
        current_woman = man_to_woman[man]
        man_rank_current = men_preferences[man].index(current_woman)
        
        for woman in women_preferences:
            if woman == current_woman:
                continue
            
            try:
                man_rank_woman = men_preferences[man].index(woman)
            except ValueError:
                continue
            
            if man_rank_woman < man_rank_current:
                current_man = matching[woman]
                if women_rankings[woman][man] < women_rankings[woman][current_man]:
                    return False, [(man, woman)]
    
    return True, []


def gale_shapley(men_preferences, women_preferences):
    """
    Gale-Shapley algorithm for stable matching.
    
    Args:
        men_preferences: Dictionary mapping man -> list of women in order of preference
        women_preferences: Dictionary mapping woman -> list of men in order of preference
    
    Returns:
        Dictionary mapping woman -> man (the stable matching)
    """
    free_men = list(men_preferences.keys())
    engaged = {}
    proposals = {man: 0 for man in free_men}
    
    women_rankings = {}
    for woman, prefs in women_preferences.items():
        women_rankings[woman] = {man: rank for rank, man in enumerate(prefs)}
    
    while free_men:
        man = free_men[0]
        
        if proposals[man] >= len(men_preferences[man]):
            free_men.pop(0)
            continue
        
        woman = men_preferences[man][proposals[man]]
        proposals[man] += 1
        
        if woman not in engaged:
            engaged[woman] = man
            free_men.pop(0)
        else:
            current_man = engaged[woman]
            if women_rankings[woman][man] < women_rankings[woman][current_man]:
                engaged[woman] = man
                free_men.pop(0)
                free_men.append(current_man)
    
    return engaged


def compare_matchings(matching1, matching2, men_preferences, women_preferences):
    """
    Compares two matchings to see which is better for men vs women.
    
    Returns:
        Dictionary with comparison metrics
    """
    def calculate_average_rank(matching, preferences, is_men=True):
        """Calculate average preference rank in a matching"""
        total_rank = 0
        count = 0
        
        if is_men:
            # For men: how well did they do?
            man_to_woman = {man: woman for woman, man in matching.items()}
            for man, woman in man_to_woman.items():
                rank = preferences[man].index(woman)
                total_rank += rank
                count += 1
        else:
            # For women: how well did they do?
            for woman, man in matching.items():
                rank = preferences[woman].index(man)
                total_rank += rank
                count += 1
        
        return total_rank / count if count > 0 else 0
    
    return {
        'men_avg_rank_1': calculate_average_rank(matching1, men_preferences, True),
        'men_avg_rank_2': calculate_average_rank(matching2, men_preferences, True),
        'women_avg_rank_1': calculate_average_rank(matching1, women_preferences, False),
        'women_avg_rank_2': calculate_average_rank(matching2, women_preferences, False),
    }


def demonstrate_properties():
    """Demonstrate key properties of stable matchings"""
    print("=" * 60)
    print("Stable Matching Properties Demonstration")
    print("=" * 60)
    
    # Property 1: Uniqueness (or lack thereof)
    print("\nProperty 1: Multiple Stable Matchings")
    print("-" * 60)
    
    men_prefs = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'Z', 'X'],
        'C': ['Z', 'X', 'Y']
    }
    
    women_prefs = {
        'X': ['A', 'B', 'C'],
        'Y': ['B', 'C', 'A'],
        'Z': ['C', 'A', 'B']
    }
    
    print("Men preferences:")
    for man, prefs in men_prefs.items():
        print(f"  {man}: {prefs}")
    print("\nWomen preferences:")
    for woman, prefs in women_prefs.items():
        print(f"  {woman}: {prefs}")
    
    # Find all stable matchings
    all_stable = find_all_stable_matchings(men_prefs, women_prefs)
    print(f"\nNumber of stable matchings: {len(all_stable)}")
    
    for i, matching in enumerate(all_stable, 1):
        print(f"\nStable matching {i}:")
        for woman, man in sorted(matching.items()):
            print(f"  {woman} <-> {man}")
    
    # Property 2: Man-optimal vs Woman-optimal
    print("\n\nProperty 2: Man-Optimal vs Woman-Optimal Matching")
    print("-" * 60)
    
    # Man-optimal: Run Gale-Shapley with men proposing
    man_optimal = gale_shapley(men_prefs, women_prefs)
    
    # Woman-optimal: Run Gale-Shapley with women proposing (swap roles)
    woman_optimal = gale_shapley(women_prefs, men_prefs)
    # Swap back: woman_optimal maps men -> women, we need women -> men
    woman_optimal = {woman: man for man, woman in woman_optimal.items()}
    
    print("Man-optimal matching (men propose):")
    for woman, man in sorted(man_optimal.items()):
        print(f"  {woman} <-> {man}")
    
    print("\nWoman-optimal matching (women propose):")
    for woman, man in sorted(woman_optimal.items()):
        print(f"  {woman} <-> {man}")
    
    # Compare the two
    comparison = compare_matchings(man_optimal, woman_optimal, men_prefs, women_prefs)
    print("\nComparison:")
    print(f"  Men's average rank in man-optimal: {comparison['men_avg_rank_1']:.2f}")
    print(f"  Men's average rank in woman-optimal: {comparison['men_avg_rank_2']:.2f}")
    print(f"  Women's average rank in man-optimal: {comparison['women_avg_rank_1']:.2f}")
    print(f"  Women's average rank in woman-optimal: {comparison['women_avg_rank_2']:.2f}")
    
    # Property 3: Stability guarantee
    print("\n\nProperty 3: Gale-Shapley Always Produces Stable Matching")
    print("-" * 60)
    
    # Test with various preference configurations
    test_cases = [
        {
            'name': 'Case 1: All agree',
            'men': {'A': ['X', 'Y'], 'B': ['X', 'Y']},
            'women': {'X': ['A', 'B'], 'Y': ['A', 'B']}
        },
        {
            'name': 'Case 2: Complete disagreement',
            'men': {'A': ['X', 'Y'], 'B': ['Y', 'X']},
            'women': {'X': ['B', 'A'], 'Y': ['A', 'B']}
        }
    ]
    
    for case in test_cases:
        print(f"\n{case['name']}:")
        matching = gale_shapley(case['men'], case['women'])
        is_stable, blocking = is_stable_matching(matching, case['men'], case['women'])
        print(f"  Result: {'STABLE ✓' if is_stable else 'UNSTABLE ✗'}")
        for woman, man in sorted(matching.items()):
            print(f"    {woman} <-> {man}")


if __name__ == "__main__":
    demonstrate_properties()
