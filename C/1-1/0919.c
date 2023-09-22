#include <stdio.h>

// int main(){
//     int i, j, temp;
//     int a[5] = {5, 4, 3, 2, 1};
//     printf("%d \n", &a[0]);
//     printf("%d \n", &a[1]);

//     printf("%u \n", a);
//     printf("%u \n", a + 1);
// }

// int main(){
//     int a[10] = {10,20,30,40,50,60,70,80,90,100};
//     int *p = a;

//     printf("%d \n", *p);
//     p[0] = 1000;
//     p[1] = 2000;

//     printf("%d \n", *p);
//     printf("%d \n", *(p+1));
//     printf("%d \n", *(p+2));

//     printf("%d \n", p[0]);
//     printf("%d \n", p[1]);
//     printf("%d \n", p[2]);
// }

// int main(){
//     int a[5] = {10,20,30,40,50};
//     int *p = a;

//     printf("a[0] = %d a[1] = %d a[2] = %d \n", a[0], a[1], a[2]);
//     printf("p[0] = %d p[1] = %d p[2] = %d \n", p[0], p[1], p[2]);

//     p[0] = 60;
//     p[1] = 70;
//     p[2] = 80;

//     printf("a[0] = %d a[1] = %d a[2] = %d \n", a[0], a[1], a[2]);
//     printf("p[0] = %d p[1] = %d p[2] = %d \n", p[0], p[1], p[2]);

// }

// void sub(int b[], int n);

// int main(void)
// {
//     int a[3] = {1, 2, 3};
//     printf("%d %d %d\n", a[0], a[1], a[2]);
//     sub(a, 3);
//     printf("%d %d %d\n", a[0], a[1], a[2]);
//     return 0;
// }

// void sub(int b[], int n)
// {
//     b[0] = 4;
//     b[1] = 5;
//     b[2] = 6;
// }

void brighten_image(int image[5][5])
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            image[i][j] += 10;
        }
    }
}

void brighten_image2(int *p)
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            *(p + i * 5 + j) += 10;
        }
    }
}

void print_image(int image[5][5])
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            printf("%d ", image[i][j]);
        }
        printf("\n");
    }
}

void print_image2(int b[5][5])
{
    int *p[5] = b;
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; i++)
        {
            printf("%d ", *(p + i * 5 + j));
        }
        printf("\n");
    }
}

int main()
{
    int image[5][5] = {
        {1, 1, 1, 1, 1},
        {1, 0, 0, 0, 1},
        {1, 0, 9, 0, 1},
        {1, 0, 0, 0, 1},
        {1, 1, 1, 1, 1}};
    int(*p)[5][5] = &image;
    print_image2(image);
    brighten_image2(image);
    print_image2(image);

    printf("%d \n", *p[0][0]);
    return 0;
}
