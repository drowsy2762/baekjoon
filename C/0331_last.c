// 산술계산 프로그램
#include<stdio.h>

int main(void){
    int num1, num2;
    char op;
    printf("사칙연산을 입력해주세요: ");
    scanf("%d %c %d", &num1, &op, &num2);

    switch (op)
    {
    case '+':
        printf("두 수의 합은 :");
        printf("%d + %d = %d", num1, num2, num1+num2);
        break;
    case '-':
        printf("두 수의 차는 :");
        printf("%d - %d = %d", num1, num2, num1-num2);
        break;
    case '*':
        printf("두 수의 곱은 :");
        printf("%d * %d = %d", num1, num2, num1*num2);
        break;
    case '/':
        printf("두 수의 나눗셈은 :");
        printf("%d / %d = %d", num1, num2, num1/num2);
        break;
    case '%' :
        printf("두 수의 나머지는 :");
        printf("%d %% %d = %d", num1, num2, num1%num2);
        break;
    default: 
        printf("잘못된 연산자입니다.");
        break;
    }

}