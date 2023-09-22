#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#define ROW 3
#define COL 3

// int main(){
//     char str1[6] = "Seoul";
//     char str2[3] = {'i', 's', '\0'};
//     char str3[] = "the capital city of Korea.";
    
//     printf("%s %s %s\n", str1, str2, str3);
//     return 0;
// }

// int main(){
//     char src[] = "My name is seunghun.";
//     char dst[100];
//     int i;
//     printf("src: %s\n", src);
//     for(i = 0; src[i] != '\0'; i++){
//         dst[i] = src[i];
//     }
//     dst[i] = '\0';
//     printf("dst: %s\n", dst);
// }

// int main(){
//     char src1[100] = "My name is seunghun.";
//     char src2[100] = "I'm 21 years old.";
//     char dst[100];
//     strcat(src1, src2);
//     strcat(src1, "I'm a student.");
//     strcat(src1, "test");
//     printf("src1: %s\n", src1);
// }

// int main(){
//     char src1[100];
//     char src2[100];

//     scanf("%s", src1);
//     scanf("%s", src2);
//     int result = strcmp(src1, src2);
//     if(result == 0){
//         printf("same\n");
//     }else if(result > 0){
//         printf("첫번째 문자열이 더 큽니다.\n");
//     }else{
//         printf("두번째 문자열이 더 큽니다.\n");
//     }
// }

// int main(){
//     char src[100] = "100";
//     int value ;

//     sscanf(src, "%d", &value);
//     printf("%d\n", value);
//     value++;
//     sprintf(src, "%d", value);
//     printf("%s\n", src);
// }

// int main(){
//     char str[100];
//     gets(str);
//     puts(str);
// }

// int main(){
//     int s[ROW][COL];
//     srand(time(NULL));
//     for(int i = 0; i < ROW; i++){
//         for(int j = 0; j < COL; j++){
//             s[i][j] = rand() % 100;
//         }
//     }
//     for(int i = 0; i < ROW; i++){
//         for(int j = 0; j < COL; j++){
//             printf("%d ", s[i][j]);
//         }
//         printf("\n");
//     }
// }

int main(){
    int A[ROW][COL] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[ROW][COL] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int C[ROW][COL];
    for(int i = 0; i < ROW; i++){
        for(int j = 0; j < COL; j++){
            C[i][j] = A[i][j] + B[i][j];
        }
    }
    for(int i = 0; i < ROW; i++){
        for(int j = 0; j < COL; j++){
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
}