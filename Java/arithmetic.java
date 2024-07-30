import java.util.*;
class arith
{ int answer=0;
    void sum(int a,int b)
    {
        answer=a+b;
        System.out.println("Sum="+answer);
    }
   
    void diff(int a,int b)
    { 
        answer=a-b;
        System.out.println(a+"-"+b+"="+answer);

    }
    
    void mul(int a,int b)
    {
        answer=a*b;
        System.out.println(a+"x"+b+"="+answer);

    }
    
    void div(int a,int b)
    {
        answer=a/b;
        System.out.println(a+"/"+b+"="+answer);
    }

}

class arithmetic
{
    public static void main(String[] args)
    {
        int ch=0,a,b;
        Scanner sc=new Scanner(System.in);
        arith obj= new arith();
        while(ch!=4)
        {System.out.print("\n1.Sum\n2.Difference\n3.Multiplication\n4.Division\n5.Exit\nEnter choice:");
         ch=sc.nextInt();
         if(ch==5)
         {
            break;
         }
         else if(ch==1||ch==2||ch==3||ch==4)
         {System.out.print("Enter A:");
          a=sc.nextInt();
          System.out.print("B:");
          b=sc.nextInt();
          switch(ch)
          {
             case 1: obj.sum(a,b);
                     break;
             case 2: obj.sum(a,b);
                      break; 
             case 3: obj.sum(a,b);
                     break;
             case 4: obj.sum(a,b);
                     break;
             default: System.out.println("Enter valid input!!!!");
                        break;

          }
         }
         else
         {
            System.out.print("Enter valid input!!\n");
         }
        }
        sc.close();
    }
}