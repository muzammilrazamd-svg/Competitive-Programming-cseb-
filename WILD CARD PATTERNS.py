import java.io.*;
import java.util.*;

public class Solution {

    public static boolean isMatch(String s, String p) {
        int sLen = s.length(), pLen = p.length();
        int sIdx = 0, pIdx = 0;
        int starIdx = -1, matchIdx = -1;

        while (sIdx < sLen) {
            // If pattern character matches string character or is '?'
            if (pIdx < pLen && (p.charAt(pIdx) == '?' || p.charAt(pIdx) == s.charAt(sIdx))) {
                sIdx++;
                pIdx++;
            } 
            // If pattern character is '*', record its position and the current string position
            else if (pIdx < pLen && p.charAt(pIdx) == '*') {
                starIdx = pIdx;
                matchIdx = sIdx;
                pIdx++;
            } 
            // If mismatch happens but a '*' was seen earlier, backtrack to the last '*'
            else if (starIdx != -1) {
                pIdx = starIdx + 1;
                matchIdx++;
                sIdx = matchIdx;
            } 
            // If characters don't match and no '*' to fall back on
            else {
                return false;
            }
        }

        // Check if all remaining characters in the pattern are '*'
        while (pIdx < pLen && p.charAt(pIdx) == '*') {
            pIdx++;
        }

        return pIdx == pLen;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextLine()) return;
        
        String s = scanner.nextLine().trim();
        if (!scanner.hasNextLine()) return;
        
        String p = scanner.nextLine().trim();

        if (isMatch(s, p)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
        
        scanner.close();
    }
}
