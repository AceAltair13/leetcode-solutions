class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = sum(1 for x in s[: k] if x in {'a', 'e', 'i', 'o', 'u'})
        i, max_vowels = 0, vowels

        while i + k < len(s):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                vowels -= 1
            if s[i + k] in {'a', 'e', 'i', 'o', 'u'}:
                vowels += 1
            i += 1
            max_vowels = max(max_vowels, vowels)
        
        return max_vowels