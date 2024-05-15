#include<stdio.h>
#include<stdlib.h>
void main()
{
    int ar[]={4,5,0,1,9,0,5,0},c0=0;
    int p[8]={0};
    int i,j=0;
    for(i=0;i<8;++i)
    {
        if(ar[i]==0)
        {
            ++c0;

        }
        else
        {
            p[j]=ar[i];
            ++j;
        }
        
    }
        printf("\n");
   
    while(c0>0)
    {
        p[j]=0;
        --c0;
        ++j;
    }
    for(i=0;i<8;++i)
    {
       printf("%d",p[i]);
    }
}