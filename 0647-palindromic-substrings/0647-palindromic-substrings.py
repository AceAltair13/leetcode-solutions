class Solution:
    def countSubstrings(self, s: str) -> int:
        # Similar to LeetCode 5

        ans = 0

        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        return ans
