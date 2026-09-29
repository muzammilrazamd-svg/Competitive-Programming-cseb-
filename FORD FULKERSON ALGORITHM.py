import java.io.*;
import java.util.*;

public class Solution {

    static int V;
    static int[][] capacity;
    static int[] parent;

    // BFS to find if there is a path from source to sink in the residual graph
    public static boolean bfs(int s, int t) {
        boolean[] visited = new boolean[V];
        Arrays.fill(visited, false);
        Queue<Integer> queue = new LinkedList<Integer>();

        queue.add(s);
        visited[s] = true;
        parent[s] = -1;

        while (!queue.isEmpty()) {
            int u = queue.poll();

            for (int v = 0; v < V; v++) {
                if (!visited[v] && capacity[u][v] > 0) {
                    queue.add(v);
                    parent[v] = u;
                    visited[v] = true;
                    if (v == t) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static int fordFulkerson(int s, int t) {
        int u, v;
        int maxFlow = 0;

        parent = new int[V];

        // Augment the flow while there is a path from source to sink
        while (bfs(s, t)) {
            // Find the maximum flow through the path found by BFS
            int pathFlow = Integer.MAX_VALUE;
            for (v = t; v != s; v = parent[v]) {
                u = parent[v];
                pathFlow = Math.min(pathFlow, capacity[u][v]);
            }

            // Update residual capacities of the edges and reverse edges along the path
            for (v = t; v != s; v = parent[v]) {
                u = parent[v];
                capacity[u][v] -= pathFlow;
                capacity[v][u] += pathFlow;
            }

            maxFlow += pathFlow;
        }

        return maxFlow;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) return;

        V = scanner.nextInt();
        int E = scanner.nextInt();

        capacity = new int[V][V];

        for (int i = 0; i < E; i++) {
            int u = scanner.nextInt();
            int v = scanner.nextInt();
            int cap = scanner.nextInt();
            // If multiple edges between same nodes exist, accumulate capacities
            capacity[u][v] += cap;
        }

        int source = 0;
        int sink = V - 1;

        int maxFlow = fordFulkerson(source, sink);
        System.out.println(maxFlow);

        scanner.close();
    }
}
