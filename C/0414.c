#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* int main(){
    int n, count=,i;
    srand((unsigned)time(NULL));
    n = rand() % 20 + 1;
    printf("Number game: (1-20");
    while(1){
        count++;
        printf("Please input a number: ");
        scanf("%d", &i);
        if(i == n){
            printf("You are right! You have tried %d times.\n", count);
            break;
        }
        else if(i > n){
            printf("Too big!\n");
        }
        else{
            printf("Too small!\n");
        }
    }
}*/
/*int Hello(){
    for(int i = 0; i<20 ; i++){
        printf("*");
    }
    printf("\n");
    printf("Hello World!\n");
    for (int i = 0; i < 20; i++)
    {
        printf("*");
    }
    printf("\n");
    return 0;
}
int main(){
    Hello();
    
}*/
/*int max(int x, int y){
    if(x > y){
        return x;
    }
    else{
        return y;
    }
}
int main(){
    int a, b, c;
    printf("Please input three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    printf("The max number is %d\n", max(max(a, b), c));
    return 0;
}*/
int get_int(){
    int n;
    printf("정수를 하나 입력해주세요: ");
    scanf("%d", &n);
    return n;
}
int sum(int x, int y){
    return x + y;
}
int main(){
    int a, b;
    a = get_int();
    b = get_int();
    printf("두 수의 합은 %d입니다.\n", sum(a, b));
}