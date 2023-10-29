def find_majority_element(nums):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    most_common = max(num_counts, key=num_counts.get)
    return most_common


nums = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(nums))
