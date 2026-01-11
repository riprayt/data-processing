"""
Exercise 4: Minimum Spanning Tree Algorithms
Implements Prim's and Kruskal's algorithms for MST
"""

import heapq
from collections import defaultdict


class Graph:
    """Weighted undirected graph representation"""
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = []  # List of all edges (u, v, weight)
    
    def add_edge(self, u, v, weight):
        """Add a weighted undirected edge"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        self.edges.append((u, v, weight))


class UnionFind:
    """Union-Find data structure for Kruskal's algorithm"""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True


def prim_mst(graph, start):
    """
    Prim's algorithm for Minimum Spanning Tree
    
    Greedy strategy: Always add the minimum-weight edge connecting
    a vertex in the MST to a vertex outside
    
    Time Complexity: O((V + E) log V) with binary heap
    Space Complexity: O(V)
    
    Returns:
        List of edges in the MST
    """
    mst_edges = []
    visited = {start}
    pq = []  # Priority queue: (weight, u, v)
    
    # Initialize with edges from start
    for neighbor, weight in graph.graph[start]:
        heapq.heappush(pq, (weight, start, neighbor))
    
    while pq and len(visited) < len(graph.graph):
        weight, u, v = heapq.heappop(pq)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst_edges.append((u, v, weight))
        
        # Add edges from v to unvisited vertices
        for neighbor, edge_weight in graph.graph[v]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, v, neighbor))
    
    return mst_edges


def kruskal_mst(graph):
    """
    Kruskal's algorithm for Minimum Spanning Tree
    
    Greedy strategy: Sort edges by weight, add edges that don't create cycles
    
    Time Complexity: O(E log E) = O(E log V)
    Space Complexity: O(V)
    
    Returns:
        List of edges in the MST
    """
    # Sort edges by weight
    sorted_edges = sorted(graph.edges, key=lambda x: x[2])
    
    # Create mapping from vertex to index
    vertices = set()
    for u, v, _ in sorted_edges:
        vertices.add(u)
        vertices.add(v)
    
    vertex_to_idx = {v: i for i, v in enumerate(sorted(vertices))}
    idx_to_vertex = {i: v for v, i in vertex_to_idx.items()}
    
    uf = UnionFind(len(vertices))
    mst_edges = []
    
    for u, v, weight in sorted_edges:
        u_idx = vertex_to_idx[u]
        v_idx = vertex_to_idx[v]
        
        if uf.union(u_idx, v_idx):
            mst_edges.append((u, v, weight))
            
            # Stop when we have V-1 edges
            if len(mst_edges) == len(vertices) - 1:
                break
    
    return mst_edges


def demonstrate_mst():
    """Demonstrate MST algorithms"""
    print("=" * 70)
    print("Minimum Spanning Tree Algorithms")
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
    
    print("Graph edges:")
    for u, v, w in g1.edges:
        print(f"  {u} --{w}-- {v}")
    
    prim_edges = prim_mst(g1, 'A')
    kruskal_edges = kruskal_mst(g1)
    
    prim_weight = sum(w for _, _, w in prim_edges)
    kruskal_weight = sum(w for _, _, w in kruskal_edges)
    
    print(f"\nPrim's MST (starting from A):")
    for u, v, w in prim_edges:
        print(f"  {u} --{w}-- {v}")
    print(f"  Total weight: {prim_weight}")
    
    print(f"\nKruskal's MST:")
    for u, v, w in kruskal_edges:
        print(f"  {u} --{w}-- {v}")
    print(f"  Total weight: {kruskal_weight}")
    
    # Example 2: Larger graph
    print("\n\nExample 2: Larger Graph")
    print("-" * 70)
    
    g2 = Graph()
    edges = [
        (0, 1, 7), (0, 3, 5),
        (1, 2, 8), (1, 3, 9), (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15), (3, 5, 6),
        (4, 5, 8), (4, 6, 9),
        (5, 6, 11),
    ]
    
    for u, v, w in edges:
        g2.add_edge(u, v, w)
    
    prim_edges = prim_mst(g2, 0)
    kruskal_edges = kruskal_mst(g2)
    
    prim_weight = sum(w for _, _, w in prim_edges)
    kruskal_weight = sum(w for _, _, w in kruskal_edges)
    
    print(f"Prim's MST weight: {prim_weight}")
    print(f"Kruskal's MST weight: {kruskal_weight}")
    print(f"Both algorithms produce MST with same weight: {prim_weight == kruskal_weight}")
    
    # Example 3: Network design
    print("\n\nExample 3: Network Design Application")
    print("-" * 70)
    
    g3 = Graph()
    # Cities and connection costs
    g3.add_edge('NYC', 'Boston', 200)
    g3.add_edge('NYC', 'DC', 225)
    g3.add_edge('NYC', 'Chicago', 800)
    g3.add_edge('Boston', 'Chicago', 1000)
    g3.add_edge('DC', 'Atlanta', 600)
    g3.add_edge('Chicago', 'Denver', 1000)
    g3.add_edge('Chicago', 'Atlanta', 700)
    g3.add_edge('Atlanta', 'Miami', 650)
    g3.add_edge('Denver', 'LA', 1000)
    g3.add_edge('Denver', 'Seattle', 1300)
    g3.add_edge('LA', 'Seattle', 1100)
    
    mst_edges = kruskal_mst(g3)
    total_cost = sum(w for _, _, w in mst_edges)
    
    print("Minimum cost network connecting all cities:")
    for u, v, w in sorted(mst_edges):
        print(f"  {u} -- ${w} -- {v}")
    print(f"\nTotal cost: ${total_cost}")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. Both algorithms find the same MST (may have different edges)")
    print("2. Prim's: Start from a vertex, grow the tree")
    print("3. Kruskal's: Sort edges, add if no cycle")
    print("4. MST has exactly V-1 edges for V vertices")
    print("5. Applications: Network design, clustering, approximation algorithms")


if __name__ == "__main__":
    demonstrate_mst()
