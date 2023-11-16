def isHappy(n):
    def get_next(number):
        return sum(int(digit) ** 2 for digit in str(number))

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
        print(n)

    return n == 1


n = 19
print(isHappy(n))
