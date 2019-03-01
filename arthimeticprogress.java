import java.io.*;
import java.util.*;
class ArithmeticProgress
{
public static void main(String args[])
{
Scanner s=new Scanner(system.in);
int a,n,d;
System.out.println("Enter start term a");
a=s.nextInt();
System.out.println("Enter difference d");
d=s.nextInt();
System.out.println("enter no. of terms n");
n=s.nextInt();
int add=0;
for(int i=1;i<=n;i++)
{
add=add+a;
a=a+d;
}
System.out.println("The arithmatic progression is"+a);
}
}
