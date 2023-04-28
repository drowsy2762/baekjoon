#include<stdio.h>

int x = 10;
int factorial(int x){
    if(x == 1){
        return 1;
    }
    else{
        return x * factorial(x-1);
    }
}
void sub(){
    static int scount = 0;
    int acount = 0;
    printf("scount = %d, acount = %d\n",scount,acount);
    scount++;
}