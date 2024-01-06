def generate(n):
    def backtrack(s, l, r):
        if len(s) == 2 * n:
            res.append(s)
            return

        if l < n:
            backtrack(s + "(", l + 1, r)
        if r < l:
            backtrack(s + ")", l, r + 1)

    res = []
    backtrack("", 0, 0)
    return res


n = 3
print(generate(n))
