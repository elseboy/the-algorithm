def pascals_triangle(num):
    ans = [[1]]
    for i in range(1, num):
        temp = ans[-1][:]
        temp.insert(0, 0)
        temp.append(0)

        next_row = []
        for j in range(len(ans) + 1):
            next_row.append(temp[j] + temp[j + 1])
        ans.append(next_row)
    return ans


output = pascals_triangle(3)
for arr in output:
    print(arr)
