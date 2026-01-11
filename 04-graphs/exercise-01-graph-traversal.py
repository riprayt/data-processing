"""
Exercise 1: Graph Traversal (BFS and DFS)
Implements Breadth-First Search and Depth-First Search algorithms
"""

from collections import deque, defaultdict


class Graph:
    """Simple graph representation using adjacency list"""
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an undirected edge between u and v"""
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def add_directed_edge(self, u, v):
        """Add a directed edge from u to v"""
        self.graph[u].append(v)


def bfs(graph, start):
    """
    Breadth-First Search
    
    Time Complexity: O(V + E) where V is vertices, E is edges
    Space Complexity: O(V)
    
    Returns:
        Dictionary mapping node -> distance from start
    """
    visited = set()
    distance = {}
    queue = deque([start])
    visited.add(start)
    distance[start] = 0
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    return distance


def dfs(graph, start):
    """
    Depth-First Search (iterative)
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        Set of visited nodes
    """
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph.graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited


def dfs_recursive(graph, start, visited=None):
    """
    Depth-First Search (recursive)
    
    Time Complexity: O(V + E)
    Space Complexity: O(V) for recursion stack
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    for neighbor in graph.graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited


def find_path_bfs(graph, start, end):
    """
    Find shortest path using BFS
    
    Returns:
        List representing the path from start to end, or None if no path exists
    """
    if start == end:
        return [start]
    
    visited = set()
    parent = {}
    queue = deque([start])
    visited.add(start)
    parent[start] = None
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            # Reconstruct path
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor in graph.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)
    
    return None  # No path found


def demonstrate_traversal():
    """Demonstrate BFS and DFS algorithms"""
    print("=" * 70)
    print("Graph Traversal: BFS and DFS")
    print("=" * 70)
    
    # Example 1: Simple undirected graph
    print("\nExample 1: Simple Graph")
    print("-" * 70)
    
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 4)
    
    print("Graph structure:")
    print("  0 -- 1 -- 3")
    print("  |         |")
    print("  2 -------- 4")
    
    print("\nBFS starting from 0:")
    distances = bfs(g1, 0)
    for node, dist in sorted(distances.items()):
        print(f"  Node {node}: distance {dist}")
    
    print("\nDFS (iterative) starting from 0:")
    visited = dfs(g1, 0)
    print(f"  Visited nodes: {sorted(visited)}")
    
    print("\nDFS (recursive) starting from 0:")
    visited_rec = dfs_recursive(g1, 0)
    print(f"  Visited nodes: {sorted(visited_rec)}")
    
    # Example 2: Path finding
    print("\n\nExample 2: Shortest Path Finding")
    print("-" * 70)
    
    g2 = Graph()
    g2.add_edge('A', 'B')
    g2.add_edge('A', 'C')
    g2.add_edge('B', 'D')
    g2.add_edge('B', 'E')
    g2.add_edge('C', 'F')
    g2.add_edge('D', 'G')
    g2.add_edge('E', 'G')
    g2.add_edge('F', 'G')
    
    print("Finding shortest path from A to G:")
    path = find_path_bfs(g2, 'A', 'G')
    if path:
        print(f"  Path: {' -> '.join(path)}")
        print(f"  Length: {len(path) - 1} edges")
    else:
        print("  No path found")
    
    # Example 3: Larger graph
    print("\n\nExample 3: Larger Graph")
    print("-" * 70)
    
    g3 = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
    for u, v in edges:
        g3.add_edge(u, v)
    
    print("BFS traversal from node 1:")
    distances = bfs(g3, 1)
    for node in sorted(distances.keys()):
        print(f"  Node {node}: distance {distances[node]}")
    
    print("\n" + "=" * 70)
    print("Key Differences:")
    print("=" * 70)
    print("1. BFS uses a queue (FIFO), explores level by level")
    print("2. DFS uses a stack (LIFO), explores as deep as possible")
    print("3. BFS finds shortest path in unweighted graphs")
    print("4. DFS uses less memory but may not find shortest path")
    print("5. Both have O(V + E) time complexity")


if __name__ == "__main__":
    demonstrate_traversal()
