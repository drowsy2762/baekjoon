# M, N = map(int, input().split())
# # 에라토스테네스의 체
# # 리스트를 생성하고 모든 값을 True로 초기화
# array = [True for _ in range(0, N + 1)]

# # 0과 1은 소수가 아니므로 False로 초기화
# array[1] = False

# # 2부터 N의 제곱근까지의 모든 수를 확인하며
# # i가 소수인 경우 i를 제외한 i의 모든 배수를 지우기
# # n+1을 해주는 이유는 n까지만 확인하기 때문에
# for x in range(2, N + 1):
#     if array[x] == True:
#         for y in range(x + x, N + 1, x):
#             array[y] = False

# # M부터 N까지의 모든 소수 출력
# for x in range(M, N + 1):
#     if array[x] == True:
#         print(x)


M, N = map(int, input().split())
array = [True for a in range(0, N + 1)]
# m 이하의 수는 구하는 값이 아니여서 초기화
for c in range(0, M - 1):
    array[c] = False

for x in range(2, N + 1):
    if array[x - 1] == True:
        for y in range(x + x, N + 1, x):
            array[y - 1] = False


for a in range(0, N + 1):
    if array[a] == True:
        print(a)
