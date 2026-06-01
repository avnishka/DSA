# print a name 4 times using recursion (head)
# count = 0


# def name():
#     global count
#     if count == 4:
#         return
#     print("Avnishka")
#     count += 1
#     name()


# name()
# same question but by tail recursion
# count = 0


# def name():
#     global count
#     if count == 4:
#         return
#     count += 1
#     name()
#     print("Avnishka")


# name()

# same quetion with parameters print x n times


# def name(x, n):
#     if n == 0:
#         return
#     print(x)
#     name(x, n - 1)


# name("Avni", 4)

# print num i to n using recursion:
# def num(i, n):
#     if i > n:
#         return
#     print(i)
#     num(i + 1, n)


# num(1, 5)

# sum (n ) by parameterized recursion
#
# def summing(sum, i, n):
#     if i > n:
#         print(sum)
#         return
#     summing(sum + i, i + 1, n)


# summing(0, 1, 4)

# sum(n) by functional recursion
#
# def sum_fun(n):
#     if n == 0:
#         return 0
#     return n + sum_fun(n - 1)


# print(sum_fun(4))

# factorial of a number by rec
#
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))
