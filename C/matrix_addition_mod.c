#include<stdlib.h>
#include<stdio.h>
void main()
{
    int a[20][20],b[20][20],c[20][20],m=0,n=0;
    printf("Enter number of rows and coloumns of matrices:\nm:");
    scanf("%d",&m);
    printf("n:");
    scanf("%d",&n);
    
    printf("Enter values of Mat A:\n");
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            scanf("%d",&a[i][j]);
        }
        printf("\n");
    }
    printf("Mat A:\n");
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            printf("%d  ",a[i][j]);
        }
        printf("\n \n");
    }


    printf("Enter values of Mat b:\n");
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            scanf("%d",&b[i][j]);
        }
        printf("\n");
    }
    
    /*printf("Mat B:\n");
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            printf("%d  ",b[i][j]);
        }
        printf("\n \n");
    }*/
    
    //addition
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
          c[i][j]=a[i][j]+b[i][j];
        }
        
    }

    // printing of both mat
    printf("Mat A \t\tMat B\n");
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            printf("%d ",a[i][j]);
        }
        printf("\t\t");
        for(int j=0;j<n;++j)
        {
            printf("%d ",b[i][j]);
        }
        printf("\n");
    }
    
    printf("Resultant matrix:\n");
    for(int i=0;i<m;++i)
    {
        for(int j=0;j<n;++j)
        {
            printf("%d \t",c[i][j]);
        }
        printf("\n \n");
    }

}