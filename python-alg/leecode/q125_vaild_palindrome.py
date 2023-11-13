def vaild(s):
    new_str = [char.lower() for char in s if char.isalnum()]
    print(new_str)

    l, r = 0, len(new_str) - 1

    while l < r:
        if new_str[l] != new_str[r]:
            return False
        l += 1
        r -= 1
    return True


s = 'Marge, let\'s "[went]." I await {news} telegram.'
print(vaild(s))
