import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNext()) return;

        String s = scanner.next();
        int n = s.length();

        // Compute KMP LPS (Longest Prefix Suffix) array
        int[] lps = new int[n];
        int len = 0;
        int i = 1;

        while (i < n) {
            if (s.charAt(i) == s.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        int longestBorder = lps[n - 1];
        int candidatePeriod = n - longestBorder;

        // Check if the candidate period divides the total string length evenly
        if (n % candidatePeriod == 0) {
            System.out.println(candidatePeriod);
        } else {
            System.out.println(n);
        }

        scanner.close();
    }
}
