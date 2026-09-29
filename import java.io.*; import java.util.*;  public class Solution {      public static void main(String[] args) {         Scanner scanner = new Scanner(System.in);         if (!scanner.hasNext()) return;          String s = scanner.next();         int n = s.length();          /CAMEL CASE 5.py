import java.io.*;
import java.util.*;

public class Solution {

    // Helper method to extract uppercase characters from a string
    private  Compute KMP LPS (Longest Prefix Suffix) array         int[] lps = new int[n];         int len = 0;         int i = 1;          while (i < n) {             if (s.charAt(i) == s.charAt(len)) {                 len++;                 lps[i] = len;                 i++;             } else {                 if (len != 0) {                static String getAbbreviation(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) return;

        int n = scanner.nextInt();
        String dictStr = scanner.next();
        String pattern = scanner.next();

        // Parse comma-separated words from the dictionary string
        String[] words = dictStr.split(",");

        List<String> matches = new ArrayList<String>();

        for (String word : words) {
            String abbrev = getAbbreviation(word);
            // Check if the abbreviation starts with the target pattern
            if (abbrev.startsWith(pattern)) {
                matches.add(word);
            }
        }

        if (matches.isEmpty()) {
            System.out.println("No match found");
        } else {
            // Sort matching words:
            // 1. By the lexicographical order of their uppercase abbreviations
            // 2. By standard lexicographical order of the original word if abbreviations are identical
            Collections.sort(matches, new Comparator<String>() {
                public int compare(String a, String b) {
                    String abbrevA = getAbbreviation(a);
                    String abbrevB = getAbbreviation(b);

                    int abbrevComp = abbrevA.compareTo(abbrevB);
                    if (abbrevComp != 0) {
                        return abbrevComp;
                    }
                    return a.compareTo(b);
                }
            });

            StringBuilder out = new StringBuilder();
            for (int i = 0; i < matches.size(); i++) {
                if (i > 0) {
                    out.append(" ");
                }
                out.append(matches.get(i));
            }
            System.out.println(out.toString());
        }

        scanner.close();
    }
}
