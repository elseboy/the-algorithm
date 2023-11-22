import heapq


def kSmallestPairs(nums1, nums2, k):
    result = []
    min_heap = []

    for i in range(min(k, len(nums1))):
        heapq.heappush(min_heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

    while k > 0 and min_heap:
        curr_sum, n1, n2, index = heapq.heappop(min_heap)
        result.append([n1, n2])

        if index + 1 < len(nums2):
            heapq.heappush(
                min_heap, (n1 + nums2[index + 1], n1, nums2[index + 1], index + 1)
            )
        k -= 1

    return result


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

print(kSmallestPairs(nums1, nums2, k))
