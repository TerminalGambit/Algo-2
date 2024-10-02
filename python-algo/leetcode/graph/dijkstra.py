from graph import Graph

def main():
    vertices = ['a', 'b', 'c', 'd', 'e']
    edges = {
        'a': [('b', 2), ('c', 5)],
        'b': [('c', 1), ('d', 2)],
        'c': [('d', 3), ('e', 1)],
        'd': [('e', 2)],
        'e': []
    }
    orientation = 'directed'  # or 'undirected' as needed
    weighted = True
    graph = Graph(vertices, edges, orientation, weighted)

    source_vertex = 'a'
    distances, predecessors = graph.dijkstra(source_vertex)

    print("Shortest distances from source vertex '{}':".format(source_vertex))
    for vertex, distance in distances.items():
        print(f"Vertex {vertex}: Distance {distance}")

    print("\nPredecessors in shortest path tree:")
    for vertex, predecessor in predecessors.items():
        print(f"Vertex {vertex}: Predecessor {predecessor}")

    # Reconstruct the shortest path from 'a' to 'e'
    path = reconstruct_path(predecessors, 'a', 'e')
    if path:
        print("\nShortest path from 'a' to 'e':", " -> ".join(path))
    else:
        print("No path found from 'a' to 'e'.")

def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return None  # No path found


if __name__ == '__main__':
    main()
