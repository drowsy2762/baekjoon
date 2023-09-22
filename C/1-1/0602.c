#include <stdio.h>

// int main(){
//     int i, j , temp;
//     int arr[5] = {5, 4, 3, 2, 1};
//     //정렬
//     for(i = 0 ; i < 5 ; i++){
//         for(j = 0 ; j < 5 ; j++){
//             if(arr[i] < arr[j]){
//                 temp = arr[i];
//                 arr[i] = arr[j];
//                 arr[j] = temp;
//             }
//         }
//     }
//     for(i = 0 ; i < 5 ; i++){
//         printf("%d ", arr[i]);
//     }

// }

// int main(){
//     int i, j, temp;
//     int arr[5] = {5, 4, 3, 2, 1};
//     for(i = 0 ; i < 5 ; i++){
//         for(j = 0 ; j < 5 - i ; j++){
//             if(arr[j] > arr[j + 1]){
//                 temp = arr[j + 1];
//                 arr[j + 1] = arr[j];
//                 arr[j] = temp;
//             }
//         }
//     }
//     for(i = 0 ; i < 5 ; i++){
//         printf("%d ", arr[i]);
//     }
// }

int main(){
    int arr[5] = {1,2,3,4,5};
    int num[5][5] = {0,};
    for(int i = 0 ; i < 5 ; i++){
        for(int j = 0 ; j < 5-i ; j++){
            printf("%d ", arr[j+i]);
            num[i][j] = arr[j+i];
        }
        for(int j = 5-i ; j < 5 ; j++){
            printf("0 ");
            num[i][j] = 0;
        }
        printf("\n");
    }

    for(int i = 0 ; i < 5 ; i++){
        for(int j = 0 ; j < 5 ; j++){
            printf("%d ", num[i][j]);
        }
        printf("\n");
    }
}