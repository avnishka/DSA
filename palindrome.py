
m=int(input("Enter a number "+""))

def isPalindrome(x: int) -> bool:
    num  =x
    reverse=0
    while (num>0):
        digit=num%10
        reverse= reverse*10+digit
        num=num//10
    return x==reverse

print(isPalindrome(m))
