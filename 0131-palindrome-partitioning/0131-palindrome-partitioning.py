class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        sub = []

        def dfs(i):
            if i >= len(s):
                ans.append(sub[:])
                return 
            
            for j in range(i, len(s)):
                temp = s[i: j + 1]
                if temp == temp[::-1]:
                    sub.append(temp[:])
                    dfs(j + 1)
                    sub.pop()
        
        dfs(0)
        return ans