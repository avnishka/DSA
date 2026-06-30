def armstrong_num():
    n = 153
    num = n
    total = 0
    m = len(str(n))
    while num > 0:
        ld = num % 10
        total = total + (ld**m)
        num //= 10
    return total == n


print(armstrong_num())
