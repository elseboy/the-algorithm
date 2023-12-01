def largestAltitude(gain):
    n = len(gain)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + gain[i]

    max_alt = max(prefix_sum)

    return max_alt


gain = [-5, 1, 5, 0, -7]
print(largestAltitude(gain))
