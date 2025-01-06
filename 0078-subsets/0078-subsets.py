class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []
        n = len(nums)

        def dfs(i):
            if i >= n:
                ret.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # dont include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return ret