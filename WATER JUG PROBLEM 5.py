import java.io.*;
import java.util.*;

public class Solution {
 public static int gcd(int a,int b)
 {return b==0 ? a:gcd(b,a%b) ;
    
 }

    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int a=sc.nextInt();
    int b=sc.nextInt();
    int c=sc.nextInt();
    int result=gcd(a,b);
    
    if(c%result==0)
    { System.out.println("YES");   
        
    }
    
    else
    {
             System.out.println("NO");
    
    }
}
    }
