#include<stdio.h>
#include<stdlib.h>
void main()
{
    int div=0,nodiv=0;
    for(int i=1;i<=30;++i)
    {
        if (i%6==0)
        {
            div+=i;
        }
        else{
            nodiv+=i;
        }
    }
    int diff=0;
    diff=nodiv-div;
    printf("Diff is %d",diff);
}

