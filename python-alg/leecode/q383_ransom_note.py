def canConstruct(ran, mag):
    counter = {}

    for m in mag:
        counter[m] = counter.get(m, 0) + 1

    print(counter)

    for r in ran:
        if r not in counter or counter[r] == 0:
            return False

        counter[r] -= 1

    return True


ran = "aa"
mag = "ab"
print(canConstruct(ran, mag))
