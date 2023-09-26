# ## 각 품목의 매입가와 판매가를 리스트로 저장합니다.
# purchase_prices = [500, 900, 800, 3500, 700, 1000]
# selling_prices = [1200, 1400, 1000, 4000, 1500, 2000]


# # 품목의 개수를 저장합니다.
# def index_list():
#     print("1. 캔커피")
#     print("2. 삼각김밥")
#     print("3. 바나나 우유")
#     print("4. 도시락")
#     print("5. 콜라")
#     print("6. 새우깡")


# # 입력받은 품목이 몇 번째 인덱스에 해당하는지 찾습니다.
# def find_index(item):
#     if item == 1:
#         return 0
#     elif item == 2:
#         return 1
#     elif item == 3:
#         return 2
#     elif item == 4:
#         return 3
#     elif item == 5:
#         return 4
#     elif item == 6:
#         return 5
#     else:
#         print("잘못된 품목을 입력하셨습니다.")


# # 입력받은 품목의 매출을 계산합니다.
# def calculate_revenue(item):
#     if item != -1:
#         revenue = selling_prices[item] * quantity - purchase_prices[item] * quantity
#         print("매출은", revenue, "원입니다.")
#     else:
#         print("잘못된 품목을 입력하셨습니다.")
#     return revenue


# total = 0

# # 사용자로부터 구매한 품목과 수량을 입력받습니다.
# while True:
#     index_list()
#     item = input("판매한 품목을 입력하세요: ")
#     quantity = int(input("판매한 수량을 입력하세요: "))
#     item = find_index(int(item))
#     total += calculate_revenue(item)
#     if input("더 팔린 물건이 있습니까?? (y/n) ") == "n":
#         break

# print("총 매출은", total, "원입니다.")
