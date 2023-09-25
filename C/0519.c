// 배열생성
#include<stdio.h>
#include<time.h>
#include<stdlib.h>

// int main(){
//     //배열의 초기화
//     int ary[5];
//     for(int i = 0; i < 5; i++){
//         ary[i] = i;
//         printf("%d ", ary[i]);
//     }
// }

// int main(){
//     //학생점수 입력받아서 평균점수 구하기
//     int n = 0;
//     printf("과목의 개수를 입력해주세요: ");
//     scanf("%d", &n);
//     int score[100];
//     float sum = 0;
//     for(int i = 0; i < n; i++){
//         printf("학생%d의 점수를 입력하세요: ", i+1);
//         scanf("%d", &score[i]);
//         sum += score[i];
//     }
//     printf("평균점수는 %.2f점입니다.", sum/5);

// }

// int main(){
//     int score[5] = {40,20,32,24,40};
//     for(int i = 0; i < 5; i++){
//         printf("score[%d] = %d\n ", i, score[i]);
//     }
// }

// int main(){
//     int num[5];
//     for(int i = 0; i < 5; i++){
//         scanf("%d", &num[i]);
//     }
//     for(int i = 0; i < 5; i++){
//         printf("%d ", num[4-i]);
//     }
// }

// int main(){
//     //난수 생성후 최소값찾기
//     srand((unsigned)time(NULL));
//     int num[10];
//     for(int i = 0; i < 10; i++){
//         num[i] = rand() % 100 + 1;
//         printf("%d ", num[i]);
//     }
//     int min = num[0];
//     for(int i = 0; i < 10; i++){
//         if(min > num[i]){
//             min = num[i];
//         }
//     }
//     printf("\n최소값은 %d입니다.", min);
// }

int main(){
    int i=0;
    char ch[20];
    printf("문자열을 입력하세요: ");
    scanf("%s", ch);
    while(ch[i] != '\0'){
        i++;
    }
    printf("문자열의 길이는 %d입니다.\n", i);
    printf("%s",ch);
}