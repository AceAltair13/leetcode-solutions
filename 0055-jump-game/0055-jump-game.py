class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, j = 0, 0
        n = len(nums)

        while i <= j and j < n:
            j = max(j, i + nums[i])
            i += 1
        
        return j >= n - 1