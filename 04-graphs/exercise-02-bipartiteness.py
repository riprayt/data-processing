"""
Exercise 2: Bipartite Graph Detection
Determines if a graph is bipartite using BFS/DFS coloring
"""

from collections import deque, defaultdict


class Graph:
    """Graph representation using adjacency list"""
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an undirected edge between u and v"""
        self.graph[u].append(v)
        self.graph[v].append(u)


def is_bipartite_bfs(graph, start):
    """
    Check if graph is bipartite using BFS (2-coloring)
    
    A graph is bipartite if it can be colored with 2 colors such that
    no two adjacent vertices have the same color.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        Tuple (is_bipartite, coloring_dict)
    """
    color = {}
    queue = deque([start])
    color[start] = 0  # Color 0 or 1
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph.graph[node]:
            if neighbor not in color:
                # Color neighbor with opposite color
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                # Found edge between same-colored vertices
                return False, color
    
    # Check all components
    for node in graph.graph:
        if node not in color:
            # New component, start BFS from here
            queue = deque([node])
            color[node] = 0
            
            while queue:
                current = queue.popleft()
                for neighbor in graph.graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False, color
    
    return True, color


def is_bipartite_dfs(graph, start, color=None, current_color=0):
    """
    Check if graph is bipartite using DFS (recursive)
    
    Returns:
        Tuple (is_bipartite, coloring_dict)
    """
    if color is None:
        color = {}
    
    color[start] = current_color
    
    for neighbor in graph.graph[start]:
        if neighbor not in color:
            is_bip, _ = is_bipartite_dfs(graph, neighbor, color, 1 - current_color)
            if not is_bip:
                return False, color
        elif color[neighbor] == current_color:
            return False, color
    
    return True, color


def demonstrate_bipartiteness():
    """Demonstrate bipartite graph detection"""
    print("=" * 70)
    print("Bipartite Graph Detection")
    print("=" * 70)
    print("\nA graph is bipartite if vertices can be partitioned into two sets")
    print("such that no edge connects vertices in the same set.\n")
    
    # Example 1: Bipartite graph (even cycle)
    print("Example 1: Bipartite Graph (Even Cycle)")
    print("-" * 70)
    
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 0)
    
    print("Graph: 0-1-2-3-0 (4-cycle)")
    is_bip, coloring = is_bipartite_bfs(g1, 0)
    print(f"Is bipartite: {is_bip}")
    if is_bip:
        set0 = [node for node, c in coloring.items() if c == 0]
        set1 = [node for node, c in coloring.items() if c == 1]
        print(f"Partition: Set 0 = {set0}, Set 1 = {set1}")
    
    # Example 2: Non-bipartite graph (odd cycle)
    print("\n\nExample 2: Non-Bipartite Graph (Odd Cycle)")
    print("-" * 70)
    
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)  # Triangle (odd cycle)
    
    print("Graph: 0-1-2-0 (triangle)")
    is_bip, coloring = is_bipartite_bfs(g2, 0)
    print(f"Is bipartite: {is_bip}")
    if not is_bip:
        print("Reason: Contains odd-length cycle")
    
    # Example 3: Bipartite graph (tree)
    print("\n\nExample 3: Bipartite Graph (Tree)")
    print("-" * 70)
    
    g3 = Graph()
    g3.add_edge('A', 'B')
    g3.add_edge('A', 'C')
    g3.add_edge('B', 'D')
    g3.add_edge('B', 'E')
    g3.add_edge('C', 'F')
    
    print("Tree structure:")
    print("      A")
    print("    /   \\")
    print("   B     C")
    print("  / \\   /")
    print(" D   E F")
    
    is_bip, coloring = is_bipartite_bfs(g3, 'A')
    print(f"\nIs bipartite: {is_bip}")
    if is_bip:
        set0 = sorted([node for node, c in coloring.items() if c == 0])
        set1 = sorted([node for node, c in coloring.items() if c == 1])
        print(f"Partition: Set 0 = {set0}, Set 1 = {set1}")
    
    # Example 4: Complex bipartite graph
    print("\n\nExample 4: Complex Bipartite Graph")
    print("-" * 70)
    
    g4 = Graph()
    # Left side: {0, 1, 2}, Right side: {3, 4, 5}
    g4.add_edge(0, 3)
    g4.add_edge(0, 4)
    g4.add_edge(1, 4)
    g4.add_edge(1, 5)
    g4.add_edge(2, 3)
    g4.add_edge(2, 5)
    
    print("Bipartite graph with two partitions")
    is_bip, coloring = is_bipartite_bfs(g4, 0)
    print(f"Is bipartite: {is_bip}")
    if is_bip:
        set0 = sorted([node for node, c in coloring.items() if c == 0])
        set1 = sorted([node for node, c in coloring.items() if c == 1])
        print(f"Partition: Set 0 = {set0}, Set 1 = {set1}")
    
    # Example 5: Non-bipartite with multiple components
    print("\n\nExample 5: Graph with Multiple Components")
    print("-" * 70)
    
    g5 = Graph()
    # Component 1: bipartite
    g5.add_edge(0, 1)
    g5.add_edge(1, 2)
    # Component 2: non-bipartite (triangle)
    g5.add_edge(3, 4)
    g5.add_edge(4, 5)
    g5.add_edge(5, 3)
    
    print("Graph with two components (one bipartite, one not)")
    is_bip, coloring = is_bipartite_bfs(g5, 0)
    print(f"Is bipartite: {is_bip}")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. A graph is bipartite if and only if it has no odd-length cycles")
    print("2. All trees are bipartite")
    print("3. Even-length cycles are bipartite")
    print("4. Odd-length cycles are NOT bipartite")
    print("5. Can be checked in O(V + E) time using BFS/DFS")


if __name__ == "__main__":
    demonstrate_bipartiteness()
