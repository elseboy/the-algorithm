def group_anagrams(str_arr):
    str_map = {}
    for s in str_arr:
        key = "".join(sorted(s))
        if key not in str_map:
            str_map[key] = []
        str_map[key].append(s)

    return list(str_map.values())


string = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(string))
