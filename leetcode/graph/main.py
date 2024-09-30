from graph import Graph

def main():
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    edges = {
        'a': ['b', 'c'],
        'b': ['c', 'd', 'e'],
        'c': ['d'],
        'd': ['e'],
        'e': ['f'],
        'f': []
    }
    orientation = 'directed'  # Change to 'undirected' for undirected graph
    weighted = False
    graph = Graph(vertices, edges, orientation, weighted)
    print(graph.get_adjacent_vertices('a'))
    graph.visualize()
    print(graph.bfs('a'))
    print(graph.dfs('a'))
    print(graph.dijkstra('a'))


if __name__ == '__main__':
    main()
