#include<stdlib.h>
#include<stdio.h>
void main()
{
    int num,rev=0,count=0,digit=0,number=0;
    printf("Enter number:");
    scanf("%d",&num);
    number=num;
    do
    {   digit=num%10;
        rev=(rev*10)+digit;
        num=num/10;
    }
    while(num!=0);
   printf("Reverse of number is:%d",rev);
   if(rev==number)
   {
    printf("\nYes it is a palindrome");
   }
   else
   {
    printf("\nIt is not a palindrome");

   }
}