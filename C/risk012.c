#include<stdlib.h>
#include<stdbool.h>
#include<stdio.h>
void main()
{  
    int ar[]={1,0,2,0,1,0,2};
    int zero=0,one=0,two=0;
    int length=sizeof(ar)/sizeof(ar[0]);
    int item[length];
    for(int i=0;i<length;++i)
    {
        if(ar[i]==0)
        {
            ++zero;
        }
        if(ar[i]==1)
        {
            ++one;
        }
        if(ar[i]==2)
        {
            ++two;
        }
    }
    int i=0;
    while(true)
    {
      if(zero!=0)
      {
        item[i]=0;
        --zero;
        ++i;
        continue;
      }
      if(one!=0)
      {
        item[i]=1;
        --one;
        ++i;
        continue;
      }
      if(two!=0)
      {
        item[i]=2;
        --two;
        ++i;
        continue;
      }
      break;
    }
    for(int i=0;i<length;++i)
    {
       printf("%d",item[i]);
    }

}