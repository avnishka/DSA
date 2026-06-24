# try 1 / method 1
def findMaxConsecutiveOnes(nums):
    n = len(nums) + 1
    result = []
    count = 0
    nums.append(0)
    for i in range(0, n):
        if nums[i] == 1:
            count += 1
        elif nums[i] == 0:
            result.append(count)
            count = 0

    return max(result)


nums = [1, 1, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))
