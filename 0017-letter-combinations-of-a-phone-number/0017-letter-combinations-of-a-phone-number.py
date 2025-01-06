class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {
            '2':"abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz" 
        }

        ans = []

        def dfs(i, curr):

            if len(curr) == len(digits):
                if curr:
                    ans.append(curr)
                return 
            
            for c in phone[digits[i]]:
                dfs(i + 1, curr + c)
        
        dfs(0, "")
        return ans