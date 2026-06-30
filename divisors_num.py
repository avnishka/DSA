from math import sqrt


def divisors_num(n):
    count = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            count.append(i)
            if i != n // i:
                count.append(n // i)
    count.sort()
    return count


n = int(input("Enter a number: "))
print(divisors_num(n))
