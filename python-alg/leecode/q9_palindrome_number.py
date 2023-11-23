def isPalindrome(num):
    s = str(num)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    print(left, right)
    return True


num = 121
print(isPalindrome(num))
