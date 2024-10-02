import java.util.*;

class Graph {
    private final Map<String, List<Edge>> adjacencyList = new HashMap<>();

    public void addEdge(String u, String v, int weight) {
        adjacencyList.putIfAbsent(u, new ArrayList<>());
        adjacencyList.putIfAbsent(v, new ArrayList<>());
        adjacencyList.get(u).add(new Edge(v, weight));
        adjacencyList.get(v).add(new Edge(u, weight)); // Si le graphe est non orienté
    }

    public Map<String, Integer> dijkstra(String source) {
        Map<String, Integer> distances = new HashMap<>();
        Map<String, String> predecessors = new HashMap<>();
        for (String vertex : adjacencyList.keySet()) {
            distances.put(vertex, Integer.MAX_VALUE);
        }
        distances.put(source, 0);

        PriorityQueue<Node> priorityQueue = new PriorityQueue<>(Comparator.comparingInt(node -> node.distance));
        priorityQueue.add(new Node(source, 0));

        while (!priorityQueue.isEmpty()) {
            Node currentNode = priorityQueue.poll();
            String currentVertex = currentNode.vertex;

            for (Edge edge : adjacencyList.getOrDefault(currentVertex, new ArrayList<>())) {
                String neighbor = edge.target;
                int newDist = distances.get(currentVertex) + edge.weight;

                if (newDist < distances.get(neighbor)) {
                    distances.put(neighbor, newDist);
                    predecessors.put(neighbor, currentVertex);
                    priorityQueue.add(new Node(neighbor, newDist));
                }
            }
        }

        return distances;
    }

    private static class Edge {
        String target;
        int weight;

        Edge(String target, int weight) {
            this.target = target;
            this.weight = weight;
        }
    }

    private static class Node {
        String vertex;
        int distance;

        Node(String vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
    }

    public static void main(String[] args) {
        Graph g = new Graph();
        g.addEdge("A", "B", 1);
        g.addEdge("A", "C", 4);
        g.addEdge("B", "C", 2);
        g.addEdge("B", "D", 5);
        g.addEdge("C", "D", 1);

        Map<String, Integer> distances = g.dijkstra("A");
        System.out.println("Distances: " + distances);
    }
}