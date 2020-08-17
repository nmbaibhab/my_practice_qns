#include<stdio.h>
void factorial(int);
int multiply(int x,int arr[],int size);


int multiply(int x,int arr[],int size){
    int carry=0;
    for (int i = 0; i < size; i++)
    {
        int pro=(arr[i]*x)+carry;
        arr[i]=pro%10;
        carry=pro/10;
    }
    while(carry!=0){
        arr[size]=carry%10;
        carry=carry/10;
        size++;
    }
    return size;
}

void factorial(int num){
    int arr[10000];
    arr[0]=1;
    int size=1;
    for (int x = 2; x <= num; x++)
    {
        size=multiply(x,arr,size);
    }
    printf("Factorial is:\n");
    for (int z = size; z>=0; z--)
    {
        printf("%d",arr[z]);
    }
    
}

int main()
{
    int num;
    scanf("%d",&num);
    factorial(num);
}