def union(a, b):
    n = len(a)
    m = len(b)
    map = {}
    i, j = 0, 0
    while i < n and j < m:
        if a[i] < b[j]:
            map[a[i]] = 0
            i += 1
        else:
            map[b[j]] = 0
            j += 1
    while i < n:
        map[a[i]] = 0
        i += 1
    while j < m:
        map[b[j]] = 0
        j += 1
    new = list(map.keys())
    return new


print(union([1, 2, 3], [2, 3, 4]))
