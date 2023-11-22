def reverseBits(n):
    result = 0
    power = 31

    while n:
        # Extract the rightmost bit from n and add it to the result
        result += (n & 1) << power
        n >>= 1
        power -= 1

    return result


n = 43261596
print(reverseBits(n))
