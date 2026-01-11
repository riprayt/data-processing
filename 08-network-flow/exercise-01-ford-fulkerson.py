"""
Exercise 1: Ford-Fulkerson Algorithm
Maximum flow and minimum cut using Ford-Fulkerson algorithm
"""

from collections import deque, defaultdict


class Graph:
    """Flow network representation"""
    
    def __init__(self):
        self.graph = defaultdict(dict)  # graph[u][v] = capacity
    
    def add_edge(self, u, v, capacity):
        """Add a directed edge with capacity"""
        self.graph[u][v] = capacity
        # Add reverse edge with 0 capacity if not exists
        if v not in self.graph:
            self.graph[v] = {}
        if u not in self.graph[v]:
            self.graph[v][u] = 0
    
    def get_neighbors(self, u):
        """Get all neighbors of vertex u"""
        return list(self.graph[u].keys())


def bfs_path(graph, source, sink, parent):
    """
    BFS to find augmenting path in residual graph
    
    Returns:
        True if path exists, False otherwise
    """
    visited = set()
    queue = deque([source])
    visited.add(source)
    parent[source] = None
    
    while queue:
        u = queue.popleft()
        
        for v in graph.get_neighbors(u):
            if v not in visited and graph.graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                queue.append(v)
                
                if v == sink:
                    return True
    
    return False


def ford_fulkerson(graph, source, sink):
    """
    Ford-Fulkerson algorithm for maximum flow
    
    Time Complexity: O(E * max_flow) in worst case
    Better with BFS (Edmonds-Karp): O(V * E²)
    
    Args:
        graph: Graph object representing flow network
        source: Source vertex
        sink: Sink vertex
    
    Returns:
        Tuple (max_flow, flow_graph)
        flow_graph: Dictionary representing actual flow on each edge
    """
    # Create residual graph (initially same as original)
    residual = Graph()
    for u in graph.graph:
        for v, capacity in graph.graph[u].items():
            residual.add_edge(u, v, capacity)
    
    max_flow = 0
    parent = {}
    
    # Find augmenting paths while they exist
    while bfs_path(residual, source, sink, parent):
        # Find minimum capacity along path
        path_flow = float('inf')
        v = sink
        
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual.graph[u][v])
            v = u
        
        # Update residual graph
        v = sink
        while v != source:
            u = parent[v]
            residual.graph[u][v] -= path_flow
            residual.graph[v][u] += path_flow
            v = u
        
        max_flow += path_flow
    
    # Reconstruct actual flow
    flow_graph = defaultdict(dict)
    for u in graph.graph:
        for v in graph.graph[u]:
            original_capacity = graph.graph[u][v]
            residual_capacity = residual.graph[u][v]
            actual_flow = original_capacity - residual_capacity
            if actual_flow > 0:
                flow_graph[u][v] = actual_flow
    
    return max_flow, flow_graph


def min_cut(graph, source, sink):
    """
    Find minimum cut using max-flow min-cut theorem
    
    After finding max flow, min cut is the set of vertices reachable from source
    in the residual graph.
    """
    max_flow, flow_graph = ford_fulkerson(graph, source, sink)
    
    # Find reachable vertices from source in residual graph
    residual = Graph()
    for u in graph.graph:
        for v, capacity in graph.graph[u].items():
            residual.add_edge(u, v, capacity)
    
    # Update residual based on flow
    for u in flow_graph:
        for v, flow in flow_graph[u].items():
            residual.graph[u][v] -= flow
            residual.graph[v][u] += flow
    
    # BFS to find reachable vertices
    reachable = set()
    queue = deque([source])
    reachable.add(source)
    
    while queue:
        u = queue.popleft()
        for v in residual.get_neighbors(u):
            if v not in reachable and residual.graph[u][v] > 0:
                reachable.add(v)
                queue.append(v)
    
    # Find edges in the cut
    cut_edges = []
    for u in reachable:
        for v in graph.graph[u]:
            if v not in reachable:
                cut_edges.append((u, v))
    
    return max_flow, reachable, cut_edges


def demonstrate_ford_fulkerson():
    """Demonstrate Ford-Fulkerson algorithm"""
    print("=" * 70)
    print("Ford-Fulkerson Algorithm for Maximum Flow")
    print("=" * 70)
    
    # Example 1: Simple network
    print("\nExample 1: Simple Flow Network")
    print("-" * 70)
    
    g1 = Graph()
    g1.add_edge('s', 'A', 10)
    g1.add_edge('s', 'B', 5)
    g1.add_edge('A', 'B', 15)
    g1.add_edge('A', 't', 10)
    g1.add_edge('B', 't', 10)
    
    print("Network:")
    print("  s --10--> A --10--> t")
    print("  |         |")
    print("  5         15")
    print("  |         |")
    print("  v         v")
    print("  B --10--> t")
    
    max_flow, flow_graph = ford_fulkerson(g1, 's', 't')
    
    print(f"\nMaximum flow: {max_flow}")
    print("Flow on edges:")
    for u in sorted(flow_graph.keys()):
        for v in sorted(flow_graph[u].keys()):
            print(f"  {u} -> {v}: {flow_graph[u][v]}")
    
    # Example 2: Min cut
    print("\n\nExample 2: Minimum Cut")
    print("-" * 70)
    
    g2 = Graph()
    g2.add_edge('s', '1', 16)
    g2.add_edge('s', '2', 13)
    g2.add_edge('1', '2', 10)
    g2.add_edge('1', '3', 12)
    g2.add_edge('2', '1', 4)
    g2.add_edge('2', '4', 14)
    g2.add_edge('3', '2', 9)
    g2.add_edge('3', 't', 20)
    g2.add_edge('4', '3', 7)
    g2.add_edge('4', 't', 4)
    
    max_flow, reachable, cut_edges = min_cut(g2, 's', 't')
    
    print(f"Maximum flow: {max_flow}")
    print(f"Reachable vertices from s: {sorted(reachable)}")
    print(f"Minimum cut edges: {cut_edges}")
    print(f"Cut capacity: {sum(g2.graph[u][v] for u, v in cut_edges)}")
    print(f"Max-flow = Min-cut: {max_flow == sum(g2.graph[u][v] for u, v in cut_edges)}")
    
    # Example 3: Bipartite matching application
    print("\n\nExample 3: Bipartite Matching via Max Flow")
    print("-" * 70)
    
    g3 = Graph()
    # Left side: {1, 2, 3}, Right side: {4, 5, 6}
    # Connect source to left, right to sink
    g3.add_edge('s', '1', 1)
    g3.add_edge('s', '2', 1)
    g3.add_edge('s', '3', 1)
    g3.add_edge('1', '4', 1)
    g3.add_edge('1', '5', 1)
    g3.add_edge('2', '4', 1)
    g3.add_edge('2', '6', 1)
    g3.add_edge('3', '5', 1)
    g3.add_edge('3', '6', 1)
    g3.add_edge('4', 't', 1)
    g3.add_edge('5', 't', 1)
    g3.add_edge('6', 't', 1)
    
    max_flow, flow_graph = ford_fulkerson(g3, 's', 't')
    
    print(f"Maximum matching size: {max_flow}")
    print("Matched pairs:")
    for u in flow_graph:
        if u != 's':
            for v in flow_graph[u]:
                if v != 't' and flow_graph[u][v] > 0:
                    print(f"  {u} <-> {v}")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. Ford-Fulkerson finds maximum flow in a network")
    print("2. Max-flow min-cut theorem: max flow = min cut capacity")
    print("3. Uses augmenting paths in residual graph")
    print("4. With BFS (Edmonds-Karp): O(V * E²) time")
    print("5. Applications: Network routing, bipartite matching, image segmentation")


if __name__ == "__main__":
    demonstrate_ford_fulkerson()
