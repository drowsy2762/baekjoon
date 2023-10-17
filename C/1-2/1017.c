#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// typedef struct point
// {
//     int x;
//     int y;
// } point;

// point traslate(point p, point delta)
// {
//     int xtemp = p.x;
//     int ytemp = p.y;
//     p.x = delta.x;
//     p.y = delta.y;
//     delta.x = xtemp;
//     delta.y = ytemp;
//     return p;
// }

// int main(void)
// {
//     point p = {2, 3};
//     point delta = {10, 10};
//     point result;

//     result = traslate(p, delta);
//     printf("result: (%d, %d)\n", result.x, result.y);
// }

typedef struct student
{
    int type;
    char name[20];
    union
    {
        int stuNumber;
        char reg_number[15];
    } id;
};

void print(struct student s)
{
    switch (s.type)
    {
    case 2:
        printf("Student number: %d\n", s.id.stuNumber);
        printf("Student name:", s.name);
        break;
    case 1:
        printf("Student number: %s\n", s.id.reg_number);
        printf("Student name:", s.name);
        break;
    default:
        printf("Invalid type\n");
        break;
    }
}

int main(void)
{
    struct student s1, s2;
    s1.type = 1;
    strcpy(s1.name, "John");
    s1.id.stuNumber = 123456789;

    s2.type = 2;
    strcpy(s2.name, "Mary");
    strcpy(s2.id.reg_number, "123456789");

    print(s1);
    print(s2);
}