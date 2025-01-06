class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(i, curr, total):

            if total == target:
                ans.append(curr[:])
                return
            
            if i == len(candidates) or total >= target:
                return

            # include candidates[i]
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])
            curr.pop()

            # do not include candidates[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr, total)
        
        backtrack(0, [], 0)
        return ans
