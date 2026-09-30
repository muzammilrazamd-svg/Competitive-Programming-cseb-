import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner sc=new Scanner(System.in);
    int v=sc.nextInt();
    int n=sc.nextInt();
    int coin[]= new int[n];
    
    for(int i=0;i<n;i++)
    {coin[i]=sc.nextInt();}
    int[] dp=new int[v+1];
    Arrays.fill(dp,v+1);
    dp[0]=0;
    
    for(int i=0;i<=v;i++)
    {for(int c: coin)
    {
        if (c<=i)
    { dp[i]=Math.min(dp[i],dp[i-c]+1); }
    }
        
    }
    
    if (dp[v]>v)
    {System.out.println(-1);}
    else
    {System.out.println(dp[v]);}
     }
}
