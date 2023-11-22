def hammingWeight(n):
    count = 0

    while n:
        count += n & 1
        print(count)
        n >>= 1
    return count


n = 11
print(hammingWeight(n))
