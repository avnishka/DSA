# TLE ERROR METHOD 1
# # def maxProfit(self, prices: List[int]) -> int:
#     maxi = 0
#     n = len(prices)
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             if prices[j] > prices[i]:
#                 p = prices[j] - prices[i]
#                 maxi = max(p, maxi)
#     return maxi


# print(maxProfit([7, 1, 5, 3, 6, 4]))

# OPTIMAL WAY
def maxProfit(prices):
    maxi = 0
    mini = float("inf")
    n = len(prices)
    for i in range(0, n):
        mini = min(mini, prices[i])
        maxi = max(maxi, prices[i] - mini)
    return maxi


print(maxProfit([7, 1, 5, 3, 6, 4]))
