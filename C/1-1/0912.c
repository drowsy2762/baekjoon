#include <stdio.h>

// int main(void) {
//     int i = 3000; int* p = NULL;
//     p = &i;
//     printf("i = %d\n", i);
//     // 변수의 값 출력 printf("&i = %u\n\n", &i); // 변수의 주소 출력
//     printf("p = %u\n", p); // 포인터의 값 출력
// //     printf("*p = %d\n", *p); // 포인터를 통한 간접 참조 값 출력
// //     return 0; 
// // }

int main(void) {
int x=10, y=20; int *p;int *q;
p = &x;
printf("p = %d\n", p); printf("*p = %d\n\n", *p);
q = &y;
printf("q = %d\n", q); printf("*q = %d\n", *q);
printf("%d",*(p+4));
return 0;
}
// int main(){
//     int a = 10;
//     printf("뭐출력\n뭐출력\n anj");
//     scanf("%d\t");
// }