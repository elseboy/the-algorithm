def summaryRanges(nums):
    res = []
    start, end = nums[0], nums[0]

    def format_ranges(start, end):
        if start == end:
            return str(start)
        else:
            return f"{start}->{end}"

    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            res.append(format_ranges(start, end))
            start = end = num

    res.append(format_ranges(start, end))
    print(res)

    return


nums = [10, 11, 12, 14, 16, 17]
print(summaryRanges(nums))
