class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(i, curr, total):

            # target achieved
            if target == total:
                ans.append(curr.copy())
                return
            
            # base exit case
            if i >= len(candidates) or total > target:
                return
            
            # include candidates[i]
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            
            # dont include candidates[i]
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return ans