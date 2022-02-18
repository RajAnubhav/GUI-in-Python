#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main(){
    printf("Enter your name : ");

    char name[5];
    scanf("%s", name);
    
    printf("Welcome %s", name);

    return 0;
}