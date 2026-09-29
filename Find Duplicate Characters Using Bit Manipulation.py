import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution.11231 */
        Scanner sc=new Scanner(System.in);
        String a=sc.nextLine();
        int[] freq=new int [26];
        for(char ch:a.toCharArray())
        {
            freq[ch-'a']++;
             
        }
         for(char ch:a.toCharArray())
        {
            if( freq[ch-'a'] <a){
                
            }
            
        }
    }
}
/*public class Solution {
    public int solve(String A) {
        if (A == null || A.length() == 0) {
            return 0;
        }

        int n = A.length();
        int[][] dp = new int[n][n];

        // Every single character is a palindrome of length 1
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        // len is the length of the substring being considered
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;

                if (A.charAt(i) == A.charAt(j)) {
                    if (len == 2) {
                        dp[i][j] = 2;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1] + 2;
                    }
                } else {
                    dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }

        // The answer for the entire string length n is in dp[0][n-1]
        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Sample Input 0
        String A0 = "bebeeed";
        System.out.println("Output 0: " + sol.solve(A0)); // Expected: 4 ("eeee" or "beeb")

        // Sample Input 1
        String A1 = "caataed";
        System.out.println("Output 1: " + sol.solve(A1)); // Expected: 3 ("aat" -> "a-a-a")
    }
}*/
