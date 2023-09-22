#include<stdio.h>
#include<time.h>
// double getDouble() {
//     double num;
//     scanf("%lf", &num);
//     return num;
// }

// double add(double x, double y) {
//     return x + y;
// }

// int get_integers() {
//     int num;
//     scanf("%d", &num);
//     return num;
// }

// void main(){
//     double x,y;
//     printf("Enter x: ");
//     x = getDouble();
//     printf("Enter y: ");
//     y = getDouble();
//     printf("x + y = %lf\n", add(x, y));
// }


// int even(int num){
//     if(num % 2 == 0){
//         return 1;
//     }
//     else{
//         return 0;
//     }
// }

// int abs(int num){
//     if(num < 0){
//         return -num;
//     }
//     else{
//         return num;
//     }
// }

// int sign(int num){
//     if(num < 0){
//         return -1;
//     }
//     else if(num == 0){
//         return 0;
//     }
//     else{
//         return 1;
//     }
// }

// void main(){
//     int num;
//     printf("정수를 입력해주세요: ");
//     scanf("%d", &num);
//     if(even(num) == 1)
//         printf("입력한 정수는 짝수입니다.\n");
//     else
//         printf("입력한 정수는 홀수입니다.\n");
//     if(sign(num) == 1)
//         printf("입력한 정수는 양수입니다.\n");
//     else if(sign(num) == 0)
//         printf("입력한 정수는 0입니다.\n");
//     else
//         printf("입력한 정수는 음수입니다.\n");
//     printf("입력한 정수의 절댓값은 %d입니다.\n", abs(num));
// }

// static int saveMoney = 0;

// void save(int amount){
//     if(amount > 0){
//         printf("입금: %d\n", amount);
//         saveMoney += amount;
//     }
//     else{
//         printf("출금: %d\n", -amount);
//         saveMoney += amount;
//     }
// }

// void pMoney(int savemoney){
//     printf("잔고: %d\n",savemoney);
// }

// int main(){
//     int money = 0;
//     while(1){
//         printf("입금할 돈을 입력해주세요: ");
//         scanf("%d",&money);
//         if(money == 0){
//             break;
//         }
//         save(money);
//         pMoney(saveMoney);
//     }
// }

// static int check_num = 0;

// int check(int id, int password){
//     if(id == 1234 && password == 1234){
//         return 1;
//     }
//     else{
//         check_num++;
//         return 0;
//     }
// }

// int main(){
//     int id, password;
//     while(1){
//         printf("아이디를 입력해주세요: ");
//         scanf("%d", &id);
//         printf("비밀번호를 입력해주세요: ");
//         scanf("%d", &password);
//         if(check(id, password) == 1){
//             printf("로그인 성공\n");
//             break;
//         }
//         else{
//             printf("로그인 실패\n");
//             if(check_num == 3){
//                 printf("로그인 시도 횟수 초과\n");
//                 break;
//             }
//         }
//     }


//     return 0;
// }

//2진수 변환 재귀함수
void binary(int num){
    if(num == 0){
        return;
    }
    else{
        binary(num / 2);
        printf("%d", num % 2);
    }
}

int main(void){
    int num;
    printf("정수를 입력해주세요: ");
    scanf("%d", &num);
    binary(num);
    printf("\n");

    return 0;
}