#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

/*int main(){
    int i = 0;
    int n = 0;
    printf("κ΅¬κ΅¬?¨? ??? ? ?? ₯?΄μ£ΌμΈ?: ");
    scanf("%d",&n);
    while (i<9){
        i++;
        printf("%d * %d = %d\n",n,i,n*i);
    }
}*/

/*int main(){
    int score = 0;
    double sum = 0, average = 0;
    printf("? ?? ?? ₯? μ’λ£?? €λ©? ??λ₯? ?? ₯?΄μ£ΌμΈ?.\n");
    while(score>=0){
        average++;
        printf("? ?λ₯? ?? ₯?΄ μ£ΌμΈ?: ");
        scanf("%d",&score);
        sum += score;
    }
    printf("?κ·? ? ?? %.1lf???€.",sum/average);
}*/

/*int main(){ 
    int sum = 0;
    int num ;
    do{
        printf("? ?λ₯? ?? ₯??Έ?: ");
        scanf("%d",&num);
        sum += num;
    }while(num != 0);
    printf("?? ₯? ? ??€? ?©: %d\n",sum);
    return 0;
}*/

/*int main(){
    int i,sum;
    printf("1λΆ??° 10κΉμ??? ?©? κ΅¬ν©??€.\n");
    for(i=1;i<=10;i++){
        sum += i;
    }
    printf("1λΆ??° 10κΉμ??? ?©??? %d???€.\n",sum);
}*/

/* int main(){
    int n,factorial;
    printf("? ?λ₯? ?? ₯??Έ?: ");
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
        printf("? ?λ₯? ?? ₯??Έ?: ");
        scanf("%d",&n);        
        printf("κ³μ??κ² μ΅?κΉ??(y/n): ");
        scanf("%c",&c);
        sum += n;
        if(c == 'n'){
            break;
        }
    }
    printf("?©κ³?: %d\n",sum);
} */

int main(){
    char ch;
    char letter;
    while(1){
        printf("λ¬Έμλ₯? ?? ₯??Έ?: (?λ¬Έμλ₯? ?? ₯?΄μ£ΌμΈ?, μ’λ£?? €λ©? Qλ₯? ?? ₯?΄μ£ΌμΈ?))");
        scanf("%c",&letter);
        ch = letter-32;
        if(letter == 'Q')
            break;
        if ( letter <'a' || letter > 'z')
            printf("???λ¬Έμλ‘? λ³??: %c",ch);
    }
}