def jump_game_two(nums):
    result = 0
    l = r = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])

        l = r + 1
        r = farthest
        result += 1

    return result


nums = [2, 3, 1, 1, 4]
print(jump_game_two(nums))
