def strStr(haystack, needle):
    if not needle:  # 首先判断特殊情况，如果needle字符串是空的情况，返回0
        return 0
    n = len(haystack)  # len函数用来获得字符串的长度
    m = len(needle)  # 计算两个字符串的长度
    for i in range(n - m + 1):  # 开始循环因为窗口的长度是needle字符串的长度，因此注意一下for循环语句结束的位置
        if haystack[i : i + m] == needle[:]:  # 如果在窗口长度字符串是相同的
            return i  # 返回第i个字符串的位置
    return -1  # 如果没找到，返回-1


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
