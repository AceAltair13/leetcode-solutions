class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ansLen = 0

        for i in range(len(s)):
            # Odd length palindrome (has a center)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ansLen:
                    ans = s[l: r + 1]
                    ansLen = r - l + 1
                l -= 1
                r += 1
            
            # Even length palindrome (has 2 centers)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ansLen:
                    ans = s[l: r + 1]
                    ansLen = r - l + 1
                l -= 1
                r += 1
        
        return ans