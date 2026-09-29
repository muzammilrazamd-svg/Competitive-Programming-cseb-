import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Solution {

    static class Point {
        int r, c, time;
        Point(int r, int c, int time) {
            this.r = r;
            this.c = c;
            this.time = time;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder out = new StringBuilder();

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        // Process test cases until there are no more integers in the input
        while (scanner.hasNextInt()) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();

            int[][] grid = new int[N][M];
            Queue<Point> queue = new LinkedList<Point>();
            int freshCount = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    grid[i][j] = scanner.nextInt();
                    if (grid[i][j] == 2) {
                        queue.add(new Point(i, j, 0));
                    } else if (grid[i][j] == 1) {
                        freshCount++;
                    }
                }
            }

            if (freshCount == 0) {
                out.append("0\n");
                continue;
            }

            int maxTime = 0;

            // BFS Traversal
            while (!queue.isEmpty()) {
                Point curr = queue.poll();
                maxTime = Math.max(maxTime, curr.time);

                for (int i = 0; i < 4; i++) {
                    int nr = curr.r + dr[i];
                    int nc = curr.c + dc[i];

                    if (nr >= 0 && nr < N && nc >= 0 && nc < M && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // Mark as rotten
                        freshCount--;
                        queue.add(new Point(nr, nc, curr.time + 1));
                    }
                }
            }

            if (freshCount == 0) {
                out.append(maxTime).append("\n");
            } else {
                out.append("-1\n");
            }
        }

        System.out.print(out);
        scanner.close();
    }
}
