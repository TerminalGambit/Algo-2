from graph import Graph

def main():
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    edges = {
        'a': [('b', 1), ('c', 1)],
        'b': [('d', 1), ('e', 1)],
        'c': [('f', 1)],
        'd': [],
        'e': [],
        'f': []
    }
    orientation = 'directed'  # Change as needed
    weighted = False
    graph = Graph(vertices, edges, orientation, weighted)

    source_vertex = 'a'
    dfs_order = graph.dfs(source_vertex)

    print("DFS Traversal starting from vertex '{}':".format(source_vertex))
    print(" -> ".join(dfs_order))


if __name__ == '__main__':
    main()
