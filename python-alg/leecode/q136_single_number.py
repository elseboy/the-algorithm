def find_single_number(nums):
    num_set = set()
    for i in nums:
        if i in num_set:
            num_set.remove(i)
        else:
            num_set.add(i)
    return num_set.pop()


def bit_solution(nums):
    result = 0

    for num in nums:
        result ^= num
        print(result)
    return result


nums = [4, 1, 2, 1, 2]
print(bit_solution(nums))
