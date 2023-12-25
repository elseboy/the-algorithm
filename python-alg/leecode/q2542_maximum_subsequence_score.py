import heapq


def maxScore(nums1, nums2, k):
    print(nums1)
    print(nums2)

    pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
    print(pairs)

    pairs = sorted(pairs, key=lambda p: p[1], reverse=True)
    print(pairs)

    minHeap = []
    n1Sum = 0
    result = 0

    for n1, n2 in pairs:
        n1Sum += n1
        heapq.heappush(minHeap, n1)

        if len(minHeap) > k:
            pop = heapq.heappop(minHeap)
            n1Sum -= pop
        if len(minHeap) == k:
            result = max(result, n1Sum * n2)

    return result


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
print(maxScore(nums1, nums2, k))
