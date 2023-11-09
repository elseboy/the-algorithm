def top_k_frequent_elements(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    print(freq)

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    print(freq)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(top_k_frequent_elements(nums, k))
