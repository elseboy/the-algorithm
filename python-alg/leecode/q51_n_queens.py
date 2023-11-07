def solve_n_queens(n):
    col = set()
    posDiag = set()  # (r + c)
    navDiag = set()  # (r - c)

    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in navDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            navDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            navDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return result


n = 4
print(solve_n_queens(n))
