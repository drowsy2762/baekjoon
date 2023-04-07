#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

/*int main(){
    int i = 0;
    int n = 0;
    printf("구구단의 시작점을 입력해주세요: ");
    scanf("%d",&n);
    while (i<9){
        i++;
        printf("%d * %d = %d\n",n,i,n*i);
    }
}*/

/*int main(){
    int score = 0;
    double sum = 0, average = 0;
    printf("점수의 입력을 종료하려면 음수를 입력해주세요.\n");
    while(score>=0){
        average++;
        printf("점수를 입력해 주세요: ");
        scanf("%d",&score);
        sum += score;
    }
    printf("평균 점수는 %.1lf입니다.",sum/average);
}*/

/*int main(){ 
    int sum = 0;
    int num ;
    do{
        printf("정수를 입력하세요: ");
        scanf("%d",&num);
        sum += num;
    }while(num != 0);
    printf("입력한 정수들의 합: %d\n",sum);
    return 0;
}*/

/*int main(){
    int i,sum;
    printf("1부터 10까지의 합을 구합니다.\n");
    for(i=1;i<=10;i++){
        sum += i;
    }
    printf("1부터 10까지의 합은 %d입니다.\n",sum);
}*/

/* int main(){
    int n,factorial;
    printf("정수를 입력하세요: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        factorial *= i;
    }
    printf("%d! = %d\n",n,factorial);
} */

int main(){
    int n,sum=0;
    char c;
    while(1){
        printf("정수를 입력하세요: ");
        scanf("%d",&n);        
        printf("계속하시겠습니까?(y/n): ");
        scanf("%c",&c);
        sum += n;
        if(c == 'n'){
            break;
        }
    }
    printf("합계: %d\n",sum);
}