# 아리스토텔레스의체
def prime_list():
    n = 10000
    sieve = [True] * n
    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]


prime = prime_list()
