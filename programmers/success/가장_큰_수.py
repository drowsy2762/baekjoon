# 2026-09-08


def solution(numbers):
    str_nums = [str(n) for n in numbers]
    str_nums.sort(key=lambda x: x * 3, reverse=True)
    result = "".join(str_nums)
    if result[0] == "0":
        return "0"

    return result
