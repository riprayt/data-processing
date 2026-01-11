"""
Exercise 1: Polynomial Time Reductions
Demonstrates reductions between NP-complete problems
"""


def independent_set_brute_force(graph, k):
    """
    Independent Set: Find set of k vertices with no edges between them
    
    This is a brute force solution for demonstration.
    In practice, this is NP-complete.
    """
    from itertools import combinations
    
    vertices = list(graph.keys())
    
    for combo in combinations(vertices, k):
        is_independent = True
        for u in combo:
            for v in combo:
                if u != v and v in graph.get(u, []):
                    is_independent = False
                    break
            if not is_independent:
                break
        if is_independent:
            return True, list(combo)
    
    return False, []


def vertex_cover_brute_force(graph, k):
    """
    Vertex Cover: Find set of k vertices that cover all edges
    
    This is a brute force solution for demonstration.
    In practice, this is NP-complete.
    """
    from itertools import combinations
    
    vertices = list(graph.keys())
    edges = set()
    for u in graph:
        for v in graph[u]:
            edges.add(tuple(sorted([u, v])))
    
    for combo in combinations(vertices, k):
        covered_edges = set()
        for u in combo:
            for v in graph.get(u, []):
                covered_edges.add(tuple(sorted([u, v])))
        if len(covered_edges) == len(edges):
            return True, list(combo)
    
    return False, []


def independent_set_to_vertex_cover(graph, k):
    """
    Reduction: Independent Set ≤p Vertex Cover
    
    If G has an independent set of size k, then G has a vertex cover of size |V| - k
    """
    n = len(graph)
    cover_size = n - k
    
    if cover_size < 0:
        return False, []
    
    has_is, is_set = independent_set_brute_force(graph, k)
    
    if has_is:
        # Complement of independent set is vertex cover
        all_vertices = set(graph.keys())
        cover = list(all_vertices - set(is_set))
        return True, cover
    else:
        return False, []


def set_cover_brute_force(universe, subsets, k):
    """
    Set Cover: Find k subsets that cover the universe
    
    This is a brute force solution for demonstration.
    In practice, this is NP-complete.
    """
    from itertools import combinations
    
    for combo in combinations(range(len(subsets)), k):
        covered = set()
        for idx in combo:
            covered.update(subsets[idx])
        if covered == universe:
            return True, list(combo)
    
    return False, []


def vertex_cover_to_set_cover(graph, k):
    """
    Reduction: Vertex Cover ≤p Set Cover
    
    Each edge becomes an element, each vertex becomes a set of edges it covers
    """
    # Create universe (all edges)
    edges = []
    edge_to_idx = {}
    idx = 0
    
    for u in graph:
        for v in graph[u]:
            edge = tuple(sorted([u, v]))
            if edge not in edge_to_idx:
                edge_to_idx[edge] = idx
                edges.append(edge)
                idx += 1
    
    universe = set(range(len(edges)))
    
    # Each vertex covers a set of edges
    subsets = []
    vertices = list(graph.keys())
    
    for u in vertices:
        vertex_edges = set()
        for v in graph.get(u, []):
            edge = tuple(sorted([u, v]))
            if edge in edge_to_idx:
                vertex_edges.add(edge_to_idx[edge])
        subsets.append(vertex_edges)
    
    return set_cover_brute_force(universe, subsets, k)


def demonstrate_reductions():
    """Demonstrate polynomial time reductions"""
    print("=" * 70)
    print("Polynomial Time Reductions")
    print("=" * 70)
    print("\nReduction A ≤p B means: If we can solve B in polynomial time,")
    print("we can solve A in polynomial time.\n")
    
    # Example 1: Independent Set
    print("Example 1: Independent Set")
    print("-" * 70)
    
    graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C'],
    }
    
    print("Graph:")
    for u in graph1:
        print(f"  {u}: {graph1[u]}")
    
    k = 2
    has_is, is_set = independent_set_brute_force(graph1, k)
    
    print(f"\nIndependent set of size {k}:")
    if has_is:
        print(f"  Found: {is_set}")
    else:
        print(f"  Not found")
    
    # Example 2: Vertex Cover
    print("\n\nExample 2: Vertex Cover")
    print("-" * 70)
    
    k_vc = 2
    has_vc, vc_set = vertex_cover_brute_force(graph1, k_vc)
    
    print(f"Vertex cover of size {k_vc}:")
    if has_vc:
        print(f"  Found: {vc_set}")
    else:
        print(f"  Not found")
    
    # Example 3: Reduction IS to VC
    print("\n\nExample 3: Reduction: Independent Set ≤p Vertex Cover")
    print("-" * 70)
    
    k_is = 2
    has_vc_reduced, vc_reduced = independent_set_to_vertex_cover(graph1, k_is)
    
    print(f"Using reduction from IS (k={k_is}) to VC:")
    if has_vc_reduced:
        print(f"  Vertex cover found: {vc_reduced} (size {len(vc_reduced)})")
        print(f"  Note: VC size = |V| - IS size = {len(graph1)} - {k_is} = {len(vc_reduced)}")
    else:
        print(f"  No vertex cover found")
    
    # Example 4: Set Cover
    print("\n\nExample 4: Set Cover")
    print("-" * 70)
    
    universe = {1, 2, 3, 4, 5}
    subsets = [
        {1, 2, 3},
        {2, 4},
        {3, 4, 5},
        {1, 5},
    ]
    
    print(f"Universe: {universe}")
    print("Subsets:")
    for i, subset in enumerate(subsets):
        print(f"  S{i}: {subset}")
    
    k_sc = 2
    has_sc, sc_sets = set_cover_brute_force(universe, subsets, k_sc)
    
    print(f"\nSet cover of size {k_sc}:")
    if has_sc:
        print(f"  Found: Sets {sc_sets}")
        print(f"  Coverage: {set().union(*[subsets[i] for i in sc_sets])}")
    else:
        print(f"  Not found")
    
    # Example 5: Reduction VC to SC
    print("\n\nExample 5: Reduction: Vertex Cover ≤p Set Cover")
    print("-" * 70)
    
    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
    }
    
    k_vc2 = 2
    has_sc_reduced, sc_reduced = vertex_cover_to_set_cover(graph2, k_vc2)
    
    print(f"Using reduction from VC (k={k_vc2}) to Set Cover:")
    if has_sc_reduced:
        print(f"  Set cover found: Sets {sc_reduced}")
    else:
        print(f"  No set cover found")
    
    print("\n" + "=" * 70)
    print("Key Concepts:")
    print("=" * 70)
    print("1. Reduction A ≤p B: A is 'at least as easy' as B")
    print("2. If B is in P, then A is in P")
    print("3. If A is NP-hard, then B is NP-hard")
    print("4. Common reductions:")
    print("   - Independent Set ≤p Vertex Cover")
    print("   - Vertex Cover ≤p Set Cover")
    print("   - 3-SAT ≤p Independent Set")
    print("5. All NP-complete problems are reducible to each other")


if __name__ == "__main__":
    demonstrate_reductions()
