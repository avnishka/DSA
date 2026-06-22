# slicing approach
# s = "nitin"
# s2 = s[::-1]
# if s == s2:
#     print("palindrome")
# else:
#     print("not palindrome")

# 2 pointer approach
# left = 0
# right = len(s) - 1
# while left < right:
#     if s[left] == s[right]:
#         left += 1
#         right -= 1
#     else:
#         print("not palindrome")
#         break
# else:
#     print("palindrome")


# def palindrome(s, left, right):
#     if left < right:
#         if s[left] == s[right]:
#             palindrome(s, left + 1, right - 1)
#         else:
#             print("not palindrome")
#             return
#     else:
#         print("TRUE")
#         return


# palindrome("hahahahahahah", 0, len("hahahahahahah") - 1)


def pal(s, l, r):
    if r > l:
        if s[l] != s[r]:
            return False
        pal(s, l + 1, r - 1)
    return True


print(pal("hahahahahahah", 0, 4))
