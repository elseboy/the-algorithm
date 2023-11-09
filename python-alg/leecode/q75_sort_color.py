def sort_color(nums):
    count = {0: 0, 1: 0, 2: 0}

    for num in nums:
        count[num] += 1

    nums.clear()

    for color, freq in count.items():
        nums.extend([color] * freq)

    print(nums)


nums = [2, 0, 2, 1, 1, 0]
sort_color(nums)
