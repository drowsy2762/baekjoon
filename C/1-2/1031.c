#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// int main()
// {
//     // 동적메모리 할당
//     // 열글자 입력받을 수 있는 메모리를 할당하고, 입력받은 글자를 저장하고 출력하시오.
//     char ch[20] = "test string";
//     char *p[10];
//     for (int i = 0; i < 10; i++)
//     {
//         p[i] = (char *)malloc(sizeof(char) * 20);
//         if (p[i] == NULL)
//         {
//             printf("동적메모리 할당 실패\n");
//             exit(1);
//         }

//         strcpy(p[i], ch);
//     }

//     for (int i = 0; i < 10; i++)
//     {
//         printf("%s\n", p[i]);
//     }
// }

int main(void)
{
    char ch[20];
    char *p[10];

    for (int i = 0; i < 10; i++)
    {
        gets(ch);
        p[i] = (char *)malloc(strlen(ch) + 1);
        if (p[i] == NULL)
        {
            printf("동적메모리 할당 실패\n");
            exit(1);
        }
        strcpy(p[i], ch);
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%s\n", p[i]);
    }

    return 0;
}