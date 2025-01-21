class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        
        for c in s:
            if c in "aeiouAEIOU":
                vowels.append(c)

        ans = ""

        for c in s:
            if c in "aeiouAEIOU":
                ans += vowels.pop()
            else:
                ans += c
        
        return ans


        