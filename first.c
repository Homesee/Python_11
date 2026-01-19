#include<stdio.h>
int sum(int a,int b)
{
    int c;
    c=a+b;
    return c;
}
int main()
{
    int b,e,f,g,h,k,l,m;
    printf("Please enter a number\n");
    scanf("%d",&b); 
    printf("You entered: %d\n",b);
    e=sum(3,4);
    f=sum(5,4);
    g=sum(9,6);
    h=sum(45,78);
    printf("you got a addition %d,%d,%d,%d\n",e,f,g,h);
    printf("enter two numbers\n");
    scanf("%d%d",&k,&l);
    m=sum(k,l);
    printf("The sum of given number is %d",m);
return 0;
}

