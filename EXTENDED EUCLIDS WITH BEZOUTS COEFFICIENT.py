import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextLong()) return;

        long A = scanner.nextLong();
        long B = scanner.nextLong();

        // Extended Euclidean Algorithm
        // Solves A * x0 + B * y0 = gcd(A, B)
        long[] result = extendedGCD(A, B);
        long g = result[0];
        long x0 = result[1];
        long y0 = result[2];
EXTENDED EUCLIDS WITH BEZOUTS COEFFICIENT
        // All general solutions are given by:
        // x = x0 + k * (B / g)
        // y = y0 - k * (A / g)
        long stepX = B / g;
        long stepY = A / g;

        // Find optimal k to minimize |x| + |y|
        // Optimal k is around k = -x0 / stepX
        long kBase = Math.round((double) -x0 / stepX);

        long bestX = 0;
        long bestY = 0;
        long minSum = Long.MAX_VALUE;

        // Check neighboring values of k around kBase to ensure global minimum of |x| + |y|
        for (long k = kBase - 2; k <= kBase + 2; k++) {
            long x = x0 + k * stepX;
            long y = y0 - k * stepY;

            long sum = Math.abs(x) + Math.abs(y);

            if (sum < minSum) {
                minSum = sum;
                bestX = x;
                bestY = y;
            } else if (sum == minSum) {
                // Break tie by selecting the pair where x <= y
                if (x <= y) {
                    bestX = x;
                    bestY = y;
                }
            }
        }

        System.out.println(bestX + " " + bestY + " " + g);

        scanner.close();
    }

    // Extended GCD returns [gcd, x, y] such that A*x + B*y = gcd(A, B)
    private static long[] extendedGCD(long a, long b) {
        if (b == 0) {
            return new long[]{a, 1, 0};
        }
        long[] prev = extendedGCD(b, a % b);
        long g = prev[0];
        long x1 = prev[1];
        long y1 = prev[2];

        long x = y1;
        long y = x1 - (a / b) * y1;

        return new long[]{g, x, y};
    }
}
