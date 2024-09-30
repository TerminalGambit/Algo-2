import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class Graph:
    def __init__(self, vertices: list, edges: dict, orientation: str = 'undirected', weighted: bool = False):
        self.vertices = vertices
        self.edges = edges
        self.orientation = orientation.lower()
        self.weighted = weighted

    def add_vertex(self, vertex: str):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.edges[vertex] = []

    def add_edge(self, edge: tuple):
        start, end = edge
        if start in self.vertices and end in self.vertices:
            self.edges[start].append(end)
            if self.orientation == 'undirected':
                self.edges[end].append(start)
        else:
            print("One or both vertices not found in graph.")

    def remove_vertex(self, vertex: str):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            self.edges.pop(vertex, None)
            for key in self.edges:
                if vertex in self.edges[key]:
                    self.edges[key].remove(vertex)
        else:
            print("Vertex not found in graph.")

    def remove_edge(self, edge: tuple):
        start, end = edge
        if start in self.edges and end in self.edges[start]:
            self.edges[start].remove(end)
            if self.orientation == 'undirected' and start in self.edges[end]:
                self.edges[end].remove(start)
        else:
            print("Edge not found in graph.")

    def get_adjacent_vertices(self, vertex: str):
        return self.edges.get(vertex, [])

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
