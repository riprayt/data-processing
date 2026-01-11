"""
Exercise 3: Topological Ordering
Finds topological order of a directed acyclic graph (DAG)
"""

from collections import deque, defaultdict


class Graph:
    """Directed graph representation"""
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
    
    def add_edge(self, u, v):
        """Add a directed edge from u to v"""
        self.graph[u].append(v)
        if u not in self.in_degree:
            self.in_degree[u] = 0
        self.in_degree[v] = self.in_degree.get(v, 0) + 1
    
    def get_all_nodes(self):
        """Get all nodes in the graph"""
        nodes = set(self.graph.keys())
        for neighbors in self.graph.values():
            nodes.update(neighbors)
        return nodes


def topological_sort_kahn(graph):
    """
    Topological sort using Kahn's algorithm (BFS-based)
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List representing topological order, or None if cycle exists
    """
    in_degree = graph.in_degree.copy()
    all_nodes = graph.get_all_nodes()
    
    # Initialize in-degree for nodes with no incoming edges
    for node in all_nodes:
        if node not in in_degree:
            in_degree[node] = 0
    
    # Queue for nodes with no incoming edges
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # Reduce in-degree of neighbors
        for neighbor in graph.graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all nodes were processed (no cycle)
    if len(result) == len(all_nodes):
        return result
    else:
        return None  # Cycle exists


def topological_sort_dfs(graph):
    """
    Topological sort using DFS
    
    Time Complexity: O(V + E)
    Space Complexity: O(V) for recursion stack
    
    Returns:
        List representing topological order, or None if cycle exists
    """
    all_nodes = graph.get_all_nodes()
    visited = set()
    temp_mark = set()  # For cycle detection
    result = []
    
    def visit(node):
        if node in temp_mark:
            # Cycle detected
            return False
        if node in visited:
            return True
        
        temp_mark.add(node)
        for neighbor in graph.graph[node]:
            if not visit(neighbor):
                return False
        temp_mark.remove(node)
        visited.add(node)
        result.append(node)
        return True
    
    for node in all_nodes:
        if node not in visited:
            if not visit(node):
                return None  # Cycle exists
    
    return result[::-1]  # Reverse to get correct order


def demonstrate_topological_sort():
    """Demonstrate topological sorting"""
    print("=" * 70)
    print("Topological Ordering")
    print("=" * 70)
    print("\nTopological order: Linear ordering of vertices such that for every")
    print("directed edge (u, v), u comes before v in the ordering.\n")
    
    # Example 1: Course prerequisites
    print("Example 1: Course Prerequisites")
    print("-" * 70)
    
    g1 = Graph()
    # CS101 -> CS201 -> CS301
    # MATH101 -> CS201
    # CS201 -> CS302
    g1.add_edge('CS101', 'CS201')
    g1.add_edge('MATH101', 'CS201')
    g1.add_edge('CS201', 'CS301')
    g1.add_edge('CS201', 'CS302')
    
    print("Prerequisites:")
    print("  CS101, MATH101 -> CS201")
    print("  CS201 -> CS301, CS302")
    
    order_kahn = topological_sort_kahn(g1)
    order_dfs = topological_sort_dfs(g1)
    
    print(f"\nTopological order (Kahn's): {' -> '.join(order_kahn)}")
    print(f"Topological order (DFS): {' -> '.join(order_dfs)}")
    
    # Example 2: Task scheduling
    print("\n\nExample 2: Task Scheduling")
    print("-" * 70)
    
    g2 = Graph()
    # Task dependencies
    g2.add_edge('Task1', 'Task3')
    g2.add_edge('Task2', 'Task3')
    g2.add_edge('Task3', 'Task4')
    g2.add_edge('Task3', 'Task5')
    g2.add_edge('Task4', 'Task6')
    g2.add_edge('Task5', 'Task6')
    
    print("Task dependencies:")
    print("  Task1, Task2 -> Task3")
    print("  Task3 -> Task4, Task5")
    print("  Task4, Task5 -> Task6")
    
    order = topological_sort_kahn(g2)
    if order:
        print(f"\nValid execution order: {' -> '.join(order)}")
    
    # Example 3: Build system
    print("\n\nExample 3: Build System Dependencies")
    print("-" * 70)
    
    g3 = Graph()
    g3.add_edge('libA', 'app')
    g3.add_edge('libB', 'app')
    g3.add_edge('libC', 'libA')
    g3.add_edge('libC', 'libB')
    
    print("Dependencies:")
    print("  libC -> libA, libB")
    print("  libA, libB -> app")
    
    order = topological_sort_dfs(g3)
    if order:
        print(f"\nBuild order: {' -> '.join(order)}")
    
    # Example 4: Graph with cycle (should fail)
    print("\n\nExample 4: Graph with Cycle")
    print("-" * 70)
    
    g4 = Graph()
    g4.add_edge(0, 1)
    g4.add_edge(1, 2)
    g4.add_edge(2, 0)  # Creates cycle
    
    print("Graph: 0 -> 1 -> 2 -> 0 (cycle)")
    order = topological_sort_kahn(g4)
    if order is None:
        print("Result: No topological order exists (cycle detected)")
    else:
        print(f"Topological order: {' -> '.join(map(str, order))}")
    
    # Example 5: Complex DAG
    print("\n\nExample 5: Complex DAG")
    print("-" * 70)
    
    g5 = Graph()
    g5.add_edge(1, 2)
    g5.add_edge(1, 3)
    g5.add_edge(2, 4)
    g5.add_edge(3, 4)
    g5.add_edge(3, 5)
    g5.add_edge(4, 6)
    g5.add_edge(5, 6)
    
    print("Complex directed acyclic graph")
    order = topological_sort_kahn(g5)
    if order:
        print(f"Topological order: {' -> '.join(map(str, order))}")
        print("\nNote: Multiple valid topological orders may exist")
    
    print("\n" + "=" * 70)
    print("Key Properties:")
    print("=" * 70)
    print("1. Topological sort only exists for DAGs (no cycles)")
    print("2. Multiple valid topological orders may exist")
    print("3. Kahn's algorithm: O(V + E) using BFS")
    print("4. DFS algorithm: O(V + E) using recursion")
    print("5. Applications: Course scheduling, build systems, task dependencies")


if __name__ == "__main__":
    demonstrate_topological_sort()
