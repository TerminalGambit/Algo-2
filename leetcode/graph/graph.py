import matplotlib.pyplot as plt
import numpy as np
from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self, vertices: list, edges: dict, orientation: str = 'undirected', weighted: bool = False):
        self.vertices = vertices
        self.edges = edges  # Should be a dictionary with adjacency lists
        self.orientation = orientation.lower()
        self.weighted = weighted

    def add_vertex(self, vertex: str):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.edges[vertex] = []

    def add_edge(self, edge: tuple):
        start, end = edge[:2]
        weight = edge[2] if self.weighted and len(edge) > 2 else 1  # Default weight is 1
        if start in self.vertices and end in self.vertices:
            self.edges[start].append((end, weight))
            if self.orientation == 'undirected':
                self.edges[end].append((start, weight))
        else:
            print("One or both vertices not found in graph.")

    def remove_vertex(self, vertex: str):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            self.edges.pop(vertex, None)
            for key in self.edges:
                self.edges[key] = [(v, w) for v, w in self.edges[key] if v != vertex]
        else:
            print("Vertex not found in graph.")

    def remove_edge(self, edge: tuple):
        start, end = edge[:2]
        if start in self.edges:
            self.edges[start] = [(v, w) for v, w in self.edges[start] if v != end]
            if self.orientation == 'undirected' and end in self.edges:
                self.edges[end] = [(v, w) for v, w in self.edges[end] if v != start]
        else:
            print("Edge not found in graph.")

    def get_adjacent_vertices(self, vertex: str):
        return [v for v, _ in self.edges.get(vertex, [])]

    def visualize(self):
        # Assign positions to each vertex in a circular layout
        num_vertices = len(self.vertices)
        angles = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        positions = {}
        for idx, vertex in enumerate(self.vertices):
            x = np.cos(angles[idx])
            y = np.sin(angles[idx])
            positions[vertex] = (x, y)

        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        # Plot vertices
        for vertex, (x, y) in positions.items():
            ax.scatter(x, y, s=100, zorder=2)
            ax.text(x, y, vertex, fontsize=12, ha='center', va='center', zorder=3)

        # Plot edges
        for start_vertex in self.vertices:
            x_start, y_start = positions[start_vertex]
            for end_vertex in self.edges[start_vertex]:
                x_end, y_end = positions[end_vertex]
                if self.orientation == 'directed':
                    # Draw arrow for directed graph
                    dx = x_end - x_start
                    dy = y_end - y_start
                    ax.annotate(
                        '', xy=(x_end, y_end), xytext=(x_start, y_start),
                        arrowprops=dict(arrowstyle='->', lw=1.5),
                        zorder=1
                    )
                else:
                    # Draw line for undirected graph
                    ax.plot([x_start, x_end], [y_start, y_end], 'k-', zorder=1)

        ax.axis('off')
        plt.show()

    def bfs(self, source: str):
        """
        Perform Breadth-First Search starting from the source vertex.
        Returns a dictionary with distances and predecessors for each vertex.
        """
        if source not in self.vertices:
            print(f"Source vertex '{source}' not found in graph.")
            return None

        # Initialize distances and predecessors
        distances = {vertex: None for vertex in self.vertices}
        predecessors = {vertex: None for vertex in self.vertices}
        distances[source] = 0

        # Initialize the queue for BFS
        queue = deque()
        queue.append(source)

        while queue:
            current_vertex = queue.popleft()
            for neighbor in self.edges[current_vertex]:
                if distances[neighbor] is None:
                    distances[neighbor] = distances[current_vertex] + 1
                    predecessors[neighbor] = current_vertex
                    queue.append(neighbor)

        return distances, predecessors

    def dfs(self, source: str):
        """
        Perform Depth-First Search starting from the source vertex.
        Returns a list of vertices in the order they were visited.
        """
        visited = set()
        traversal_order = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor, _ in self.edges.get(vertex, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(source)
        return traversal_order

    def dijkstra(self, source: str):
        """
        Perform Dijkstra's Algorithm starting from the source vertex.
        Returns a dictionary with distances and predecessors for each vertex.
        """
        if not self.weighted:
            print("Graph is unweighted. Dijkstra's algorithm requires weighted edges.")
            return None

        distances = {vertex: float('inf') for vertex in self.vertices}
        predecessors = {vertex: None for vertex in self.vertices}
        distances[source] = 0

        # Priority queue to select the next vertex with the smallest distance
        priority_queue = [(0, source)]
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors
