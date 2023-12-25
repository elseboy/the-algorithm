def successfulPairs(spells, potions, success):
    potions.sort()
    res = []

    for s in spells:
        l, r = 0, len(potions) - 1
        index = len(potions)

        while l <= r:
            mid = (l + r) // 2
            if s * potions[mid] >= success:
                r = mid - 1
                index = mid
            else:
                l = mid + 1

        res.append(len(potions) - index)

    return res


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))
