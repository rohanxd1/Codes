#include<stdlib.h>
#include<stdio.h>
void main()
{
    int num,count=0;
    printf("Enter number:");
    scanf("%d",&num);
    do
    {
        num=num/10;
        ++count;
    }
    while(num!=0);
    printf("Number of digits:%d",count);
}