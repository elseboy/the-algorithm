def groupAnagrams(strs):
    str_map = {}

    for s in strs:
        key = ''.join(sorted(s))

        if key not in str_map:
            str_map[key] = []
        str_map[key].append(s)
    
    return list(str_map.values()) 


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
