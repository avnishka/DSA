# from collections import *
# from math import *
# from os import *
# from sys import *

# x = int(input("Enter a number"))


# def countDigit(n: int) -> int:
#     if n == 0:
#         return 1
#     n = abs(n)
#     count = 0
#     while n > 0:
#         n = n // 10
#         count += 1
#     return count


# print(countDigit(x))

from collections import *
from math import *
from os import *
from sys import *


def countDigit(n: int) -> int:
    # Write your code here.
    return int(log10(n) + 1)
