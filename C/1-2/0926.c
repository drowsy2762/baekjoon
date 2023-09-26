#include <stdio.h>

// void swap(int *a, int *b)
// {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

// void set_pointer(char **p)
// {
//     *p = "Hello World!";
// }

int calculator(int menu, int a, int b)
{
    switch (menu)
    {
    case 0:
        return a + b;
    case 1:
        return a - b;
    case 2:
        return a * b;
    case 3:
        return a / b;
    case 4:
        return -1;
    default:
        return 0;
    }
}

int menu(int *pa, int *pb)
{
    int menu;
    printf("메뉴를 선택하시오: \n");
    scanf("%d", &menu);
    printf("2개의 정수를 입력하시오 : \n");
    scanf("%d %d", pa, pb);
    int result = calculator(menu, *pa, *pb);
    if (result == -1)
        return -1;
    else if (result == 0)
    {
        printf("잘못된 입력입니다.\n");
        return 0;
    }
    else
    {
        printf("결과는 %d입니다.\n", result);
        return 0;
    };
}

int main()
{
    int a = 1, b = 2;
    int *pa = &a, *pb = &b;
    char *p;
    printf("==================\n");
    printf("0. 덧셈\n");
    printf("1. 뺄셈\n");
    printf("2. 곱셈\n");
    printf("3. 나눗셈\n");
    printf("4. 종료\n");
    printf("==================\n");

    while (1)
    {
        int result = menu(pa, pb);
        if (result == -1)
            break;
        else if (result == 0)
            continue;
    }

    return 0;
}