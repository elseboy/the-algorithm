def daily_temperatures(nums):
    result = [0] * len(nums)
    stack = []

    for i, t in enumerate(nums):
        while stack and t > stack[-1][0]:
            stackTe, stackIn = stack.pop()
            result[stackIn] = i - stackIn
        stack.append([t, i])
    return result


temperatures = [30, 40, 50, 60]
print(daily_temperatures(temperatures))
