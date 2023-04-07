#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

/*int main(){
    int i = 0;
    int n = 0;
    printf("구구?��?�� ?��?��?��?�� ?��?��?��주세?��: ");
    scanf("%d",&n);
    while (i<9){
        i++;
        printf("%d * %d = %d\n",n,i,n*i);
    }
}*/

/*int main(){
    int score = 0;
    double sum = 0, average = 0;
    printf("?��?��?�� ?��?��?�� 종료?��?���? ?��?���? ?��?��?��주세?��.\n");
    while(score>=0){
        average++;
        printf("?��?���? ?��?��?�� 주세?��: ");
        scanf("%d",&score);
        sum += score;
    }
    printf("?���? ?��?��?�� %.1lf?��?��?��.",sum/average);
}*/

/*int main(){ 
    int sum = 0;
    int num ;
    do{
        printf("?��?���? ?��?��?��?��?��: ");
        scanf("%d",&num);
        sum += num;
    }while(num != 0);
    printf("?��?��?�� ?��?��?��?�� ?��: %d\n",sum);
    return 0;
}*/

/*int main(){
    int i,sum;
    printf("1�??�� 10까�???�� ?��?�� 구합?��?��.\n");
    for(i=1;i<=10;i++){
        sum += i;
    }
    printf("1�??�� 10까�???�� ?��??? %d?��?��?��.\n",sum);
}*/

/* int main(){
    int n,factorial;
    printf("?��?���? ?��?��?��?��?��: ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        factorial *= i;
    }
    printf("%d! = %d\n",n,factorial);
} */

/*int main(){
    int n,sum=0;
    char c;
    while(1){
        printf("?��?���? ?��?��?��?��?��: ");
        scanf("%d",&n);        
        printf("계속?��?��겠습?���??(y/n): ");
        scanf("%c",&c);
        sum += n;
        if(c == 'n'){
            break;
        }
    }
    printf("?���?: %d\n",sum);
} */

/* int main(){
    char ch;
    char letter;
    while(1){
        printf("문자�? ?��?��?��?��?��: (?��문자�? ?��?��?��주세?��, 종료?��?���? Q�? ?��?��?��주세?��))");
        scanf("%c",&letter);
        ch = letter-32;
        if(letter == 'Q')
            break;
        if ( letter <'a' || letter > 'z')
            printf("???문자�? �??��: %c",ch);
    }
} */

int main(){
    char i;
    for (i=0;i<=10;i++){
        if(i%3 == 0)
            continue;
        printf("%d\n",i);
    }
}