import java.util.*;
class factorial
{public static void main(String[] args)
 { 
     int num,fact=1;
     Scanner sc=new Scanner(System.in);
     System.out.print("Enter number to find fact:");
     num=sc.nextInt();
     while(num!=0)
     {
         fact=fact*num;
         --num;
     }
     System.out.println("Factorial is "+fact);
     sc.close();
 }

}