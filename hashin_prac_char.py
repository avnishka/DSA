s = "azyxyyzaaaaAQ"
q = ["d", "a", "y", "x", "A"]

# count = []
# hash_map = [0] * 26
# for ch in s:
#     ascii_val = ord(ch)
#     index_val = ascii_val - 97
#     hash_map[index_val] += 1
# for item in q:
#     ascii = ord(item)
#     index = ascii - 97
#     count.append(hash_map[index])
# print(count)
count = []
hash_map = [0] * 128
for ch in s:
    ascii_val = ord(ch)
    hash_map[ascii_val] += 1
for item in q:
    ascii = ord(item)
    count.append(hash_map[ascii])
print(count)
