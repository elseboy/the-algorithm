from collections import deque


def sliding_window_maximun(nums, k):
    queue = deque()
    for i in range(k):
        while queue and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
    res = [queue[0]]
    print(queue)
    print()
    for i in range(k, len(nums)):
        if queue[0] == nums[i - k]:
            queue.popleft()
        while queue and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])
        print(queue)
        res.append(queue[0])
    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximun(nums, k))
