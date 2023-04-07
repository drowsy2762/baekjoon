#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

/*int main(){
    int i = 0;
    int n = 0;
    printf("êµ¬êµ¬?‹¨?˜ ?‹œ?‘? ?„ ?…? ¥?•´ì£¼ì„¸?š”: ");
    scanf("%d",&n);
    while (i<9){
        i++;
        printf("%d * %d = %d\n",n,i,n*i);
    }
}*/

/*int main(){
    int score = 0;
    double sum = 0, average = 0;
    printf("? ?ˆ˜?˜ ?…? ¥?„ ì¢…ë£Œ?•˜? ¤ë©? ?Œ?ˆ˜ë¥? ?…? ¥?•´ì£¼ì„¸?š”.\n");
    while(score>=0){
        average++;
        printf("? ?ˆ˜ë¥? ?…? ¥?•´ ì£¼ì„¸?š”: ");
        scanf("%d",&score);
        sum += score;
    }
    printf("?‰ê·? ? ?ˆ˜?Š” %.1lf?…?‹ˆ?‹¤.",sum/average);
}*/

/*int main(){ 
    int sum = 0;
    int num ;
    do{
        printf("? •?ˆ˜ë¥? ?…? ¥?•˜?„¸?š”: ");
        scanf("%d",&num);
        sum += num;
    }while(num != 0);
    printf("?…? ¥?•œ ? •?ˆ˜?“¤?˜ ?•©: %d\n",sum);
    return 0;
}*/

/*int main(){
    int i,sum;
    printf("1ë¶??„° 10ê¹Œì???˜ ?•©?„ êµ¬í•©?‹ˆ?‹¤.\n");
    for(i=1;i<=10;i++){
        sum += i;
    }
    printf("1ë¶??„° 10ê¹Œì???˜ ?•©??? %d?…?‹ˆ?‹¤.\n",sum);
}*/

/* int main(){
    int n,factorial;
    printf("? •?ˆ˜ë¥? ?…? ¥?•˜?„¸?š”: ");
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
        printf("? •?ˆ˜ë¥? ?…? ¥?•˜?„¸?š”: ");
        scanf("%d",&n);        
        printf("ê³„ì†?•˜?‹œê² ìŠµ?‹ˆê¹??(y/n): ");
        scanf("%c",&c);
        sum += n;
        if(c == 'n'){
            break;
        }
    }
    printf("?•©ê³?: %d\n",sum);
} */

int main(){
    char ch;
    char letter;
    while(1){
        printf("ë¬¸ìë¥? ?…? ¥?•˜?„¸?š”: (?†Œë¬¸ìë¥? ?…? ¥?•´ì£¼ì„¸?š”, ì¢…ë£Œ?•˜? ¤ë©? Që¥? ?…? ¥?•´ì£¼ì„¸?š”))");
        scanf("%c",&letter);
        ch = letter-32;
        if(letter == 'Q')
            break;
        if ( letter <'a' || letter > 'z')
            printf("???ë¬¸ìë¡? ë³??™˜: %c",ch);
    }
}