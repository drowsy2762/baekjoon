#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 3

// typedef struct _student
// {
//     char name[20];
//     int age;
//     char address[100];
// } student;

// void print(student *s)
// {
//     printf("이름 : %s\n", s->name);
//     printf("나이 : %d\n", s->age);
//     printf("주소 : %s\n", s->address);
// }

// int main()
// {
//     student *s1 = malloc(sizeof(student));
//     strcpy(s1->name, "홍길동");
//     s1->age = 30;
//     strcpy(s1->address, "서울시 용산구 한남동");
//     print(s1);
//     free(s1);
//     return 0;
// }

// int main(void)
// {
//     int x1, x2, y1, y2;
//     printf("왼쪽 상단의 좌표를 입력하세요 : ");
//     scanf("%d %d", &x1, &y1);

//     printf("오른쪽 하단의 좌표를 입력하세요 : ");
//     scanf("%d %d", &x2, &y2);

//     printf("두 점이 이루는 직사각형의 넓이는 %d입니다.\n", (x2 - x1) * (y2 - y1));
//     printf("두 점이 이루는 직사각형의 둘레는 %d입니다.\n", (x2 - x1) * 2 + (y2 - y1) * 2);
// }

struct student
{
    char name[20];
    int age;
    char address[100];
};

int main(void)
{
    struct student list[SIZE];
    int i;

    for (i = 0; i < SIZE; i++)
    {
        printf("이름 : ");
        scanf("%s", list[i].name);
        printf("나이 : ");
        scanf("%d", &list[i].age);
        printf("주소 : ");
        scanf("%s", list[i].address);
    }

    for (i = 0; i < SIZE; i++)
    {
        printf("이름 : %s\n", list[i].name);
        printf("나이 : %d\n", list[i].age);
        printf("주소 : %s\n", list[i].address);
    }
}