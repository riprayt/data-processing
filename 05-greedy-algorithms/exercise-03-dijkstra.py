"""
Exercise 3: Dijkstra's Shortest Path Algorithm
Finds shortest paths from a source vertex to all other vertices
"""

import heapq
from collections import defaultdict


class Graph:
    """Weighted graph representation"""
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        """Add a weighted directed edge from u to v"""
        self.graph[u].append((v, weight))
    
    def add_undirected_edge(self, u, v, weight):
        """Add a weighted undirected edge"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))


def dijkstra(graph, start):
    """
    Dijkstra's algorithm for shortest paths
    
    Time Complexity: O((V + E) log V) with binary heap
    Space Complexity: O(V)
    
    Args:
        graph: Graph object
        start: Starting vertex
    
    Returns:
        Tuple (distances, previous)
        distances: Dict mapping vertex -> shortest distance from start
        previous: Dict mapping vertex -> previous vertex in shortest path
    """
    distances = {start: 0}
    previous = {}
    pq = [(0, start)]  # Priority queue: (distance, vertex)
    visited = set()
    
    # Initialize distances
    all_nodes = set(graph.graph.keys())
    for node in graph.graph.values():
        for neighbor, _ in node:
            all_nodes.add(neighbor)
    
    for node in all_nodes:
        if node != start:
            distances[node] = float('inf')
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor, weight in graph.graph[current]:
            if neighbor in visited:
                continue
            
            new_dist = current_dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances, previous


def reconstruct_path(previous, start, end):
    """
    Reconstruct shortest path from start to end
    
    Returns:
        List of vertices representing the path, or None if no path exists
    """
    if end not in previous and end != start:
        return None
    
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous.get(current)
        if current == start:
            path.append(start)
            break
    
    return path[::-1] if path else None


def demonstrate_dijkstra():
    """Demonstrate Dijkstra's algorithm"""
    print("=" * 70)
    print("Dijkstra's Shortest Path Algorithm")
    print("=" * 70)
    
    # Example 1: Simple graph
    print("\nExample 1: Simple Weighted Graph")
    print("-" * 70)
    
    g1 = Graph()
    g1.add_edge('A', 'B', 4)
    g1.add_edge('A', 'C', 2)
    g1.add_edge('B', 'C', 1)
    g1.add_edge('B', 'D', 5)
    g1.add_edge('C', 'D', 8)
    g1.add_edge('C', 'E', 10)
    g1.add_edge('D', 'E', 2)
    g1.add_edge('E', 'D', 3)
    
    print("Graph:")
    print("  A --4--> B --5--> D")
    print("  |        |        |")
    print("  2        1        2")
    print("  |        |        |")
    print("  v        v        v")
    print("  C --8--> D --3--> E")
    print("  |        ^")
    print("  10       |")
    print("  |        |")
    print("  v        |")
    print("  E -------+")
    
    distances, previous = dijkstra(g1, 'A')
    
    print(f"\nShortest distances from A:")
    for node in sorted(distances.keys()):
        dist = distances[node]
        if dist == float('inf'):
            print(f"  {node}: No path")
        else:
            path = reconstruct_path(previous, 'A', node)
            print(f"  {node}: {dist} (path: {' -> '.join(path)})")
    
    # Example 2: Grid-like graph
    print("\n\nExample 2: Grid Graph")
    print("-" * 70)
    
    g2 = Graph()
    # Create a 3x3 grid
    edges = [
        (0, 1, 1), (0, 3, 2),
        (1, 2, 3), (1, 4, 1),
        (2, 5, 2),
        (3, 4, 1), (3, 6, 3),
        (4, 5, 2), (4, 7, 1),
        (5, 8, 1),
        (6, 7, 2),
        (7, 8, 1),
    ]
    
    for u, v, w in edges:
        g2.add_undirected_edge(u, v, w)
    
    distances, previous = dijkstra(g2, 0)
    
    print("Shortest distances from vertex 0:")
    for node in sorted(distances.keys()):
        if distances[node] != float('inf'):
            path = reconstruct_path(previous, 0, node)
            print(f"  {node}: distance {distances[node]}, path: {path}")
    
    # Example 3: Network routing
    print("\n\nExample 3: Network Routing Application")
    print("-" * 70)
    
    g3 = Graph()
    # Network nodes with latency
    g3.add_undirected_edge('Router1', 'Router2', 5)
    g3.add_undirected_edge('Router1', 'Router3', 3)
    g3.add_undirected_edge('Router2', 'Router4', 2)
    g3.add_undirected_edge('Router2', 'Router5', 6)
    g3.add_undirected_edge('Router3', 'Router4', 1)
    g3.add_undirected_edge('Router3', 'Router6', 4)
    g3.add_undirected_edge('Router4', 'Router5', 3)
    g3.add_undirected_edge('Router5', 'Router6', 2)
    
    source = 'Router1'
    target = 'Router6'
    
    distances, previous = dijkstra(g3, source)
    path = reconstruct_path(previous, source, target)
    
    print(f"Shortest path from {source} to {target}:")
    print(f"  Path: {' -> '.join(path)}")
    print(f"  Total latency: {distances[target]}")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. Works only with non-negative edge weights")
    print("2. Finds shortest paths from source to all vertices")
    print("3. Uses greedy strategy: always process closest unvisited vertex")
    print("4. Time complexity: O((V + E) log V) with binary heap")
    print("5. Applications: GPS navigation, network routing, social networks")


if __name__ == "__main__":
    demonstrate_dijkstra()
