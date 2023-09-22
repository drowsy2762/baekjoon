#include <stdio.h>

// int main(){
//     //pointer
//     int *p;
//     int a = 10;
//     p = &a;
//     printf("a = %d\n", a);
//     printf("p = %d\n", *p);
//     printf("p = %d\n", p);
// }

// int main(){
//     char *pc;
//     int *pi;
//     double *pd;
//     pc = (char *)10000;
//     pi = (int *)10000;
//     pd = (double *)10000;
//     printf("pc = %d, pi = %d, pd = %d\n", pc, pi, pd);
//     pc++;
//     pi++;
//     pd++;
//     printf("pc = %d, pi = %d, pd = %d\n", pc, pi, pd);
//     printf("pc+2 = %d, pi+2 = %d, pd+2 = %d\n", pc+2, pi+2, pd+2);
// }


// int swap(int x, int y){
//     int temp;
//     temp = x;
//     x = y;
//     y = temp;
// }

// int main(){
//     int a = 100;
//     int b = 100;
//     printf("a = %d, b = %d\n", a, b);
//     swap (a, b);
//     printf("a = %d, b = %d\n", a, b);
// }
void swap(int *pa, int *pb){
    int temp;
    temp = *pa;
    *pa = *pb;
    *pb = temp;
}

int main(){
    // swap 포인터로
    int a = 100;
    int b = 105;
    int *pa = &a;
    int *pb = &b;
    printf("a = %d, b = %d\n", a, b);
    swap(pa, pb);
    printf("a = %d, b = %d\n", a, b);
}