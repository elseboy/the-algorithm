def maxVowels(s, k):
    vowels = set("aeiou")

    max_vowels = curr_vowels = sum(ch in vowels for ch in s[:k])

    for i in range(k, len(s)):
        curr_vowels += s[i] in vowels
        curr_vowels -= s[i - k] in vowels
        max_vowels = max(max_vowels, curr_vowels)

    return max_vowels


s = "abciiidef"
k = 3
print(maxVowels(s, k))
