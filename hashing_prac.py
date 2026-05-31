n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# how many times values of m appear in n return the count
# constraint=n[i]<10
# count = []
# for i in m:
#     value = 0
#     for j in n:
#         if i == j:
#             value += 1
#     count.append(value)

# print(count)

# method2
# hash_map = [0] * 11
# for i in n:
#     hash_map[i] += 1
# count = []
# for j in m:
#     if j < len(hash_map):
#         count.append(hash_map[j])
#     else:
#         count.append(0)
# print(count)

# method3 using dictionary
hash_map = {}
count = []
for i in range(0, len(n)):
    hash_map[n[i]] = hash_map.get(n[i], 0) + 1
for j in m:
    count.append(hash_map.get(j, 0))
print(count)
